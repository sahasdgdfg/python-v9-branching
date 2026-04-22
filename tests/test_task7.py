import io
import sys
from student_solution import task7

def run_io_fun(s):
    sys.stdin = io.StringIO(s)
    sys.stdout = io.StringIO()
    task7()
    return sys.stdout.getvalue().strip()

def test_A():
    assert run_io_fun("95\n") == "A"

def test_C():
    assert run_io_fun("65\n") == "C"

def test_F():
    assert run_io_fun("20\n") == "F"