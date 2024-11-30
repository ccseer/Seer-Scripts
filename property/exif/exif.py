SCRIPT_INFO = {
    "name": "exif",
    "type": 2,
    "version": "1.0.0",
    "description": "Meta Information\nhttps://exiftool.org",
    "arguments": ["-i", "${input_file}", "-o", "${output_file}"],
    # https://exiftool.org/#supported
    "extensions": [
        "jpg",
        "png",
        "exr",
        "gpr",
        "heic",
        "nef",
        "raw",
        "ttf",
        "mobi",
        "azw",
        "azw3",
        "epub",
    ],
}


def process(input_path, output_path):
    import json
    import os
    import subprocess

    cur_dir = os.path.dirname(os.path.abspath(__file__))
    exe_path = os.path.join(cur_dir, "exiftool/exiftool.exe")

    try:
        sp = subprocess.check_output([exe_path, input_path, "-j"])
        # array ?
        obj = json.loads(sp.decode("utf-8"))
        dict_ret = {"EXIF": obj[0]}

        if not output_path.lower().endswith(".json"):
            output_path += ".json"

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(dict_ret, f, ensure_ascii=False, indent=4)
    except subprocess.CalledProcessError as e:
        print(f"Error executing exiftool: {e}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")


def parse_arg():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", help="input file path", required=True)
    parser.add_argument("-o", help="output dir path", required=True)
    args = parser.parse_args()
    return vars(args)


if __name__ == "__main__":
    args = parse_arg()
    process(args["i"], args["o"])
