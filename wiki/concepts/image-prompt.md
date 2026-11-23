# 圖片提示（Image Prompt）

> 不用文字描述，直接給模型一張參考圖，叫它照著這張圖的內容和風格來畫。

## 重點

- IP-Adapter 用 CLIP 圖片編碼器讀參考圖，再透過另外加的一組 cross-attention 放進模型，和文字提示並存。〔來源：[IP-Adapter](../sources/2023-ip-adapter.md) §3.2.1、§3.2.2〕
- 可訓練參數只有約 22M，可以和 ControlNet 一起用。〔來源：[IP-Adapter](../sources/2023-ip-adapter.md) Table 1、§4.3.2〕
- 強度 λ 可以調：0 = 不看圖，1 = 完全看圖。〔來源：[IP-Adapter](../sources/2023-ip-adapter.md) §3.2.3〕
- **限制**：能抓到內容和風格，但無法穩定保留細節。〔來源：[IP-Adapter](../sources/2023-ip-adapter.md) §5〕
- IDM-VTON 為了補這個缺點，另外加了 GarmentNet 專門保留衣服細節。〔來源：[IDM-VTON](../sources/2024-idm-vton.md) Abstract〕

## 和核心問題的關係

- 穿戴甲款式很難用文字描述，圖片提示是生成式路線輸入款式的自然方式。
- 但手工穿戴甲的價值在細節（手繪蝴蝶結的線條、櫻桃的位置）。只用 IP-Adapter，生成的可能是「風格很像、細節不同」的指甲。〔綜合推論〕

## 來源

- [IP-Adapter（2023）](../sources/2023-ip-adapter.md)
- [IDM-VTON（2024）](../sources/2024-idm-vton.md)
