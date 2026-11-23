# 生成式試戴（Diffusion-based Try-On）

> 把手上的指甲遮住，請 diffusion 模型依照款式圖和手的形狀，把指甲「重畫」出來。

## 重點

- 基礎是 [Diffusion 與 Inpainting](diffusion-inpainting.md)：只重畫被遮住的區域。〔來源：[Latent Diffusion](../sources/2021-latent-diffusion.md) §4.5〕
- 形狀用 [條件控制](conditional-control.md)（例如深度、法向量、姿勢圖）。〔來源：[ControlNet](../sources/2023-controlnet.md) §4〕
- 款式用 [圖片提示](image-prompt.md)（IP-Adapter）。〔來源：[IP-Adapter](../sources/2023-ip-adapter.md) §3.2〕
- 完整系統的例子：IDM-VTON 用 SDXL inpainting + IP-Adapter（高階語意）+ GarmentNet（低階細節）做服裝試穿。〔來源：[IDM-VTON](../sources/2024-idm-vton.md) Abstract〕
- 需要的輸入比 2D 貼圖多：遮罩、姿勢圖、款式圖。〔來源：[IDM-VTON](../sources/2024-idm-vton.md) §3.2〕

## 和核心問題的關係

- **光影**：由模型依照片上下文生成，有機會比漸層假反光自然。〔綜合推論〕
- **曲面**：可以透過 ControlNet 的深度 / 法向量條件控制。〔綜合推論〕
- **風險**：細節可能被改掉（IP-Adapter 的限制〔來源：[IP-Adapter](../sources/2023-ip-adapter.md) §5〕；IDM-VTON 也提到遮罩區域內的細節很難保留〔來源：[IDM-VTON](../sources/2024-idm-vton.md) §5〕）。
- **速度**：多步取樣，比 AR 貼圖慢很多，不適合即時影片。〔來源：[Latent Diffusion](../sources/2021-latent-diffusion.md) §5〕

## 來源

- [Latent Diffusion（2021）](../sources/2021-latent-diffusion.md)
- [ControlNet（2023）](../sources/2023-controlnet.md)
- [IP-Adapter（2023）](../sources/2023-ip-adapter.md)
- [IDM-VTON（2024）](../sources/2024-idm-vton.md)
