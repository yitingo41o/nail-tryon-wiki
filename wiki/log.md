# 操作紀錄（log）

> 只能往後追加。格式：`## [日期 #序號] 操作 | 對象`。
> 討論在 21:11–21:55（台灣時間）；之後的 ingest → lint → 簡報都在 21:55 之後的同一段工作中依序完成，所以用序號記順序，不寫精確時間。
> 這份紀錄也是作業要求的「實際執行與檢查紀錄」，問題與修正都照實記下。

## [2026-11-23 #1] discuss | 選主題、定範圍

- 三輪討論，詳見 [discussion.md](discussion.md)。
- 產出：核心問題（2D 貼圖 vs diffusion，曲面與光影）、6 篇資料清單、範圍以指甲為主。

## [2026-11-23 #2] ingest | 6 篇資料（批次）

依序抓取 → 寫 source 頁 → 更新 concept 頁 → 名詞表 → index。抓取階段遇到的問題：

| # | 問題 | 怎麼發現 | 處理 |
|---|---|---|---|
| 1 | 6 個 arXiv 摘要頁裡有 4 個直接抓取被工具拒絕（不在允許清單） | 抓取工具回傳錯誤 | 改成先搜尋、再抓 ar5iv 的 HTML 版全文，結果反而讀得更完整 |
| 2 | Latent Diffusion 全文有 40 萬字元，第一次只讀到前 10 萬：**inpainting（§4.5）和限制（§5）都沒讀到** | 抓取結果自己註明「Gaps」 | 用 offset 再讀第 10～20 萬字元，補上 §4.5 和 §5 |
| 3 | 我給抓取工具的問題裡寫了「例如 Lovász loss」，但 ModiFace 論文**根本沒提到 Lovász** | 抓取結果回答「論文沒有提到」 | 沒寫進 Wiki。教訓：抓取時不要在問題裡預設答案，否則可能被「附和」 |
| 4 | MediaPipe 用語不一致：論文寫 2.5D，Google 部落格寫 3D keypoints | 兩個來源對照 | 依論文寫 2.5D，差異記在該頁「待確認」 |
| 5 | IDM-VTON 的 arXiv 頁沒有寫會議 | 抓取結果寫「Venue not stated」 | 改用官方 GitHub README（ECCV 2024），並註明出處 |
| 6 | LDM inpainting 的輸入方式 §4.5 沒寫 | 讀 §4.5 時發現 | 依 §4.3.2 推測為串接（concatenate），標〔待確認〕 |

## [2026-11-23 #3] lint #1 | `check_wiki.py` 第一次執行

結果：**7 個錯誤**

- 3 個壞連結 → 都指向 `log.md`（這份檔案當時還沒建立）。
- 4 個「出處不精確」→ 全部在 IDM-VTON 頁，出處寫成〔方法〕〔實驗表格〕，不是章節號。原因：第一次只讀了摘要頁的整理。

處理：

- 重新抓 IDM-VTON 全文 HTML，補上 §3.2、§4.1、§4.2、§5、Table 1。
- **重抓時發現一個錯誤**：第一次的摘要整理說 IDM-VTON「在 VITON-HD **和 DressCode** 上 FID、CLIP-I 都最好」，但正文 Table 1 只有 VITON-HD，DressCode 的數字在附錄表格，沒讀到。→ 刪掉 DressCode 的說法，只保留 Table 1 的 VITON-HD 數字（FID 6.29 vs 6.43、SSIM 0.870 vs 0.898）。
- 同時確認「刺青、痣」的限制確實在 §5。

## [2026-11-23 #4] 修改檢查流程 | `check_wiki.py`

lint #1 也暴露了**檢查腳本本身的漏洞**：

1. 「待確認」只數行內標記，漏掉「## 待確認」段落底下的條目 → 修正後從 3 處變成 8 處。
2. concept 頁只檢查「有沒有連到 source」，沒檢查出處精不精確 → `diffusion-tryon.md` 引用 IDM-VTON 時寫〔方法〕〔限制段落〕卻通過了。修正後 concept / comparison 頁引用 source 時也必須有 § / Table / Fig. / Abstract。

## [2026-11-23 #5] 處理待確認 | ControlNet 會議

- 用 CVF Open Access 頁面核對 ControlNet 發表於 ICCV 2023 → 移除〔待確認〕。
- 剩下 6 處待確認（腳本另外誤把 log.md 裡的文字算進去，已排除 log.md），都是「資料沒寫 / 沒讀到」的情況，保留標記，不猜。

## [2026-11-23 #6] lint #2 | 人工檢查 + 再加一項自動檢查

- 腳本通過後，人工逐條比對 concept 頁和 source 頁，找到 1 個腳本抓不到的問題：`2d-overlay-tryon.md` 寫「網頁版用 TensorFlow.js」，但 ModiFace 的 source 頁裡沒有這句（是我從搜尋結果記得的）。→ 回原文 §1 核對，補進 source 頁。
- 這類「概念頁說了、來源頁沒說」的問題，至少數字可以自動抓 → `check_wiki.py` 新增第 7 項：concept / comparison 頁裡的數字必須出現在它引用的 source 頁。
- 測試：故意把 94.5 改成 95.4，腳本正確報錯；改回後全部通過。
- 狀態：19 頁、6 處待確認、全部通過。→ Wiki 可以拿來產生簡報。

## [2026-11-23 #7] query | 產生簡報大綱

- 只讀 `index.md` 和相關頁，排出 17 張投影片的大綱，每張列出用到的 Wiki 頁 → [workflow/slide-outline.md](../workflow/slide-outline.md)。
- Query 時發現 Wiki 的缺口：沒有任何「估計指甲 3D 形狀 / 法向量」的資料；混合做法沒有來源實驗過。→ 沒有用模型記憶補，簡報上標「推論」並列為下一步。

## [2026-11-23 #8] generate + check | 簡報 `slides/index.html`

| 檢查 | 結果 | 處理 |
|---|---|---|
| `check_slides.py`（data-wiki、數字可追溯、大綱一致、圖片 alt） | 第一次就全部通過 | 故意把 68.1% 改成 86.1%，腳本正確報錯 → 確認腳本真的有在抓 |
| 瀏覽器實際渲染（Playwright 截圖 17 張 + 量內容是否超出頁尾） | 1 個問題：第 9 張 inpainting 示意的**遮罩沒對準指甲**（蓋在兩片指甲中間） | 圖片被 `object-fit: cover` 裁切，百分比座標失準 → 改成固定 3:4 比例不裁切，用格線量出第 2 片指甲的位置重放遮罩；圖片太高壓到頁尾 → 縮小寬度 |
| 初學者可讀性（人工逐張讀，找「沒解釋就用」的術語） | 4 個：cross-attention、self-attention、UNet、SDXL | 第 11、12 張補上白話解釋（小辭典） |
| 頁碼重複 | 頁尾和導覽列都顯示頁碼，全螢幕時重疊 | 移除頁尾的頁碼 |

- 狀態：Wiki 19 頁全部通過、簡報 17 張全部通過。
