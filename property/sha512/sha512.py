SCRIPT_INFO = {
    "name": "sha512",
    "type": 2,
    "extensions": ["exe", "dll"],
    "arguments": ["-i", "${input_file}", "-o", "${output_file}"],
}


def sha512(input_path):
    # https://www.quickprogrammingtips.com/python/how-to-calculate-sha256-hash-of-a-file-in-python.html

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
    # the value can only be str type
    data_map["SHA512"] = str(data)
    # nested
    # data_map_nested = {}
    # data_map_nested["nested_1"] = "nested_1_v"
    # data_map_nested["nested_2"] = "nested_2_v"
    # data_map["nested_title"] = data_map_nested

    if output_path.lower().endswith(".json") == False:
        output_path += ".json"

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
    val = sha512(args["i"])
    save_data(val, args["o"])
    exit(0)
