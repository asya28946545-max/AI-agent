import json
from gigachat import GigaChat
import streamlit as st

try:
    AUTH_KEY = st.secrets["AUTH_KEY"]
except:
    AUTH_KEY = "Не покажу"

AUTH_KEY = "Не покажу"

def generate_test(topic: str, difficulty: str):
    giga = GigaChat(
        credentials = AUTH_KEY,
        verify_ssl_certs = False,
        model = "GigaChat-2"
    )

    prompt = f"""
    Ты — опытный преподаватель математического анализа. 
    Сгенерируй одну задачу по теме '{topic}' уровня сложности '{difficulty}' для студента 1 курса.
    Задача должна быть на вычисление производной.
    Не используй LaTeX и обратные слэши (пиши sin, cos, а не \sin, \cos).
    Обязательно ставь знак умножения (*) между цифрами и буквами, а также перед скобками.

    Верни результат СТРОГО в формате JSON, без какого-либо другого текста, вот такой структуры:
    {{
        "task": "текст задачи (например: найти производную f(x) = x^3)",
        "correct_answer": "правильный ответ строкой (например: 3*x**2)"
    }}
    """

    print("ИИ думает над задачей...")

    response = giga.chat(prompt)
    result_text = response.choices[0].message.content

    if "```json" in result_text:
        result_text = result_text.split("```json")[1].split("```")[0]
    elif "```" in result_text:
        result_text = result_text.split("```")[1].split("```")[0]

    result_text = result_text.strip()
    result_text = result_text.replace('\\', '\\\\')

    try:
        result_json = json.loads(result_text)
        result_json["task"] = result_json["task"].replace('$', '')
        return result_json
    except json.JSONDecodeError:
        print("Ошибка: GigaChat вернул не JSON. Вот что он сказал:")
        print(result_text)
        return None

# Блок для проверки
if __name__ == "__main__":
    task = generate_test(topic = "Производные", difficulty = "Средняя")
    if task:
        print("\n--- Сгенерированная задача ---")
        print(task["task"])
        print(f"\nЭталонный ответ (для проверки): {task['correct_answer']}")