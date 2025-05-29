import streamlit as st
import pandas as pd
import random
from datetime import datetime

st.set_page_config(page_title="賭神 - 競馬AI予想アプリ", layout="wide")
st.title("🐎 賭神 - 競馬AI予想アプリ")

# ダミーの出走馬データ
def get_race_data():
    horses = [f"馬{i}" for i in range(1, 9)]
    odds = [round(random.uniform(1.5, 20.0), 1) for _ in horses]
    popularity = list(range(1, len(horses) + 1))
    random.shuffle(popularity)
    return pd.DataFrame({
        "馬名": horses,
        "オッズ": odds,
        "人気順": popularity,
        "枠番": [i for i in range(1, len(horses)+1)],
        "馬番": random.sample(range(1, 18), len(horses))
    }).sort_values("人気順")

# AI予想ロジック（ランダムダミー）
def ai_prediction(df):
    prediction = df.sample(4)
    prediction["印"] = ["◎", "○", "▲", "☆"]
    return prediction.sort_values("人気順")

# 回収率・的中率用ダミーデータ
def get_user_stats():
    return {
        "的中率": f"{random.randint(20, 80)}%",
        "回収率": f"{random.randint(70, 150)}%",
        "累計投資": f"{random.randint(10000, 50000)}円",
        "累計払戻": f"{random.randint(8000, 60000)}円"
    }

# 入力
col1, col2 = st.columns([2,1])
with col1:
    race_name = st.text_input("🔍 レース名を入力（例：東京11R）", value="東京11R")
with col2:
    race_time = st.time_input("⏰ 発走時刻", value=datetime.now().time())

st.divider()

# データ取得・表示
df_race = get_race_data()
df_pred = ai_prediction(df_race)

st.subheader(f"📋 {race_name} - 出走馬情報（人気順）")
st.dataframe(df_race.reset_index(drop=True), use_container_width=True)

st.subheader("🧠 AI予想（買い目）")
st.dataframe(df_pred[["印", "馬名", "人気順", "オッズ"]].reset_index(drop=True), use_container_width=True)

# 投票ボタン（リンク例）
st.markdown("""
### 🎯 投票はこちらから
[▶ JRA 投票ページへ](https://www.ipat.jra.go.jp/) 
""")

# LINE通知風（表示だけ）
st.info(f"🔔 {race_name} の予想をLINE通知しました！（※ダミー表示）")

# ユーザー統計
st.subheader("📈 ユーザー成績（ダミー）")
stats = get_user_stats()
col_a, col_b, col_c, col_d = st.columns(4)
col_a.metric("的中率", stats["的中率"])
col_b.metric("回収率", stats["回収率"])
col_c.metric("累計投資", stats["累計投資"])
col_d.metric("累計払戻", stats["累計払戻"])

# フッター
today = datetime.now().strftime("%Y/%m/%d")
st.caption(f"© 賭神 - AI競馬予想 ({today})")
