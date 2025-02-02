import streamlit as st
import time
import numpy as np

def create_timer():
    # サイドバーの設定
    st.sidebar.title("コーヒー抽出メソッド")
    
    method = st.sidebar.selectbox(
        "抽出方法を選択",
        ["4:6メソッド", "スイートスポット", "1分ドリップ"]
    )

    # 出典情報の追加
    st.sidebar.markdown("""
    ### 出典元
    - **4:6メソッド**: [Philocoffea](https://philocoffea.com/?mode=f3)
        - 開発者: Tetsu Kasuya
        - 2016 World Brewers Cup Champion
    - **スイートスポット**: [COFFEE BREWING SCHOOL](https://www.coffeebrewinginstitute.com/)
    - **1分ドリップ**: [TRUNK COFFEE](https://trunk-coffee.com/)
    
    ### バージョン情報
    - Version: 1.0.0
    """)
    
    if method == "4:6メソッド":
        create_46_method_timer()
    elif method == "スイートスポット":
        create_sweetspot_timer()
    elif method == "1分ドリップ":
        create_1min_timer()

def create_46_method_timer():
    st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
    <h1 style='text-align: center; color: #ffffff; background-color: rgba(255, 255, 255, 0.1) ; font-family: "Roboto", sans-serif; font-size: 54px; '>
        4:6メソッド<br>コーヒータイマー
    </h1>
""", unsafe_allow_html=True)
    # CSS for larger display
    st.markdown("""
        <style>
        .big-timer {
            font-size: 180px !important;
            font-weight: bold;
            text-align: center;
            color: #1f77b4;
        }
        .info-text {
            font-size: 24px !important;
            line-height: 1.5;
        }
        .stButton>button {
            font-size: 24px;
            padding: 20px 40px;
        }
        .stMarkdown {
            font-size: 24px;
        }
        .stAlert {
            font-size: 28px;
        }
        div[data-baseweb="select"] {
            font-size: 20px;
        }
        div[data-baseweb="input"] {
            font-size: 20px;
        }
        /* 抽出中の表示を大きく */
        .big-pour-indicator {
        font-size: 36px !important;
        padding: 20px !important;
        line-height: 1.5 !important;
        background-color: rgba(0, 0, 255, 0.3) !important;  /* 青色背景30%透過 */
        }
        .stInfo {
            font-size: 36px !important;
        }
        .big-warning {
            font-size: 42px !important;
            padding: 25px !important;
            line-height: 1.6 !important;
            background-color: rgba(255, 255, 0, 0.3) !important;  /* 黄色背景30%透過 */
        }
        .stWarning {
            font-size: 42px !important;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # 既存のCSSの後に音声再生用のJavaScriptを追加
    st.markdown("""
            <audio id="beep-sound" src="data:audio/wav;base64,UklGRiQAAABXQVZFZm10IBAAAAABAAEARKwAABCxAgAEABAAZGF0YQAAAAA="></audio>
            <script>
            function playBeep() {
                document.getElementById('beep-sound').play();
            }
            </script>
    """, unsafe_allow_html=True)
    
    # 基本設定の修正
    coffee_amount = st.number_input("コーヒー粉量(g)", value=20, step=1, min_value=10, max_value=50)
    
    # コーヒー粉量から総水量を計算（15倍を基準とし、10g単位で四捨五入）
    calculated_water = round((coffee_amount * 15) / 10) * 10
    
    # 計算された総水量を表示（編集不可）
    st.markdown(f"""
        <div class="info-text">
        推奨総水量: {calculated_water}g (お湯 : コーヒー粉= 15 : 1)
        </div><br>
    """, unsafe_allow_html=True)
    
    # 抽出設定の計算
    first_phase = calculated_water * 0.4
    second_phase = calculated_water * 0.6
    pour_amounts = [first_phase/2, first_phase/2, second_phase/3, second_phase/3, second_phase/3]
    times = [0, 45, 90, 135, 165]
    sum_of_elements = 0
    for i in range(4):  # 0 から 3 までのインデックスを指定
        sum_of_elements += pour_amounts[i]  # 各要素を合計に足していく
        sum_pour_amounts[0] =sum_of_elements
    
    if st.button('タイマー開始'):
        info_area = st.empty()
        timer = st.empty()
        pour_indicator = st.empty()
        next_pour_warning = st.empty()
        
        start_time = time.time()
        show_warning = False
        
        while True:
            current_time = time.time() - start_time
            
            if current_time > 210:
                timer.markdown('<p class="big-timer">完了!</p>', unsafe_allow_html=True)
                break
            
            current_stage = 0
            for i, t in enumerate(times):
                if current_time >= t:
                    current_stage = i
            
            info_area.markdown(f"""
            <div class="info-text">
            総抽出量: {calculated_water}g (合計時間: 3分30秒)<br>
            1回目: {pour_amounts[0]:d}g - 0秒開始 {'(実行中)' if current_stage == 0 else '(完了)' if current_stage > 0 else ''}<br>
            2回目: {pour_amounts[1]:d}g 「総量{sum(pour_amounts[:1]):d}g」 - 45秒開始 {'(実行中)' if current_stage == 1 else '(完了)' if current_stage > 1 else ''}<br>
            3回目: {pour_amounts[2]:d}g 「総量{sum(pour_amounts[:2]):d}g」 - 1分30秒開始 {'(実行中)' if current_stage == 2 else '(完了)' if current_stage > 2 else ''}<br>
            4回目: {pour_amounts[3]:d}g 「総量{sum(pour_amounts[:3]):d}g」 - 2分15秒開始 {'(実行中)' if current_stage == 3 else '(完了)' if current_stage > 3 else ''}<br>
            5回目: {pour_amounts[4]:d}g 「総量{sum(pour_amounts[:4]):d}g」 - 2分45秒開始 {'(実行中)' if current_stage == 4 else '(完了)' if current_stage > 4 else ''}
            </div>
            """, unsafe_allow_html=True)
            
            if current_stage < len(times):
                pour_indicator.markdown(f"""
                    <div class="big-pour-indicator stInfo">
                        第{current_stage + 1}回目の抽出中 ({pour_amounts[current_stage]:.1f}g)
                    </div>
                """, unsafe_allow_html=True)
            
            if current_stage < len(times) - 1:
                time_to_next = times[current_stage + 1] - current_time
                if 0 < time_to_next <= 10:
                    show_warning = not show_warning
                    if show_warning:
                        next_time_str = f"{times[current_stage + 1] // 60}分{times[current_stage + 1] % 60}秒"
                        next_pour_warning.markdown(f"""
                            <div class="big-warning stWarning" onload="playBeep()">
                            ⚠️ あと{int(time_to_next)}秒で第{current_stage + 2}回目の抽出 ({pour_amounts[current_stage + 1]:.1f}g) - {next_time_str}開始
                            </div>
                            <script>playBeep();</script>
                        """, unsafe_allow_html=True)
                else:
                    next_pour_warning.empty()
            else:
                next_pour_warning.empty()  #6回目の警告を消す
            
            minutes = int(current_time // 60)
            seconds = int(current_time % 60)
            timer.markdown(f'<p class="big-timer">{minutes:02d}:{seconds:02d}</p>', unsafe_allow_html=True)
            
            time.sleep(0.5)
        
        if current_time > 210:
            timer.markdown('<p class="big-timer">完了!</p>', unsafe_allow_html=True)
            pour_indicator.empty()  # 抽出中の表示を消す
            next_pour_warning.empty()  # 警告表示を消す

        st.success("4:6メソッド完了！美味しいコーヒーをお楽しみください！")

def create_sweetspot_timer():
    st.title("スイートスポット抽出法")
    st.info("開発中 - 近日公開予定")

def create_1min_timer():
    st.title("1分ドリップ")
    st.info("開発中 - 近日公開予定")

if __name__ == "__main__":
    create_timer() 
