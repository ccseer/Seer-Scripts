SCRIPT_INFO = {
    "name": "ipynb",
    "type": 0,
    "extensions": ["ipynb"],
    "arguments": ["-i", "${input_file}", "${oit}"],
    "version": "1.0.0",
    "description": "jupyter notebook, https://github.com/jsvine/notebookjs",
}


def parse_arg():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", help="input file path", required=True)
    args = parser.parse_args()
    return vars(args)


class Api:
    input_file = 0

    def __init__(self, f):
        self.input_file = f

    def get_file_contents(self):
        with open(self.input_file, mode="r") as f:
            return f.read()


if __name__ == "__main__":
    import webview

    args = parse_arg()
    api = Api(args["i"])

    wnd = webview.create_window("Seer", js_api=api, url="index.html")

    webview.start()
