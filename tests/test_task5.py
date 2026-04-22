import io
import sys
from student_solution import task5

def run_io_fun(s):
    sys.stdin = io.StringIO(s)
    sys.stdout = io.StringIO()
    task5()
    return sys.stdout.getvalue().strip()

def test_leap():
    assert run_io_fun("2020\n") == "Leap year"

def test_not_leap():
    assert run_io_fun("1900\n") == "Not leap year"