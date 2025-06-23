from functions.run_python_file import run_python_file


def test():
    print("Result for main.py:")
    print(run_python_file("calculator", "main.py"))
    print()

    print("Result for tests.py:")
    print(run_python_file("calculator", "tests.py"))
    print()

    print("Result for ../main.py:")
    print(run_python_file("calculator", "../main.py"))
    print()

    print("Result for nonexistant.py:")
    print(run_python_file("calcualtor", "nonexistent.py"))


if __name__ == "__main__":
    test()
