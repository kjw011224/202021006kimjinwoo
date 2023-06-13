import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import streamlit as st

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

    # 시간 범위 설정
    t = np.linspace(0, 10, 1000)

    # 단위 계단 함수 생성
    u = np.ones_like(t)

    # 시스템 응답 구하기
    t, y = signal.step(T, T=t, X0=0)

    # 응답 곡선 그리기
    fig1, ax1 = plt.subplots()
    ax1.plot(t, y)
    ax1.set(xlabel='Time', ylabel='Output', title='Step Response')
    ax1.grid(True)

    # 주파수 응답 (보드선도) 그리기
    w, mag, phase = signal.bode(T)
    fig2, (ax2, ax3) = plt.subplots(2, 1)
    ax2.semilogx(w, mag)
    ax2.set(xlabel='Frequency [rad/s]', ylabel='Magnitude [dB]', title='Bode Plot')
    ax2.grid(True)
    ax3.semilogx(w, phase)
    ax3.set(xlabel='Frequency [rad/s]', ylabel='Phase [degrees]')
    ax3.grid(True)

    # 스트림릿 애플리케이션에 그래프 출력
    st.pyplot(fig1)
    st.pyplot(fig2)

if __name__ == '__main__':
    main()
    st.write('202021006김진우')
