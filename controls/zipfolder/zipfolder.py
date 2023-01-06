SCRIPT_INFO = {
    "name": "zipfolder",
    "type": 1,
    "extensions": ["${type_folder}"],
    "arguments": ["-e", "${7z}", "-i", "${input_file}", "-w"],
    "author": "Corey",
    "version": "1.0.0",
    "description": "Compress the folder to a zip file",
}


def parse_arg():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-e", help="7z.exe file path", required=True)
    parser.add_argument("-i", help="input file path", required=True)
    parser.add_argument(
        "-w", help="whether open output window", required=False, action="store_true"
    )
    args = parser.parse_args()
    return vars(args)


if __name__ == "__main__":
    import os
    import subprocess
    import sys

    args = parse_arg()

    input_path = args["i"]
    filename = os.path.splitext(os.path.basename(input_path))[0]
    # overwrite when exists
    output_file = os.path.realpath(input_path + ".zip")

    ret = subprocess.run([args["e"], "a", output_file, input_path])
    if ret.returncode == 0 and args["w"] is True:
        subprocess.Popen(["explorer", "/select,", os.path.normpath(output_file)])
    sys.exit(ret.returncode)
