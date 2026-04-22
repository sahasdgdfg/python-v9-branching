import io
import sys
from student_solution import task6

def run_io_fun(s):
    sys.stdin = io.StringIO(s)
    sys.stdout = io.StringIO()
    task6()
    return sys.stdout.getvalue().strip()

def test_freezing():
    assert run_io_fun("-5\n") == "Freezing"

def test_warm():
    assert run_io_fun("25\n") == "Warm"

def test_hot():
    assert run_io_fun("40\n") == "Hot"