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

cmd = [path_pip, "install", "-r", os.path.join(cur_dir, "requirements.txt")]
print(cmd)
ret = subprocess.run(cmd)
exit(ret.returncode)
