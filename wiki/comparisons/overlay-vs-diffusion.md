# 2D 貼圖 vs Diffusion 生成（Overlay vs Diffusion Try-On）

> 這頁是 Wiki 用來回答核心問題的比較頁，也是簡報「比較表」那張投影片的來源。

## 重點

| 面向 | 2D 貼圖（AR 路線） | Diffusion 生成（生成式路線） |
|---|---|---|
| 款式還原 | 圖案直接貼上，不會被改〔綜合推論〕 | 可能「風格像、細節不同」：IP-Adapter 無法穩定保留細節（[IP-Adapter](../sources/2023-ip-adapter.md) §5） |
| 光影 | 用漸層模擬鏡面反光（[Nail Polish Try-On](../sources/2019-nail-polish-tryon.md) §3.4） | 依照片上下文重畫（[Latent Diffusion](../sources/2021-latent-diffusion.md) §4.5） |
| 曲面 | 只有平面遮罩 + 方向（[Nail Polish Try-On](../sources/2019-nail-polish-tryon.md) §3.4） | 可用深度 / 法向量圖當條件（[ControlNet](../sources/2023-controlnet.md) §4） |
| 立體裝飾 | 只能當平面圖〔綜合推論〕 | 有機會畫出陰影和側面，但形狀不保證正確〔綜合推論〕 |
| 速度 | 即時：iPad Pro 每幀 29.8 ms（[Nail Polish Try-On](../sources/2019-nail-polish-tryon.md) Abstract） | 多步取樣，慢（[Latent Diffusion](../sources/2021-latent-diffusion.md) §5） |
| 需要的東西 | 指甲分割資料集（ModiFace 自己標了 1,438 張）（[Nail Polish Try-On](../sources/2019-nail-polish-tryon.md) §3.1） | 預訓練大模型 + 遮罩、姿勢等條件（[IDM-VTON](../sources/2024-idm-vton.md) §3.2） |
| 適合的情境 | 手機鏡頭即時試戴、影片 | 一張照片的「高品質預覽圖」、商品宣傳圖〔綜合推論〕 |

## 和核心問題的關係

〔綜合推論〕兩條路線不是二選一，可以**混合**：

1. 先用 2D 貼圖把**你自己的款式**準確放到指甲上（保證細節是對的）。
2. 再用低強度的 diffusion（或只在邊緣與反光區域 inpainting）補上光影和曲面感。

這個混合做法**沒有任何一篇 Wiki 資料直接實驗過**，是根據各篇的優缺點推出來的假設，適合當期末專案的實驗題目。

## 來源

- [Nail Polish Try-On（2019）](../sources/2019-nail-polish-tryon.md)
- [Latent Diffusion（2021）](../sources/2021-latent-diffusion.md)
- [ControlNet（2023）](../sources/2023-controlnet.md)
- [IP-Adapter（2023）](../sources/2023-ip-adapter.md)
- [IDM-VTON（2024）](../sources/2024-idm-vton.md)
