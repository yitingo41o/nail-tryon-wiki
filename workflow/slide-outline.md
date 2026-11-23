# 簡報大綱（Query 節點的輸出）

> 由 Query 節點產生：先讀 `wiki/index.md`，再讀相關頁，只用 Wiki 內容排出大綱。
> 每張投影片列出它會用到的 Wiki 頁；生成簡報時，這些頁就是該張的 `data-wiki`。
> 讀者設定：不懂電腦視覺的人（客人、同學）。教學結構：問題 → 為什麼難 → 路線一 → 路線二 → 比較 → 應用 → 小測驗 → 回顧。

| # | 標題 | 要教的重點 | 用到的 Wiki 頁 |
|---|---|---|---|
| 1 | 封面 | AI 怎麼讓你在手機上試戴穿戴甲？ | `wiki/index.md` |
| 2 | 今天要回答的問題 | 核心問題 + 3 個學習目標 | `wiki/index.md`、`wiki/discussion.md` |
| 3 | 為什麼試戴很難 | 指甲小、手會動、有弧度、會反光（用作品照說明） | `concepts/curvature-and-lighting.md`、`concepts/nail-segmentation.md` |
| 4 | 兩條路線 | AR 貼圖 vs Diffusion 生成的流程圖 | `concepts/2d-overlay-tryon.md`、`concepts/diffusion-tryon.md` |
| 5 | 路線一 ① 找到手 | 手掌偵測 → 21 個 2.5D 關鍵點；為什麼先找手掌 | `concepts/hand-landmarks.md`、`sources/2020-mediapipe-hands.md` |
| 6 | 路線一 ② 找到指甲 | 三個輸出、類別不平衡、連通元件、94.5 mIoU | `concepts/nail-segmentation.md`、`sources/2019-nail-polish-tryon.md` |
| 7 | 路線一 ③ 貼上去 + 假反光 | 互動示範：平貼 → 轉方向 → 漸層反光 → 拉長遮罩 | `concepts/2d-overlay-tryon.md`、`sources/2019-nail-polish-tryon.md` |
| 8 | 路線二入門：Diffusion | 從雜訊一步步畫出圖；潛在空間省計算 | `concepts/diffusion-inpainting.md`、`sources/2021-latent-diffusion.md` |
| 9 | Inpainting | 只重畫遮住的地方；光影跟著照片；但慢 | `concepts/diffusion-inpainting.md`、`sources/2021-latent-diffusion.md` |
| 10 | ControlNet | 鎖住 + 複製 + 零卷積；法向量圖 = 曲面 | `concepts/conditional-control.md`、`sources/2023-controlnet.md` |
| 11 | IP-Adapter | 作品照當提示；22M；細節不保證 | `concepts/image-prompt.md`、`sources/2023-ip-adapter.md` |
| 12 | 組起來：IDM-VTON | inpainting + IP-Adapter + GarmentNet；細節仍難保留 | `concepts/diffusion-tryon.md`、`sources/2024-idm-vton.md` |
| 13 | 比較表 | 款式、光影、曲面、立體裝飾、速度 | `comparisons/overlay-vs-diffusion.md` |
| 14 | 用我的作品來想（推論） | 平面手繪 / 珍珠光澤 / 立體櫻桃各適合哪條路線 | `concepts/curvature-and-lighting.md`、`comparisons/overlay-vs-diffusion.md` |
| 15 | 混合做法與下一步（推論） | 先貼圖保細節、再生成補光影；Wiki 缺口 | `comparisons/overlay-vs-diffusion.md`、`concepts/curvature-and-lighting.md` |
| 16 | 小測驗 | 3 題，點開看答案 | `concepts/hand-landmarks.md`、`concepts/image-prompt.md`、`concepts/2d-overlay-tryon.md` |
| 17 | 重點回顧與參考資料 | 3 句話總結 + Wiki 連結 | `wiki/index.md` |

Query 時發現 Wiki 不夠的地方（沒有用模型記憶補，而是記下來）：

- Wiki 沒有任何「估計指甲 3D 形狀 / 法向量」的資料 → 簡報第 15 張列為「下一步要 ingest 的資料」，不做技術說明。
- 混合做法沒有任何來源實驗過 → 簡報標示「推論」。
