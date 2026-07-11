import os
import subprocess

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Runs files from the format .py",
        "parameters": {
            "required": ["file_path","args"],
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Name of the .py file to be executed. Should end in the .py format.",
                },
                "args": {
                    "type": "list of strings",
                    "description": "Contains any arguments that the function that is being called might require.",
                }
            },
        },
    },
}

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:    
        path_work_dir = os.path.abspath(working_directory)
        full_path = os.path.normpath(os.path.join(path_work_dir, file_path))
        path_list = [full_path, path_work_dir]
        valid_target_path = os.path.commonpath(path_list) == path_work_dir

        if not valid_target_path: 
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(full_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if full_path[len(full_path)-3:len(full_path)] != ".py":
            return f'Error: "{file_path}" is not a Python file'

        command = ['python', os.path.abspath(full_path)]
        if args != None:
             command.extend(args)

        compl_process = subprocess.run(command, capture_output=True,text=True,timeout=30)
        output_string = f''
        if compl_process.returncode != 0:
            output_string = output_string + f'Process exited with code {compl_process.returncode}'
        if compl_process.stderr == '' and compl_process.stdout == '':
            output_string = output_string + f'\nNo output produced'
        elif compl_process.stderr == '':
            output_string = output_string + f'\nSTDOUT: {compl_process.stdout}'
        elif compl_process.stdout == '':
            output_string = output_string + f'\nSTDERR: {compl_process.stderr}'
        
        return output_string
    
    except Exception as e:
        return f'Error: {e}'