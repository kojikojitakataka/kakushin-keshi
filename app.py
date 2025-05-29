import streamlit as st

# ページ設定
st.set_page_config(page_title="賭神 - 競馬AI予想", page_icon="🐎", layout="centered")

# タイトル
st.title("🏇 賭神 - AI競馬予想")

# 本日の予想
st.subheader("🎯 今日の本命レース")
st.markdown("""
### 東京11R 安田記念(G1)

- ◎ 本命：4番 ソウルラッシュ  
- ○ 対抗：11番 セリフォス  
- ▲ 単穴：6番 ナミュール  
- ☆ 穴馬：8番 ドウデュース  
""")
