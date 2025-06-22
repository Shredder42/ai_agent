import os


def get_files_info(working_directory, directory=None):
    working_directory_path = os.path.abspath(working_directory)
    directory_path = os.path.normpath(os.path.join(working_directory_path, directory))

    if not directory_path.startswith(working_directory_path):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(directory_path):
        return f'Error: "{directory}" is not a directory'

    try:
        directory_contents = os.listdir(directory_path)

        data_list = [
            f"- {item}: file_size={os.path.getsize(os.path.join(directory_path, item))} bytes, is_dir={os.path.isdir(os.path.join(directory_path, item))}"
            for item in directory_contents
        ]

        return "\n".join(data_list)

    except Exception as e:
        return f"Error listing files: {e}"
