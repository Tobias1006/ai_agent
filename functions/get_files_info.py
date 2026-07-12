import os 

schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}

def get_files_info(working_directory:str, directory: str = ".") -> str:
    try:
        ent_det = []
        
        path_work_dir = os.path.abspath(working_directory)
        full_path = os.path.normpath(os.path.join(path_work_dir, directory))
        path_list = [full_path, path_work_dir]
        valid_target_dir = os.path.commonpath(path_list) == path_work_dir
        
        list_of_files = os.listdir(full_path) 

        if not valid_target_dir: 
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(full_path):
            return f'Error: "{directory}" is not a directory'
        for ent in list_of_files:
            path_ent = os.path.join(full_path, ent)
            ent_det.append((path_ent, os.path.getsize(path_ent), os.path.isdir(path_ent)))
        for ent in ent_det: 
            print(f'- {ent[0]}: file_size={ent[1]}, is_dir={ent[2]}')
        return ent_det
    except Exception as e:
            return f'Error: {e}'

