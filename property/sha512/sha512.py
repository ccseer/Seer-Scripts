# https://www.quickprogrammingtips.com/python/how-to-calculate-sha256-hash-of-a-file-in-python.html

SCRIPT_INFO = {
    "name": "sha512",
    "type": 2,
    "extensions": ["exe", "dll"],
    "arguments": ["-i", "${input_file}", "-o", "${output_file}"],
}


def sha512(input_path):
    import hashlib

    sha256_hash = hashlib.sha256()
    with open(input_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


def save_data(data, output_path):
    import json

    data_map = {}
    # SHA512 is for first column in Property View
    data_map["SHA512"] = str(data)

    if output_path.lower().endswith(".json") == False:
        output_path += ".json"

    print(output_path)
    json_object = json.dumps(data_map)
    with open(output_path, "w") as f:
        f.write(json_object)


def parse_arg():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", help="input file path", required=True)
    parser.add_argument("-o", help="output dir path", required=True)
    args = parser.parse_args()
    return vars(args)


if __name__ == "__main__":
    args = parse_arg()
    print("args", args)
    val = sha512(args["i"])
    save_data(val, args["o"])
    exit(0)
