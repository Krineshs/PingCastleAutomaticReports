import subprocess

def run_pingcastle_process(arguments, creationflags):
    process = subprocess.Popen(arguments, creationflags=creationflags)
    process.communicate()