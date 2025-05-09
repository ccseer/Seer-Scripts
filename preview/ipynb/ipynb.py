import json
import logging
import os
import shutil


def script_info():
    SCRIPT_INFO = {
        "name": "ipynb",
        "type": 0,
        "extensions": ["ipynb"],
        "arguments": ["-i", "${input_file}", "-o", "${output_file}.html"],
        "version": "1.1.0",
        "description": "jupyter notebook\nhttps://github.com/jsvine/notebookjs",
    }
    return SCRIPT_INFO


def generate_final_html(input_file: str, output_file: str, template_file: str):
    logging.info(f"Generating HTML from: {input_file}")
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            ipynb_json = json.dumps(json.load(f), ensure_ascii=False)
        with open(template_file, "r", encoding="utf-8") as f:
            template_html = f.read()
        final_html = template_html.replace("IPYNB_JSON", ipynb_json)
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(final_html)

        template_dir = os.path.dirname(template_file)
        output_dir = os.path.dirname(output_file)
        src_assets = os.path.join(template_dir, "assets")
        dst_assets = os.path.join(output_dir, "assets")
        if os.path.exists(dst_assets):
            shutil.rmtree(dst_assets)
        shutil.copytree(src_assets, dst_assets)

        logging.info(f"HTML written to: {output_file}")
        return True
    except Exception as e:
        logging.error(f"Failed to generate HTML: {e}")
        return False


def parse_arg():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", help="input file path", required=True)
    parser.add_argument("-o", help="output dir path", required=True)
    args = parser.parse_args()
    return vars(args)


if __name__ == "__main__":
    args = parse_arg()
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(cur_dir, "assets")

    input_ipynb = args["i"]
    if not os.path.exists(input_ipynb):
        print(f"Input file {input_ipynb} does not exist.")
        exit(-1)
    output_html = args["o"]
    template = os.path.join(os.path.dirname(__file__), "index.html")

    ok = generate_final_html(input_ipynb, output_html, template)
    if not ok:
        print("Error generating HTML.")
        exit(-1)
