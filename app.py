import streamlit as st
from generator import generate_test
from checker import check_answer

st.set_page_config(page_title="ИИ-Ассистент по производным", page_icon="🧮")
st.title("🧮 ИИ-Ассистент по производным")
st.write("Нажмите кнопку ниже, чтобы сгенерировать задачу, и введите ваш ответ.")

if "task_data" not in st.session_state:
    st.session_state.task_data = None

if st.button("Сгенерировать задачу"):
    with st.spinner("Нейросеть GigaChat придумывает задачу..."):
        st.session_state.task_data = generate_test(topic="Производные", difficulty="Средняя")

if st.session_state.task_data:
    task = st.session_state.task_data
    st.info(f"**Условие задачи:**\n\n{task['task']}")

    user_answer = st.text_input("Введите ваш ответ (например: 3*x**2):")

    if st.button("Проверить ответ"):
        if not user_answer:
            st.warning("Пожалуйста, введите ответ!")
        else:
            is_correct = check_answer(user_answer, task["correct_answer"])
            if is_correct:
                st.success("✅ ВЕРНО! Отличная работа.")
            else:
                st.error(f"❌ ОШИБКА. Правильный ответ: {task['correct_answer']}")