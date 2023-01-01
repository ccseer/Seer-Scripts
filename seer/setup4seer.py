import os
import subprocess
import sys

cur_dir = os.path.dirname(os.path.abspath(__file__))

path_pip_py = os.path.join(cur_dir, "get-pip.py")
cmd = [sys.executable, path_pip_py]
print(cmd)
ret = subprocess.run(cmd)
if ret.returncode != 0:
    exit(ret.returncode)

path_pip = os.path.realpath(os.path.join(cur_dir, "../Scripts/pip.exe"))
if os.path.exists(path_pip) is False:
    exit(-1)

cmd = [path_pip, "install", "-r", os.path.join(cur_dir, "requirements.txt")]
print(cmd)
ret = subprocess.run(cmd)
exit(ret.returncode)
