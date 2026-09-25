"""Basic tests for fastpy."""

import importlib

import pytest

# fastcore C extension tests
fastcore = None
for module_name in ("fastpy.core.fastcore", "fastcore"):
    try:
        fastcore = importlib.import_module(module_name)
        break
    except ImportError:
        continue


@pytest.mark.skipif(fastcore is None, reason="fastcore C extension not built")
def test_fastcore_add():
    assert fastcore.add(2, 3) == 5


@pytest.mark.skipif(fastcore is None, reason="fastcore C extension not built")
def test_fastcore_mul_double():
    assert fastcore.mul_double(2.5, 4.0) == pytest.approx(10.0)


# interpreter tests
from fastpy.interpreter import FastPyInterpreter


def test_interpreter_eval_expression():
    interp = FastPyInterpreter()
    assert interp.run("1 + 2") == 3


def test_interpreter_eval_string_expression():
    interp = FastPyInterpreter()
    assert interp.run("'fast' + 'py'") == "fastpy"


def test_interpreter_eval_builtins():
    interp = FastPyInterpreter()
    assert interp.run("sum([1, 2, 3])") == 6
