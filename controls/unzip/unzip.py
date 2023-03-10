import os


def script_info():
    from pathlib import Path

    save_dir = os.path.join(Path.home(), "Downloads")
    si = {
        "name": "unzip",
        # 0: preview
        # 1: controls
        # 2: property
        "type": 1,
        # extensions: will show the button when matched
        "extensions": ["zip", "rar", "7z"],
        # unzip.py -e "/path/to/7z.exe" -i "/path/to/z.zip" -o "/path/to/save/"
        # ${7z}: https://github.com/ccseer/Seer/wiki/7.-Scripts
        "arguments": ["-e", "${7z}", "-i", "${input_file}", "-o", save_dir, "-w"],
        # optional below
        "author": "Corey",
        "version": "1.0.1",
        "description": "unzip archive file here",
        # https://freeiconshop.com/icon/zip-icon-flat/
        "icon_path": "icon.png",
    }
    return si


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
    args = parser.parse_args()
    return vars(args)


# ZipFile.extractall
if __name__ == "__main__":
    import subprocess
    import sys

    args = parse_arg()

    # this_py ${PLUGIN_INFO["arguments"]}

    # this_py = sys.argv[0]
    path_7z = args["e"]
    input_path = args["i"]
    if os.path.exists(path_7z) is False or os.path.exists(input_path) is False:
        sys.exit(-1)

    dist_folder = os.path.splitext(os.path.basename(input_path))[0]
    output_dir = os.path.join(args["o"], dist_folder)

    ret = subprocess.run([path_7z, "x", input_path, "-r", "-y", "-o" + output_dir])
    if ret.returncode == 0 and args["w"] is True:
        subprocess.Popen(["explorer", os.path.normpath(output_dir)])
    sys.exit(ret.returncode)
