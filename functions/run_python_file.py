import os
import subprocess


def run_python_file(working_directory, file_path):
    working_directory_path = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory_path, file_path))

    if not abs_file_path.startswith(working_directory_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'

    if not abs_file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a python file'

    try:
        result = subprocess.run(
            ["python", abs_file_path],
            capture_output=True,
            timeout=30,
            text=True,
            cwd=working_directory_path,
        )

        if not result:
            return "No output produced"

        output = []
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"nSTDERR:\n{result.stderr}")
        if result.returncode != 0:
            output.append(f"\nProcess exited with code {result.returncode}")

        return "\n".join(output)

    except Exception as e:
        return f"Error: executing Python file: {e}"


if __name__ == "__main__":
    run_python_file("calculator", "lorem.txt")
