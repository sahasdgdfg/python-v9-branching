import io
import sys
from student_solution import task4


def run_io_fun(s):
    sys.stdin = io.StringIO(s)
    sys.stdout = io.StringIO()
    task4()
    return sys.stdout.getvalue().strip()


def test_case1():
    assert run_io_fun("1\n5\n3\n") == "5"


def test_case2():
    assert run_io_fun("-1\n-5\n-3\n") == "-1"