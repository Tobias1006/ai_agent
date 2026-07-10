import os
from functions.config import MAX_CHARACTERS

def get_file_content(working_directory: str, file_path:str) -> str:
    try: 
        path_work_dir = os.path.abspath(working_directory)
        full_path = os.path.normpath(os.path.join(path_work_dir, file_path))
        path_list = [full_path, path_work_dir]
        valid_target_file = os.path.commonpath(path_list) == path_work_dir

        if not valid_target_file: 
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(full_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        print(full_path)
        with open(full_path, "r") as f:
            file_content = f.read(MAX_CHARACTERS)
            if f.read(1):
                file_content += f'[...File "{file_path}" truncated at {MAX_CHARACTERS} characters]'
        return file_content
    
    except Exception as e:
            return f'Error: {e}'
    
