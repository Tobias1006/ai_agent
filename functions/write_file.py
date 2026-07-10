import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try: 
        path_work_dir = os.path.abspath(working_directory)
        full_path = os.path.normpath(os.path.join(path_work_dir, file_path))
        path_list = [full_path, path_work_dir]
        valid_target_path = os.path.commonpath(path_list) == path_work_dir

        if not valid_target_path: 
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(full_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        
        if '/' in file_path:
            dirs_in_path = file_path.rsplit('/')
            os.makedirs(dirs_in_path[0], exist_ok=True)
        with open(full_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as e:
            return f'Error: {e}'
    