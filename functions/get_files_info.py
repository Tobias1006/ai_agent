import os 

def get_files_info(working_directory:str, directory: str = ".") -> str:
    try:
        path_work_dir = os.path.abspath(working_directory)
        full_path = os.path.normpath(os.path.join(path_work_dir, directory))
        path_list = [full_path, path_work_dir]
        valid_target_dir = os.path.commonpath(path_list) == path_work_dir
        if not valid_target_dir: 
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(full_path):
            return f'Error: "{directory}" is not a directory'
        return f'Success: "{directory}" is within the working directory'
    except Exception as e:
            return f'Error: {e}'

