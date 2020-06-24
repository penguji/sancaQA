import subprocess


def invoke(cmd: str):
    output, errors = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    ).communicate()
    o = output.decode("utf-8")
    return o