# Latent Diffusion：High-Resolution Image Synthesis with Latent Diffusion Models

| 欄位 | 內容 |
|---|---|
| 作者 | Robin Rombach, Andreas Blattmann, Dominik Lorenz, et al.（LMU Munich、Heidelberg、Runway ML） |
| 年份 / 發表 | arXiv 2021-12（2112.10752），CVPR 2022 |
| 連結 | https://arxiv.org/abs/2112.10752 |
| 讀過的章節 | §1–§5（含 §4.5 inpainting、§5 限制）；附錄未讀 |
| 核對狀態 | 部分核對（附錄未讀） |

## 一句話

Stable Diffusion 的基礎：先把圖片壓縮成小的「潛在表示」，再在這個小空間裡做 diffusion，讓生成高解析度圖片變得便宜很多。

## 在試戴流程中的位置

生成式路線的**地基**。後面的 [ControlNet](2023-controlnet.md)、[IP-Adapter](2023-ip-adapter.md)、[IDM-VTON](2024-idm-vton.md) 都建立在這類模型上。試戴會用到的是它的 **inpainting（只重畫遮住的區域）** 能力。

## 重點

1. **兩階段**：先訓練一個自編碼器（autoencoder），把圖片壓縮成潛在表示 z；再在 z 上訓練 diffusion 模型（UNet 骨幹）。生成時先生出 z，再用解碼器還原成圖片。〔§3.1、§3.2〕
2. **壓縮倍率 f 的取捨**：測了 f = 1～32。f 太小訓練很慢，f 太大細節會被壓掉；f = 4～16 比較平衡，其中 f = 4 和 f = 8 最適合高品質生成。〔§4.1〕
3. **用 cross-attention 加條件**：把文字等條件編碼後，透過 cross-attention 放進 UNet 的中間層，Query 來自圖片特徵、Key/Value 來自條件。〔§3.3〕
4. **省計算**：論文引用像素空間的 diffusion 模型需要 150～1000 V100 天訓練；在 LSUN-Bedrooms 上，LDM 用約一半參數、約 4 倍少的訓練資源。〔§1、§4.2〕
5. **Inpainting**：依 LaMa 的設定在 Places 資料集上訓練和評估。最大的 LDM-4 微調版 FID 9.39，LaMa 約 12.0；遮住 40–50% 的困難情況，LDM 1.50 對 LaMa 2.21。使用者研究中，兩兩比較時 LDM-4 勝出 68.1%。〔§4.5、Table 7、Table 4〕
6. **潛在空間模型比像素空間模型**在 inpainting 上至少快 2.7 倍，FID 至少好 1.6 倍。〔Table 6〕

## 關於曲面與光影

本篇沒有直接討論曲面或光影。但它的機制和核心問題有關：

- Inpainting 是「根據周圍的畫面重畫遮住的地方」，所以光影是**從整張照片的上下文推出來的**，不是用公式算的。
- 論文的限制提到：自編碼器的重建可能成為「需要精細像素準確度」任務的瓶頸〔§5〕。指甲是很小的區域、手繪圖案又很細，這一點對試戴很重要。

## 限制

- 雖然比像素空間 diffusion 快很多，逐步取樣仍然比 GAN 慢。〔§5〕
- 需要精細像素準確度的任務，自編碼器重建可能是瓶頸。〔§5〕

## 待確認

- §4.5 沒有寫明遮罩和被遮住的圖片怎麼輸入模型。§4.3.2 提到 LDM 處理這類任務時，會把空間對齊的條件「接（concatenate）」到去噪模型的輸入；本 Wiki 推測 inpainting 也是這樣，但未在原文 §4.5 核對到。
- 完整實驗設定在附錄 E.2.2，未讀。

## 相關頁面

- 概念：[Diffusion 與 Inpainting](../concepts/diffusion-inpainting.md)、[生成式試戴](../concepts/diffusion-tryon.md)
- 比較：[2D 貼圖 vs Diffusion 生成](../comparisons/overlay-vs-diffusion.md)
