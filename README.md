# 穿戴甲虛擬試戴 LLM Wiki ＋ 教學 HTML 簡報

生成式 AI 作業：用 LLM Wiki 做一份教學 HTML 簡報。

- 📊 **教學簡報**：https://yitingo41o.github.io/nail-tryon-wiki/slides/
- 📚 **LLM Wiki 目錄**：[wiki/index.md](wiki/index.md)
- 🔁 **Loop / Graph 設計**：[workflow/graph.md](workflow/graph.md)
- 🧾 **執行與檢查紀錄**：[wiki/log.md](wiki/log.md)
- 💭 **反思**：[workflow/reflection.md](workflow/reflection.md)

---

## 1. LLM Wiki 主題與簡短介紹

**主題：穿戴甲虛擬試戴（virtual nail try-on）背後的技術。**

我有經營自己的手工穿戴甲品牌，期末專案想做「穿戴甲品牌 AI 小幫手」，其中最核心的技術就是虛擬試戴。這個 Wiki 要回答一個問題：

> 「直接把指甲圖貼到手上（2D 貼圖 / AR 路線）」和「用 diffusion 生成」差在哪？兩者各自怎麼處理**指甲曲面**與**光影**？

Wiki 用「先討論、後生成」的方式建立（[討論紀錄](wiki/discussion.md)），共 ingest 6 篇資料，依試戴流程的每一步各挑一篇：

| 流程步驟 | 資料 |
|---|---|
| 找到手 | MediaPipe Hands（2020） |
| 找到指甲 + 貼上去 | Nail Polish Try-On（ModiFace, 2019） |
| 生成的基礎、inpainting | Latent Diffusion Models（2021） |
| 控制形狀 | ControlNet（2023） |
| 參考款式圖 | IP-Adapter（2023） |
| 完整生成式試戴系統 | IDM-VTON（2024） |

## 2. LLM Wiki 連結與成果

- 目錄：[wiki/index.md](wiki/index.md)
- 規則（schema）：[CLAUDE.md](CLAUDE.md)，寫明三層結構（raw / wiki / 規則）、三種操作（ingest / query / lint）、頁面格式與寫作規則。沿用上週 [mamba-video-notes](https://github.com/yitingo41o/mamba-video-notes) 的誠信規則（不可捏造、數字附出處、待確認標記、檢查腳本）。

```
nail-tryon-wiki/
├── CLAUDE.md / AGENTS.md      規則
├── raw/sources.md             原始資料登記（只存連結與讀過的章節）
├── wiki/
│   ├── index.md               目錄
│   ├── log.md                 操作紀錄（ingest / lint / query）
│   ├── discussion.md          先討論、後生成的紀錄
│   ├── glossary.md            名詞表（22 個）
│   ├── sources/   (6 頁)      一篇資料一頁
│   ├── concepts/  (8 頁)      一個概念一頁，整合多篇
│   └── comparisons/ (1 頁)    2D 貼圖 vs Diffusion 比較
├── slides/index.html          教學簡報（17 張）
├── workflow/                  graph、簡報大綱、反思
└── scripts/                   check_wiki.py、check_slides.py
```

**Wiki 與簡報的對應**：每張投影片底部都列出它用到的 Wiki 頁（`data-wiki`），點了就能看到出處；投影片上的每個數字都經 `check_slides.py` 確認出現在引用的 Wiki 頁裡。對應表見 [workflow/slide-outline.md](workflow/slide-outline.md)。

## 3. 教學 HTML 簡報

**https://yitingo41o.github.io/nail-tryon-wiki/slides/**（← → 鍵換頁，手機可滑動）

教學結構：問題 → 為什麼難 → 路線一（找手 → 找指甲 → 貼圖，含**可操作的指甲貼圖示範**）→ 路線二（Diffusion → Inpainting → ControlNet → IP-Adapter → IDM-VTON）→ 比較表 → 用我的作品來想 → 混合做法 → 小測驗 → 回顧。照片都是我自己的作品。

## 4. Loop / Graph 設計

詳見 [workflow/graph.md](workflow/graph.md)（含 v1 → v2 的流程圖）。簡述：

```
討論 → [Ingest 迴圈：取得資料 →C1 完整? → 寫 source 頁 →C2 對得回原文? → 更新概念/名詞/index/log]
     → C3 Lint（腳本 + 人工）→ Query（只讀 Wiki 排大綱）→ C4 Wiki 夠嗎?
     → 生成簡報 → C5 簡報檢查（腳本 + 渲染截圖 + 初學者可讀性）→ 發布
```

- **重複執行**：每篇資料跑一次 ingest 迴圈；抓取不完整就重抓；lint 不過就回去改；簡報檢查不過就回到 Query 或重新生成；Wiki 不夠就列為下一輪 ingest。
- **需要檢查 / 重生成的地方**：C1–C5 五個檢查點，其中 C3、C5 有自動腳本。
- **為什麼**：Wiki 是唯一的事實來源，錯誤必須在進入 Wiki 時擋下；只檢查簡報抓不到「Wiki 本身就錯」的情況。

## 5. 實際執行與檢查紀錄

完整紀錄：[wiki/log.md](wiki/log.md)。重點：

| 檢查 | 結果 |
|---|---|
| lint #1（`check_wiki.py`） | 7 個錯誤：3 個壞連結、4 個出處不精確（IDM-VTON） |
| 修出處時重抓全文 | 發現第一次的摘要**誇大成績**（說 DressCode 也最好，正文沒有）→ 刪除 |
| 檢查腳本自我檢討 | 發現腳本漏算待確認、漏查概念頁出處 → 修正 |
| lint #2（人工） | 概念頁有一句來自 AI 記憶、source 頁沒有 → 回原文核對補上；新增「數字對不上」自動檢查 |
| `check_slides.py` | 全部通過；故意改錯數字確認腳本會報錯 |
| 渲染截圖 + 可讀性 | 遮罩位置錯、圖片壓到頁尾、4 個術語沒解釋 → 修正 |
| 最終狀態 | Wiki 19 頁、簡報 17 張，兩個腳本都「全部通過」；保留 6 處〔待確認〕 |

自己跑檢查：

```bash
python3 scripts/check_wiki.py
python3 scripts/check_slides.py
```

## 6. 反思

詳見 [workflow/reflection.md](workflow/reflection.md)。

- **最常出錯的節點**：取得資料 → 寫 source 頁（ingest）。10 個問題中有 7 個在這裡產生，原因是中間隔了多層 AI 摘要，容易漏、容易多講、容易被問題帶著走。
- **檢查往前移到哪裡**：從「只檢查簡報」往前移到「抓取後立刻檢查完整性」、「寫 source 頁時就要求精確章節出處」、「Wiki 層就檢查數字一致」。
- **有沒有改 graph**：有，v1（線性、最後才檢查）→ v2（5 個檢查點、多個迴圈）。因為簡報檢查只能確認「簡報忠實引用 Wiki」，無法確認「Wiki 忠實反映論文」，所以檢查要放在錯誤產生的地方。
