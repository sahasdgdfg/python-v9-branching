import io
import sys
from student_solution import task1

def run_io_fun(s):
    sys.stdin = io.StringIO(s)
    sys.stdout = io.StringIO()
    task1()
    return sys.stdout.getvalue().strip()

def test_even():
    assert run_io_fun("4\n") == "Even"

def test_odd():
    assert run_io_fun("5\n") == "Odd"