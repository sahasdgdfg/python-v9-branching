import sys
import os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import ast
import inspect
import pytest
import student_solution


FORBIDDEN_NODES = (
    ast.For,
    ast.While,
    ast.ListComp,
    ast.SetComp,
    ast.DictComp,
    ast.GeneratorExp,
)


def check_no_loops(func):
    source = inspect.getsource(func)
    tree = ast.parse(source)

    for node in ast.walk(tree):
        if isinstance(node, FORBIDDEN_NODES):
            pytest.fail(
                f"Запрещено использовать циклы или генераторы в функции {func.__name__}"
            )


@pytest.fixture(autouse=True)
def no_loops_check():
    for name in dir(student_solution):
        if name.startswith("task"):
            func = getattr(student_solution, name)
            if callable(func):
                check_no_loops(func)