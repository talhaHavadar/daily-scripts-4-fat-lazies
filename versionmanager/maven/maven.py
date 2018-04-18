import subprocess
import re

def get_version(project_path):
    process = subprocess.Popen(["mvn", "help:evaluate", '-Dexpression=project.version'], shell=True, cwd=project_path,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    rcode = process.returncode
    if rcode == 0:
        return True, __clear_output__(out)[0]
    return False, out

def set_version(project_path, version):
    process = subprocess.Popen(["mvn", "versions:set", '-DnewVersion=' + version], shell=True, cwd=project_path,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    rcode = process.returncode
    if rcode == 0:
        return True, version
    return False, out

def __clear_output__(output_string):
    output = []
    for line in output_string.splitlines():
        if line.decode().startswith("["):
            continue
        output.append(line.decode())
    return output