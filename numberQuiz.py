import random

try:
    import streamlit as st
except ImportError:  # pragma: no cover
    st = None


def _reset_game():
    st.session_state.answer = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.message = "1에서 100까지 숫자 중 하나를 맞춰보세요!"
    st.session_state.guess_input = 1


def main():
    if st is None:
        raise RuntimeError(
            "streamlit가 설치되어 있지 않습니다. 먼저 `pip install streamlit`로 설치한 후 `streamlit run numberQuiz.py`로 실행하세요."
        )

    st.title("숫자 맞추기 퀴즈")

    if "answer" not in st.session_state:
        _reset_game()

    st.button("새 게임", on_click=_reset_game)

    st.write(st.session_state.message)

    guess = st.number_input(
        "숫자를 입력하세요",
        min_value=1,
        max_value=100,
        step=1,
        value=st.session_state.get("guess_input", 1),
        key="guess_input",
    )

    if st.button("제출"):
        st.session_state.attempts += 1

        if guess < st.session_state.answer:
            st.session_state.message = f"더 큰 숫자입니다. (시도: {st.session_state.attempts})"
        elif guess > st.session_state.answer:
            st.session_state.message = f"더 작은 숫자입니다. (시도: {st.session_state.attempts})"
        else:
            st.success(
                f"정답입니다! 축하합니다! {st.session_state.attempts}번 만에 맞췄습니다."
            )
            st.session_state.message = (
                "게임을 다시 시작하려면 '새 게임' 버튼을 눌러주세요."
            )

    st.write("시도 횟수:", st.session_state.attempts)


if __name__ == "__main__":
    main()
