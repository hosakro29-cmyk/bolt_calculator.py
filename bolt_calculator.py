import streamlit as st


# ==================================================
# 미터 보통 나사 데이터
# ==================================================
THREAD_DATA = {
    "M3":  {"pitch": 0.50, "effective_diameter": 2.675},
    "M4":  {"pitch": 0.70, "effective_diameter": 3.545},
    "M5":  {"pitch": 0.80, "effective_diameter": 4.480},
    "M6":  {"pitch": 1.00, "effective_diameter": 5.350},
    "M8":  {"pitch": 1.25, "effective_diameter": 7.188},
    "M10": {"pitch": 1.50, "effective_diameter": 9.026},
    "M12": {"pitch": 1.75, "effective_diameter": 10.863},
    "M14": {"pitch": 2.00, "effective_diameter": 12.701},
    "M16": {"pitch": 2.00, "effective_diameter": 14.701},
    "M18": {"pitch": 2.50, "effective_diameter": 16.376},
    "M20": {"pitch": 2.50, "effective_diameter": 18.376},
    "M22": {"pitch": 2.50, "effective_diameter": 20.376},
    "M24": {"pitch": 3.00, "effective_diameter": 22.051},
    "M27": {"pitch": 3.00, "effective_diameter": 25.051},
    "M30": {"pitch": 3.50, "effective_diameter": 27.727},
}


# ==================================================
# 볼트 등급별 체결 데이터
#
# 단위:
# minimum_force : kN
# normal_torque : N·m
#
# 아래 수치는 예시입니다.
# 실제 사용 전 S-1651-D 기준서의 값으로 교체하십시오.
# ==================================================
FASTENER_DATA = {
    "4.6": {
        "M3":  {"minimum_force": 0.60, "normal_torque": 0.90},
        "M4":  {"minimum_force": 1.10, "normal_torque": 1.80},
        "M5":  {"minimum_force": 1.80, "normal_torque": 3.30},
        "M6":  {"minimum_force": 2.50, "normal_torque": 5.40},
        "M8":  {"minimum_force": 4.50, "normal_torque": 13.00},
        "M10": {"minimum_force": 7.20, "normal_torque": 26.00},
        "M12": {"minimum_force": 10.50, "normal_torque": 46.00},
        "M14": {"minimum_force": 14.40, "normal_torque": 74.00},
        "M16": {"minimum_force": 19.20, "normal_torque": 114.00},
        "M18": {"minimum_force": 23.40, "normal_torque": 162.00},
        "M20": {"minimum_force": 30.00, "normal_torque": 228.00},
        "M22": {"minimum_force": 37.20, "normal_torque": 306.00},
        "M24": {"minimum_force": 43.20, "normal_torque": 390.00},
        "M27": {"minimum_force": 56.40, "normal_torque": 576.00},
        "M30": {"minimum_force": 69.00, "normal_torque": 780.00},
    },

    "8.8": {
        "M3":  {"minimum_force": 1.00, "normal_torque": 1.50},
        "M4":  {"minimum_force": 1.80, "normal_torque": 3.00},
        "M5":  {"minimum_force": 2.90, "normal_torque": 5.50},
        "M6":  {"minimum_force": 4.10, "normal_torque": 9.00},
        "M8":  {"minimum_force": 7.50, "normal_torque": 22.00},
        "M10": {"minimum_force": 12.00, "normal_torque": 44.00},
        "M12": {"minimum_force": 17.50, "normal_torque": 77.00},
        "M14": {"minimum_force": 24.00, "normal_torque": 123.00},
        "M16": {"minimum_force": 32.00, "normal_torque": 190.00},
        "M18": {"minimum_force": 39.00, "normal_torque": 270.00},
        "M20": {"minimum_force": 50.00, "normal_torque": 380.00},
        "M22": {"minimum_force": 62.00, "normal_torque": 510.00},
        "M24": {"minimum_force": 72.00, "normal_torque": 650.00},
        "M27": {"minimum_force": 94.00, "normal_torque": 960.00},
        "M30": {"minimum_force": 115.00, "normal_torque": 1300.00},
    },

    "10.9": {
        "M3":  {"minimum_force": 1.30, "normal_torque": 2.00},
        "M4":  {"minimum_force": 2.40, "normal_torque": 4.50},
        "M5":  {"minimum_force": 3.80, "normal_torque": 8.00},
        "M6":  {"minimum_force": 5.80, "normal_torque": 13.00},
        "M8":  {"minimum_force": 10.50, "normal_torque": 32.00},
        "M10": {"minimum_force": 17.00, "normal_torque": 63.00},
        "M12": {"minimum_force": 24.00, "normal_torque": 110.00},
        "M14": {"minimum_force": 33.00, "normal_torque": 175.00},
        "M16": {"minimum_force": 44.00, "normal_torque": 270.00},
        "M18": {"minimum_force": 54.00, "normal_torque": 385.00},
        "M20": {"minimum_force": 69.00, "normal_torque": 540.00},
        "M22": {"minimum_force": 85.00, "normal_torque": 720.00},
        "M24": {"minimum_force": 99.00, "normal_torque": 920.00},
        "M27": {"minimum_force": 129.00, "normal_torque": 1350.00},
        "M30": {"minimum_force": 158.00, "normal_torque": 1850.00},
    },

    "12.9": {
        "M3":  {"minimum_force": 1.60, "normal_torque": 2.50},
        "M4":  {"minimum_force": 2.90, "normal_torque": 5.50},
        "M5":  {"minimum_force": 4.60, "normal_torque": 10.00},
        "M6":  {"minimum_force": 6.90, "normal_torque": 16.00},
        "M8":  {"minimum_force": 12.50, "normal_torque": 38.00},
        "M10": {"minimum_force": 20.00, "normal_torque": 75.00},
        "M12": {"minimum_force": 29.00, "normal_torque": 130.00},
        "M14": {"minimum_force": 39.00, "normal_torque": 205.00},
        "M16": {"minimum_force": 52.00, "normal_torque": 315.00},
        "M18": {"minimum_force": 64.00, "normal_torque": 450.00},
        "M20": {"minimum_force": 82.00, "normal_torque": 630.00},
        "M22": {"minimum_force": 101.00, "normal_torque": 840.00},
        "M24": {"minimum_force": 118.00, "normal_torque": 1080.00},
        "M27": {"minimum_force": 154.00, "normal_torque": 1570.00},
        "M30": {"minimum_force": 189.00, "normal_torque": 2150.00},
    },
}


# ==================================================
# 페이지 설정
# ==================================================
st.set_page_config(
    page_title="볼트 체결력 계산기",
    page_icon="🔩",
    layout="centered",
)


# ==================================================
# 제목
# ==================================================
st.title("볼트 체결력 및 체결토크 계산기")

st.info(
    "볼트 크기, 등급, 수량을 입력하면 체결력과 체결토크를 계산합니다."
)


# ==================================================
# 입력 영역
# ==================================================
col1, col2 = st.columns(2)

with col1:
    bolt_size = st.selectbox(
        "볼트 크기",
        options=list(THREAD_DATA.keys()),
        index=list(THREAD_DATA.keys()).index("M8"),
    )

with col2:
    bolt_grade = st.selectbox(
        "볼트 등급",
        options=["4.6", "8.8", "10.9", "12.9"],
        index=2,
    )

bolt_count = st.number_input(
    "볼트 수",
    min_value=1,
    value=1,
    step=1,
)


# ==================================================
# 계산
# ==================================================
thread_info = THREAD_DATA[bolt_size]
fastener_info = FASTENER_DATA[bolt_grade][bolt_size]

single_minimum_force = fastener_info["minimum_force"]
single_normal_torque = fastener_info["normal_torque"]

total_minimum_force = single_minimum_force * bolt_count
total_normal_torque = single_normal_torque * bolt_count


# ==================================================
# 결과 출력
# ==================================================
st.subheader("계산 결과")

result_col1, result_col2 = st.columns(2)

with result_col1:
    st.metric(
        "볼트 유효경",
        f'{thread_info["effective_diameter"]:.3f} mm',
    )

    st.metric(
        "피치",
        f'{thread_info["pitch"]:.2f} mm',
    )

    st.metric(
        "낱개 최소체결력",
        f"{single_minimum_force:.2f} kN",
    )
    st.metric(
        "낱개 일반체결토크",
        f"{single_normal_torque:.2f} N·m",
    )
    

with result_col2:
    
    st.metric(
        "전체 최소체결력",
        f"{total_minimum_force:.2f} kN",
    )
    st.metric(
        "전체 일반체결토크",
        f"{total_normal_torque:.2f} N·m",
    )

    st.metric(
        "볼트 등급",
        bolt_grade,
    )

    st.metric(
        "볼트 수",
        f"{bolt_count}개",
    )


# ==================================================
# 계산식 표시
# ==================================================
st.subheader("계산식")

st.write(
    f"전체 최소체결력 = "
    f"{single_minimum_force:.2f} kN × {bolt_count}개 "
    f"= {total_minimum_force:.2f} kN"
)

st.write(
    f"전체 일반체결토크 = "
    f"{single_normal_torque:.2f} N·m × {bolt_count}개 "
    f"= {total_normal_torque:.2f} N·m"
)


# ==================================================
# 주의사항
# ==================================================
st.warning(
    "현재 코드의 체결력과 토크 값은 예시값입니다. "
    "실제 설계 및 제조에 사용하기 전에 S-1651-D 기준서의 "
    "정확한 표 값으로 교체하십시오."
)
