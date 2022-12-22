import os
import sys
from pathlib import Path

__save_path = os.path.join(Path.home(), "Downloads")


PLUGIN_INFO = {
    "name": "unzip",
    # 0: preview
    # 1: button in control bar
    # 2: property view
    "type": 1,
    # extensions: will show the button when matched
    "extension": ["zip", "rar", "7z"],
    # unzip.py -e "/path/to/7z.exe" -i "/path/to/z.zip" -o "/path/to/save/"
    # ${7z}: https://github.com/ccseer/Seer/wiki/7.-Scripts
    "arguments": ["-e", "${7z}", "-i", "${input}", "-o", __save_path, "-w"],
    # optional below
    "author": "Corey",
    "version": "1.0.0",
    "description": "unzip zip file here",
    # "icon_path":""
}


def parse_arg():
    import argparse

    parser = argparse.ArgumentParser(
        prog="unzip",
        description="Scripts for Seer",
        epilog="https://github.com/ccseer/Seer-Scripts",
    )
    parser.add_argument("-e", help="7z.exe file path", required=True)
    parser.add_argument("-i", help="input file path", required=True)
    parser.add_argument("-o", help="output dir path", required=True)
    parser.add_argument(
        "-w", help="whether open output window", required=False, action="store_true"
    )
    # parser.print_help()
    args = parser.parse_args()
    return vars(args)


# ZipFile.extractall
if __name__ == "__main__":
    import subprocess

    args = parse_arg()

    # this_py ${PLUGIN_INFO["arguments"]}
    print("args", args)

    # this_py = sys.argv[0]
    path_7z = args["e"]
    input_path = args["i"]
    if os.path.exists(path_7z) is False or os.path.exists(input_path) is False:
        print(
            "file not found, path_7z: {0}, input_path: {1}".format(
                os.path.exists(path_7z), os.path.exists(input_path)
            )
        )
        sys.exit(-1)

    output_dir = args["o"]
    # if os.path.exists(output_dir) is False:
    #     output_dir = __save_path

    # p = r"C:\Program Files\WindowsApps\CNABA5E861-AC2A-4523-B3C1.Seer-AWindowsQuickLookTo_3.1.1.0_neutral__p7t0z30wh4868\Seer\plugins\7z.exe"
    # p = r"C:\Program Files (x86)\Seer\plugins\7z.exe"
    ret = subprocess.run([path_7z, "x", input_path, "-r", "-y", "-o" + output_dir])
    if ret.returncode == 0 and args["w"] is True:
        subprocess.Popen(["explorer", os.path.normpath(output_dir)])
    sys.exit(ret.returncode)
