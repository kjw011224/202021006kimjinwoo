import numpy as np
from scipy import signal
import streamlit as st

def plot_step_response(T):
    # 시간 범위 설정
    t = np.linspace(0, 10, 1000)

    # 단위 계단 함수 생성
    u = np.ones_like(t)

    # 시스템 응답 구하기
    _, y = signal.step(T, T=t, X0=0)

    # 응답 곡선 그리기
    st.line_chart(y)

def plot_bode_plot(T):
    # 주파수 응답 (보드선도) 구하기
    w, mag, phase = signal.bode(T)

    # 주파수 응답 (보드선도) 그리기
    fig, axs = st.subplots(2, 1)
    axs[0].semilogx(w, mag)
    axs[0].set(xlabel='Frequency [rad/s]', ylabel='Magnitude [dB]', title='Bode Plot')
    axs[1].semilogx(w, phase)
    axs[1].set(xlabel='Frequency [rad/s]', ylabel='Phase [degrees]')
    st.pyplot(fig)

def main():
    st.title('Control System Analysis')

    # 전달함수 G(s)의 분자와 분모의 계수
    numerator = [100]
    denominator = [1, 5, 6]

    # 전달함수 H(s)의 분자와 분모의 계수
    numerator_feedback = [1]
    denominator_feedback = [1]

    # 폐루프 전달함수 T(s) 구하기
    numerator_loop = np.convolve(numerator, denominator_feedback)
    denominator_loop = np.convolve(denominator, denominator_feedback)

    # 전달함수 T(s) 생성
    T = signal.TransferFunction(numerator_loop, denominator_loop)

    # 스트림릿 애플리케이션에 그래프 출력
    st.pyplot(fig1)
    st.pyplot(fig2)

if __name__ == '__main__':
    main()
