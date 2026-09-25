class FastPyInterpreter:
    def __init__(self):
        self.globals = {"__name__": "__fastpy__"}

    def run(self, code: str):
        """Execute code and return the result"""
        try:
            compiled = compile(code, "<fastpy>", "eval" if self._is_expression(code) else "exec")
            return eval(compiled, self.globals)
        except SyntaxError:
            try:
                exec(code, self.globals)
            except Exception as e:
                print(f"Execution error: {type(e).__name__}: {e}")
        except Exception as e:
            print(f"Error: {type(e).__name__}: {e}")

    def _is_expression(self, code: str) -> bool:
        """Simple check if code is an expression rather than a statement"""
        code = code.strip()
        if not code or code.startswith(("#", "def ", "class ", "if ", "for ", "while ")):
            return False
        return True

    def repl(self):
        """Interactive read-eval-print loop"""
        print("fastpy REPL — type exit or quit to exit")
        while True:
            try:
                line = input(">>> ")
            except (EOFError, KeyboardInterrupt):
                print("\nExiting")
                break
            if line.lower() in ("exit", "quit"):
                break
            result = self.run(line)
            if result is not None:
                print(result)
