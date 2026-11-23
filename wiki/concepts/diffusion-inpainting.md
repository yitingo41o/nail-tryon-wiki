# Diffusion 與 Inpainting

> Diffusion 模型從一團雜訊開始，一步一步「去雜訊」畫出圖片。Inpainting 是只重畫照片中被遮住的區域，其他地方保持原樣。

## 重點

- Latent Diffusion 先把圖片壓縮成小的潛在表示，再在潛在空間做 diffusion，比直接在像素上做便宜很多。〔來源：[Latent Diffusion](../sources/2021-latent-diffusion.md) §3.1、§3.2〕
- 壓縮倍率 f = 4 和 f = 8 最適合高品質生成；壓太多細節會不見。〔來源：[Latent Diffusion](../sources/2021-latent-diffusion.md) §4.1〕
- 文字等條件透過 cross-attention 放進模型。〔來源：[Latent Diffusion](../sources/2021-latent-diffusion.md) §3.3〕
- Inpainting 效果：在 Places 資料集上 FID 9.39，比 LaMa 的約 12.0 好；兩兩比較的使用者研究中 68.1% 選 LDM。〔來源：[Latent Diffusion](../sources/2021-latent-diffusion.md) §4.5、Table 7、Table 4〕
- 缺點：逐步取樣比 GAN 慢；需要精細像素準確度時，自編碼器可能是瓶頸。〔來源：[Latent Diffusion](../sources/2021-latent-diffusion.md) §5〕

## 和核心問題的關係

- **光影**：Inpainting 依整張照片的上下文重畫，光線方向、膚色、反光比較容易和原照片一致。這是生成式路線最大的優勢。〔綜合推論〕
- **細節風險**：指甲很小、手繪圖案很細，正好碰到「精細像素準確度」的限制。〔來源：[Latent Diffusion](../sources/2021-latent-diffusion.md) §5〕
- **速度**：多步取樣，不適合手機上即時試戴。〔來源：[Latent Diffusion](../sources/2021-latent-diffusion.md) §5〕

## 來源

- [Latent Diffusion（2021）](../sources/2021-latent-diffusion.md)
