#!/usr/bin/env python3
"""簡報自動檢查（CLAUDE.md 第 6 節）。

  1. 每張投影片都有 data-wiki，且列出的 Wiki 頁都存在
  2. 投影片中的每個數字，都出現在它引用的 Wiki 頁裡（可追溯）
  3. 投影片張數與 workflow/slide-outline.md 一致，且每張的 data-wiki 包含大綱列出的頁
  4. 圖片檔存在、都有 alt
  5. 沒有 Google Fonts 以外的外部資源
"""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HTML = ROOT / "slides" / "index.html"
NUM_RE = re.compile(r"\d[\d,]*(?:\.\d+)?")


class SlideParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.slides, self.imgs, self.ext = [], [], []
        self.depth = 0
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("script", "style"):
            self.skip += 1
        if tag == "section" and "slide" in a.get("class", ""):
            self.slides.append({"wiki": a.get("data-wiki"), "text": ""})
            self.depth = 1
        elif self.depth and tag == "section":
            self.depth += 1
        if tag == "img":
            self.imgs.append(a)
        for k in ("src", "href"):
            v = a.get(k, "")
            if v.startswith("http") and "fonts.g" not in v:
                self.ext.append(v)

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip -= 1
        if tag == "section" and self.depth:
            self.depth -= 1

    def handle_data(self, data):
        if self.depth and not self.skip:
            self.slides[-1]["text"] += data + " "


errors = []
parser = SlideParser()
parser.feed(HTML.read_text(encoding="utf-8"))
slides = parser.slides

# 3. outline
outline = (ROOT / "workflow" / "slide-outline.md").read_text(encoding="utf-8")
rows = [r for r in outline.splitlines() if re.match(r"^\| \d+ \|", r)]
if len(rows) != len(slides):
    errors.append(f"[大綱] 大綱有 {len(rows)} 張，簡報有 {len(slides)} 張")

for i, s in enumerate(slides, 1):
    # 1. data-wiki
    if not s["wiki"]:
        errors.append(f"[第 {i} 張] 沒有 data-wiki")
        continue
    pages = [p.strip() for p in s["wiki"].split(",")]
    texts = []
    for p in pages:
        f = ROOT / p
        if not f.exists():
            errors.append(f"[第 {i} 張] data-wiki 指到不存在的 {p}")
        else:
            texts.append(f.read_text(encoding="utf-8"))
    wiki_text = "\n".join(texts)
    # 3b. 大綱列出的頁都要在 data-wiki 裡
    if i <= len(rows):
        for ref in re.findall(r"`([^`]+\.md)`", rows[i - 1]):
            full = ref if ref.startswith("wiki/") else "wiki/" + ref
            if full not in pages:
                errors.append(f"[第 {i} 張] 大綱說會用到 {full}，但 data-wiki 沒有列出")
    # 2. numbers
    for n in sorted(set(NUM_RE.findall(s["text"]))):
        if len(n.replace(",", "").replace(".", "")) < 2:
            continue  # 個位數：步驟編號、λ = 0/1 等
        if n not in wiki_text:
            errors.append(f"[第 {i} 張] 數字「{n}」在引用的 Wiki 頁裡找不到")

# 4. images
for a in parser.imgs:
    if not (HTML.parent / a.get("src", "")).exists():
        errors.append(f"[圖片] 找不到 {a.get('src')}")
    if "alt" not in a:
        errors.append(f"[圖片] {a.get('src')} 沒有 alt")

# 5. external
for u in parser.ext:
    errors.append(f"[外部資源] {u}")

print(f"檢查 {len(slides)} 張投影片")
for e in errors:
    print("✗", e)
if errors:
    print(f"\n共 {len(errors)} 個錯誤")
    sys.exit(1)
print("全部通過")
