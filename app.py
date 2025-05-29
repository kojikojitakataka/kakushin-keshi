import streamlit as st
import pandas as pd

# --- ページ設定 ---
st.set_page_config(
    page_title="賭神 - 競馬AI予想",
    page_icon="🐎",
    layout="centered",
)

# --- タイトル表示 ---
st.markdown("### 🏆 AI競馬予想 - 賭神")

# --- ロゴの代わりにテキスト表示（画像なし対応） ---
st.markdown("#### 📌 ロゴ画像が見つかりませんでした（images/logo.png）")

st.markdown("---")

# --- サンプル予想表示 ---
st.subheader("🎯 今回のAI予想")
st.markdown("""
**東京11R 安田記念(G1)**  
- ◎ 4番 ソウルラッシュ  
- ○ 11番 セリフォス  
- ▲ 6番 ナミュール  
- ☆ 8番 ドウデュース  
""")

st.markdown("---")

# --- 実績例（ダミー） ---
st.subheader("📊 的中実績（例）")
data = {
    "日付": ["5/25", "5/26", "5/27"],
    "レース": ["京都11R", "東京10R", "中京9R"],
    "買い目": ["3連単 1-5-9", "馬連 2-8", "単勝 7"],
    "結果": ["的中", "不的中", "的中"],
    "回収率": [280, 0, 190],
}
df = pd.DataFrame(data)
st.dataframe(df)

st.markdown("---")

# --- シェア案内 ---
st.info("🔗 このページを友達にシェアしよう！URLをコピーして送るだけ。")
