import streamlit as st
import pandas as pd

# ロゴ表示（images/logo.png が必要です）
st.image("images/logo.png", width=200)

st.title("賭神｜競馬・競艇AI予想アプリ")

# アップロードエリア
uploaded_file = st.file_uploader("CSVファイルをアップロードしてください", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("アップロードされたデータ：")
    st.dataframe(df)

# ダミー予想表示
st.subheader("🔮 AI予想（仮）")
sample_predictions = pd.DataFrame({
    "レース": ["京都11R", "中山10R", "福島9R"],
    "買い目": ["3連単 1-2-3", "馬連 4-6", "ワイド 2-5"],
    "的中率": ["78%", "66%", "59%"]
})
st.table(sample_predictions)
