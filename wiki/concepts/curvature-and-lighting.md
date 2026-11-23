# 指甲曲面與光影（Nail Curvature & Lighting）

> 指甲不是平的：它有弧度，表面（尤其是凝膠）會反光。試戴看起來假不假，很大程度取決於這兩件事。

## 重點

- AR 路線用**漸層模擬鏡面反光**，依指甲方向擺放；沒有物理光照模型，也沒有 3D 指甲形狀。〔來源：[Nail Polish Try-On](../sources/2019-nail-polish-tryon.md) §3.4〕
- 手部關鍵點只有相對深度（2.5D），能知道手指方向，不能知道指甲表面的弧度。〔來源：[MediaPipe Hands](../sources/2020-mediapipe-hands.md) §2.2〕
- 生成式路線可以用法向量圖、深度圖當條件，控制生成結果的表面方向。〔來源：[ControlNet](../sources/2023-controlnet.md) §4〕
- 生成式路線的光影由 inpainting 依上下文生成，不需要手動設計反光。〔來源：[Latent Diffusion](../sources/2021-latent-diffusion.md) §4.5〕

## 和核心問題的關係

這頁就是核心問題本身。整理成一句話：

- **2D 貼圖**：款式 100% 是你的，但曲面和光影是「假」的（用規則畫出來）。
- **Diffusion 生成**：曲面和光影比較「真」（模型學來的），但款式可能被改掉。〔綜合推論〕

從作品照片可以看到為什麼這很重要：凝膠表面有明顯的條狀高光；櫻桃、珍珠、水鑽是**立體**的。立體裝飾的側面和陰影，2D 貼圖幾乎做不到。〔綜合推論〕

Wiki 目前的缺口：6 篇資料都沒有「估計指甲表面法向量 / 3D 形狀」的方法，下一輪 ingest 要補。

## 來源

- [Nail Polish Try-On（2019）](../sources/2019-nail-polish-tryon.md)
- [MediaPipe Hands（2020）](../sources/2020-mediapipe-hands.md)
- [ControlNet（2023）](../sources/2023-controlnet.md)
- [Latent Diffusion（2021）](../sources/2021-latent-diffusion.md)
