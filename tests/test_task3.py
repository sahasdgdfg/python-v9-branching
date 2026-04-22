import io
import sys
from student_solution import task3


def run_io_fun(s):
    sys.stdin = io.StringIO(s)
    sys.stdout = io.StringIO()
    task3()
    return sys.stdout.getvalue().strip()


def assert_float_equal(output, expected):
    assert abs(float(output) - expected) < 1e-9


def test_add():
    assert_float_equal(run_io_fun("5.0\n+\n3.0\n"), 8.0)


def test_sub():
    assert_float_equal(run_io_fun("7.5\n-\n2.5\n"), 5.0)


def test_mul():
    assert_float_equal(run_io_fun("4.0\n*\n2.5\n"), 10.0)


def test_div():
    assert_float_equal(run_io_fun("8.0\n/\n2.0\n"), 4.0)


def test_div_fraction():
    assert_float_equal(run_io_fun("7.5\n/\n2.5\n"), 3.0)