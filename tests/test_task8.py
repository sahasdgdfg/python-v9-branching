import io
import sys
from student_solution import task8

def run_io_fun(s):
    sys.stdin = io.StringIO(s)
    sys.stdout = io.StringIO()
    task8()
    return sys.stdout.getvalue().strip()

def test_monday():
    assert run_io_fun("1\n") == "Monday"

def test_sunday():
    assert run_io_fun("7\n") == "Sunday"