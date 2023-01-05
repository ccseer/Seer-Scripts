SCRIPT_INFO = {
    "name": "zipfolder",
    "type": 1,
    "extensions": ["${type_folder}"],
    "arguments": ["-e", "${7z}", "-i", "${input_file}"],
    "author": "Corey",
    "version": "1.0.0",
    "description": "Compress the folder to a zip file",
}


def parse_arg():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-e", help="7z.exe file path", required=True)
    parser.add_argument("-i", help="input file path", required=True)
    args = parser.parse_args()
    return vars(args)


if __name__ == "__main__":
    import os
    import subprocess
    import sys

    args = parse_arg()

    path_7z = args["e"]
    input_path = args["i"]

    filename = os.path.splitext(os.path.basename(input_path))[0]
    # overwrite when exists
    output_file = os.path.realpath(input_path + ".zip")

    ret = subprocess.run([path_7z, "a", output_file, input_path])
    sys.exit(ret.returncode)
