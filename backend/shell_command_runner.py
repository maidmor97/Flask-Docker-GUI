import subprocess

def run(command: list) -> str:
    result = subprocess.run(command, stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

    
