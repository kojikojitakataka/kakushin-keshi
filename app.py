streamlit as st
import pandas as pd
import random
from datetime import datetime

st.set_page_config(page_title="賭神 - 競馬AI予想アプリ", layout="wide")
st.title("🐎 賭神 - 競馬AI予想アプリ")

# 出馬表URLから取得
@st.cache_data

def fetch_race_table(url):
    try:
        df = pd.read_html(url)[0]  # Netkeiba出馬表の1つ目のテーブルを取得
        return df
    except Exception as e:
        st.error("出馬表の取得に失敗しました。URLをご確認ください。")
        return None

# AI予想ロジック（ランダム選出）
def ai_prediction(df):
    df_sample = df.sample(min(4, len(df)))
    df_sample["印"] = ["◎", "○", "▲", "☆"][:len(df_sample)]
    return df_sample

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
    race_url = st.text_input("🔗 出馬表URLを入力（例：https://db.netkeiba.com/race/202305030811）",
                              value="https://db.netkeiba.com/race/202305030811")
with col2:
    race_time = st.time_input("⏰ 発走時刻", value=datetime.now().time())

st.divider()

# 出馬表取得と表示
df_race = fetch_race_table(race_url)
if df_race is not None:
    st.subheader("📋 出走馬情報")
    st.dataframe(df_race, use_container_width=True)

    df_pred = ai_prediction(df_race)
    st.subheader("🧠 AI予想（買い目）")
    st.dataframe(df_pred[["印"] + df_pred.columns.tolist()[:-1]], use_container_width=True)

    # 投票ボタン（リンク例）
    st.markdown("""
    ### 🎯 投票はこちらから
    [▶ JRA 投票ページへ](https://www.ipat.jra.go.jp/) 
    """)

    st.info("🔔 AI予想をLINE通知しました！（※ダミー表示）")

    # ユーザー統計
    st.subheader("📈 ユーザー成績（ダミー）")
    stats = get_user_stats()
    col_a, col_b, col_c, col_d = st.columns(4)
    col_a.metric("的中率", stats["的中率"])
    col_b.metric("回収率", stats["回収率"])
    col_c.metric("累計投資", stats["累計投資"])
    col_d.metric("累計払戻", stats["累計払戻"])

# フッター
st.caption(f"© 賭神 - AI競馬予想 ({datetime.now().strftime('%Y/%m/%d')})")
