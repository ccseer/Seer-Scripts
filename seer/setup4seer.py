import os
import subprocess
import sys

cur_dir = os.path.dirname(os.path.abspath(__file__))

path_pip_py = os.path.join(cur_dir, "get-pip.py")
# print(path_pip_py, sys.executable)
ret = subprocess.run([sys.executable, path_pip_py])
if ret.returncode != 0:
    exit(ret.returncode)

path_pip = os.path.realpath(os.path.join(cur_dir, "../Scripts/pip.exe"))
if os.path.exists(path_pip) is False:
    exit(-1)
ret = subprocess.run(
    [path_pip, "install", "-r", os.path.join(cur_dir, "requirements.txt")]
)
exit(ret.returncode)
