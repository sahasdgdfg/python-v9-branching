import io
import sys
from student_solution import task2

def run_io_fun(s):
    sys.stdin = io.StringIO(s)
    sys.stdout = io.StringIO()
    task2()
    return sys.stdout.getvalue().strip()

def test_minor():
    assert run_io_fun("17\n") == "Minor"

def test_adult():
    assert run_io_fun("30\n") == "Adult"

def test_senior():
    assert run_io_fun("70\n") == "Senior"