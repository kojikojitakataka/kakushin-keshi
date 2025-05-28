import streamlit as st
from PIL import Image

st.set_page_config(page_title="賭神 - 競馬AI予想", layout="centered")

st.image("images/logo.png", width=200)

st.title("🐎 賭神 - AI競馬予想サイト")
st.markdown("精度×スピード×華やかさ。回収率100%目指すなら《賭神》。")

# 予想表示（仮の例）
st.subheader("🎯 今日のAI予想（例）")
st.write("◎ 本命：5枠10番\n○ 対抗：7枠13番\n▲ 単穴：1枠2番")

# 実績画像（あれば）
st.subheader("🔥 実績サンプル")
st.image("images/sample_result.png", use_column_width=True)

# フッター
st.markdown("---")
st.caption("© 2025 賭神 - AI競馬予想")
