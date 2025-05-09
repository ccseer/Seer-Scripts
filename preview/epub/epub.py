"""
what this script does:
    1. read index.html
    2. replace ${input_file} / jszip-3.10.1.min.js / main.css / epub-0.3.93.min.js
    3. save file as ${output_file}
"""

SCRIPT_INFO = {
    "name": "epub",
    "type": 0,
    "extensions": ["epub"],
    "arguments": [
        "-i",
        "${input_file}",
        "-o",
        "${output_file}.html",
        "${use_backslash}",
    ],
    "version": "1.0.0",
}


def parse_arg():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", help="input file path", required=True)
    parser.add_argument("-o", help="output dir path", required=True)
    args = parser.parse_args()
    return vars(args)


if __name__ == "__main__":
    import os

    args = parse_arg()
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(cur_dir, "assets")

    val = ""
    with open(os.path.join(assets_dir, "index.html"), "r", encoding="utf-8") as f:
        val = f.read()

    val = val.replace(
        "PLACEHOLDER_ZIPJS",
        os.path.join(assets_dir, "jszip-3.10.1.min.js").replace("\\", "/"),
    )
    val = val.replace(
        "PLACEHOLDER_EPUBJS",
        os.path.join(assets_dir, "epub-0.3.93.min.js").replace("\\", "/"),
    )
    val = val.replace(
        "PLACEHOLDER_CSS", os.path.join(assets_dir, "main.css").replace("\\", "/")
    )
    val = val.replace("PLACEHOLDER_INPUT", args["i"].replace("\\", "/"))

    with open(args["o"], "w", encoding="utf-8") as f:
        f.write(val)
