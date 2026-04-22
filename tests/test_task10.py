import io
import sys
from student_solution import task10  # функция или блок с твоим кодом

def run_io_fun(input_data):
    sys.stdin = io.StringIO(input_data)
    sys.stdout = io.StringIO()
    task10()  # вызываем код задачи 10
    return sys.stdout.getvalue().strip()

def test_weak_short():
    assert run_io_fun("abc") == "Weak"
    assert run_io_fun("1234567") == "Weak"

def test_medium_only_digits():
    assert run_io_fun("12345678") == "Medium"
    assert run_io_fun("00000000") == "Medium"

def test_strong_title_and_digits():
   
    assert run_io_fun("12345678".title()) == "Strong"  # "12345678" → Title для цифр остаётся цифры