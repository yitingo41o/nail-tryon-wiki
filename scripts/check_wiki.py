#!/usr/bin/env python3
"""Wiki 自動檢查（CLAUDE.md 第 3.3、7 節）。

檢查項目：
  1. 所有相對路徑的 Markdown 連結都指到存在的檔案
  2. 沒有孤兒頁（每頁至少被另一頁連到）
  3. index.md 列出所有 sources / concepts / comparisons 頁
  4. sources 頁：固定段落齊全且順序正確
  5. sources 頁「重點」：每點都有精確出處（§ / Table / Fig. / Abstract）
  6. concepts / comparisons 頁「重點」：每點都連到 sources，或標〔綜合推論〕
並列出所有〔待確認〕的位置。
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)#\s]+)(?:#[^)]*)?\)")
SOURCE_SECTIONS = ["一句話", "在試戴流程中的位置", "重點", "關於曲面與光影", "限制", "待確認", "相關頁面"]
PRECISE_REF = re.compile(r"〔[^〕]*(§\s*\d|Table\s*\d|Fig\.?\s*\d|Abstract)[^〕]*〕")

errors, warnings = [], []


def md_files():
    return sorted(p for p in WIKI.rglob("*.md"))


def section(text, title):
    """回傳 '## title' 底下到下一個 '## ' 之前的內容。"""
    m = re.search(rf"^## {re.escape(title)}\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
    return m.group(1) if m else None


def bullets(block):
    return [ln.strip() for ln in block.splitlines() if re.match(r"^\s*(-|\d+\.)\s", ln)]


# 1 & 2: links and orphans
inbound = {p: 0 for p in md_files()}
for p in md_files() + [ROOT / "CLAUDE.md", ROOT / "README.md", ROOT / "raw" / "sources.md"]:
    if not p.exists():
        continue
    for target in LINK_RE.findall(p.read_text(encoding="utf-8")):
        if target.startswith(("http://", "https://", "mailto:")):
            continue
        dest = (p.parent / target).resolve()
        if not dest.exists():
            errors.append(f"[壞連結] {p.relative_to(ROOT)} → {target}")
        elif dest in inbound and dest != p:
            inbound[dest] += 1
for p, n in inbound.items():
    if n == 0 and p.name != "index.md":
        errors.append(f"[孤兒頁] {p.relative_to(ROOT)} 沒有被任何頁面連到")

# 3: index completeness
index_text = (WIKI / "index.md").read_text(encoding="utf-8")
for sub in ("sources", "concepts", "comparisons"):
    for p in sorted((WIKI / sub).glob("*.md")):
        if f"{sub}/{p.name}" not in index_text:
            errors.append(f"[index 缺漏] index.md 沒有列出 {sub}/{p.name}")

# 4 & 5: source pages
for p in sorted((WIKI / "sources").glob("*.md")):
    text = p.read_text(encoding="utf-8")
    found = re.findall(r"^## (.+?)\s*$", text, re.M)
    if found != SOURCE_SECTIONS:
        errors.append(f"[段落] {p.name} 段落為 {found}，應為 {SOURCE_SECTIONS}")
        continue
    for b in bullets(section(text, "重點")):
        if not PRECISE_REF.search(b):
            ref = re.findall(r"〔[^〕]*〕", b)
            errors.append(f"[出處不精確] {p.name}：「{b[:40]}…」出處 {ref or '無'}")

# 6: concept / comparison pages
for sub in ("concepts", "comparisons"):
    for p in sorted((WIKI / sub).glob("*.md")):
        text = p.read_text(encoding="utf-8")
        block = section(text, "重點")
        if block is None:
            errors.append(f"[段落] {sub}/{p.name} 缺少「## 重點」")
            continue
        items = bullets(block) or [ln for ln in block.splitlines() if ln.startswith("|") and "---" not in ln][1:]
        for b in items:
            if "../sources/" not in b and "〔綜合推論〕" not in b:
                errors.append(f"[無來源] {sub}/{p.name}：「{b[:40]}…」")
            elif "../sources/" in b and not re.search(r"(§\s*\d|Table\s*\d|Fig\.?\s*\d|Abstract)", b):
                errors.append(f"[出處不精確] {sub}/{p.name}：「{b[:40]}…」引用來源但沒有章節 / 表格編號")

# 7: concept / comparison 頁中的數字，必須出現在它連到的 source 頁裡
NUM_RE = re.compile(r"\d[\d,]*\.?\d*")
for sub in ("concepts", "comparisons"):
    for p in sorted((WIKI / sub).glob("*.md")):
        text = p.read_text(encoding="utf-8")
        block = section(text, "重點") or ""
        for ln in block.splitlines():
            srcs = [(p.parent / s).resolve() for s in re.findall(r"\((\.\./sources/[^)]+)\)", ln)]
            if not srcs:
                continue
            src_text = "".join(s.read_text(encoding="utf-8") for s in srcs if s.exists())
            clean = re.sub(r"\([^)]*\)|〔[^〕]*〕|§\s*[\d.]+|Table\s*\d+|Fig\.?\s*\d+", "", ln)
            for n in NUM_RE.findall(clean):
                if len(n.replace(",", "")) < 2:  # 跳過個位數（步驟編號等）
                    continue
                if n not in src_text:
                    errors.append(f"[數字對不上] {sub}/{p.name}：數字 {n} 沒有出現在引用的 source 頁")

# 待確認 report：〔待確認〕行內標記 + 「## 待確認」段落裡的每一點
todo = []
for p in md_files():
    if p.name == "log.md":  # log 只是紀錄，不算待確認項目
        continue
    lines = p.read_text(encoding="utf-8").splitlines()
    in_todo = False
    for i, ln in enumerate(lines, 1):
        if ln.startswith("## "):
            in_todo = ln.strip() == "## 待確認"
            continue
        if "〔待確認〕" in ln or (in_todo and re.match(r"^\s*-\s", ln)):
            todo.append(f"  {p.relative_to(ROOT)}:{i}  {ln.strip()[:50]}")

print(f"檢查 {len(md_files())} 個 Wiki 頁面")
for e in errors:
    print("✗", e)
print(f"〔待確認〕共 {len(todo)} 處：")
print("\n".join(todo) if todo else "  （無）")
if errors:
    print(f"\n共 {len(errors)} 個錯誤")
    sys.exit(1)
print("\n全部通過")
