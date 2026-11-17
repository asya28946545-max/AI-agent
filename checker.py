import sympy as sp

def check_answer(student_answer: str, correct_answer: str):
    try:
        student_clean = student_answer.replace(' ', '')
        correct_clean = correct_answer.replace(' ', '')

        student_clean = student_clean.replace('**', '^').replace('*', '')
        correct_clean = correct_clean.replace('**', '^').replace('*', '')

        student_clean = student_clean.replace('x', '*x')
        correct_clean = correct_clean.replace('x', '*x')

        student_clean = student_clean.replace('^', '**')
        correct_clean = correct_clean.replace('^', '**')

        expr_student = sp.sympify(student_clean)
        expr_correct = sp.sympify(correct_clean)

        difference = sp.simplify(expr_student - expr_correct)
        if difference == 0:
            return True
        else:
            return False

    except Exception as e:
        return False  # Если ввели ерунду

# --- Блок для проверки ---
print("Тест 1 (должно быть True):", check_answer("8x^3 + 10*x", "8x**3 + 10*x"))
print("Тест 2 (должно быть False):", check_answer("2*x", "8x^3 + 10x"))