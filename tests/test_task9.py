import io
import sys
from student_solution import task9

def run_io_fun(s):
    sys.stdin = io.StringIO(s)
    sys.stdout = io.StringIO()
    task9()
    return sys.stdout.getvalue().strip()

def test_exists():
    assert run_io_fun("3\n4\n5\n") == "Triangle exists"

def test_not_exists():
    assert run_io_fun("1\n2\n3\n") == "Triangle does not exist"