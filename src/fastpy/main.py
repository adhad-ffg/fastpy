import sys
from fastpy import __version__
from .interpreter import FastPyInterpreter


def main():
    print(f"fastpy version {__version__}")
    interpreter = FastPyInterpreter()

    if len(sys.argv) > 1:
        with open(sys.argv[1], encoding="utf-8") as f:
            code = f.read()
        result = interpreter.run(code)
        if result is not None:
            print(result)
    else:
        interpreter.repl()


if __name__ == "__main__":
    main()
