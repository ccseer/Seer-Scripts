import logging
import os
import sys

cur_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(cur_dir)
sys.path.append(cur_dir)

import pyseer


def script_info():
    return pyseer.SCRIPT_INFO


class Api:
    __input_file = ""
    __wid = 0
    wnd = None

    def __init__(self, w, f):
        self.__input_file = f
        self.__wid = w

    def get_file_contents(self):
        logging.info("get_file_contents")
        with open(self.__input_file, mode="r") as f:
            return f.read()

    def on_loaded(self):
        import json

        logging.info("on_loaded")

        data = {}
        data[pyseer.SERR_MSG_KEY_WID] = self.__wid
        data[pyseer.SERR_MSG_KEY_SUB_ID] = pyseer.SEER_OIT_SUB_W32_LOAD_OK
        data = json.dumps(data)
        if pyseer.sendMsg2Seer(data) == False:
            self.wnd.destroy()
            sys.exit(-1)

        self.wnd.show()
        logging.info("wnd.show")


def parse_arg():
    # ['/path/to/ipynb.py', 'wnd_identifier', 'input_file']
    if len(sys.argv) != 3:
        logging.error(sys.argv)
        exit(-1)

    wid = sys.argv[1]
    target = sys.argv[2]
    logging.info("wid: " + wid)
    logging.info("target: " + target)
    return [wid, target]


def hide_wnd(window):
    # show the window when everything is loaded
    window.hide()
    logging.info("hide_wnd")


if __name__ == "__main__":
    import webview

    pyseer.init_log("Seer-" + os.path.basename(__file__) + ".log")

    args = parse_arg()
    api = Api(args[0], args[1])

    wnd = webview.create_window(
        "Seer",
        js_api=api,
        url="index.html",
        text_select=True,
        frameless=True,
        x=-1000,
        y=-1000,
    )
    logging.info("create_window")
    api.wnd = wnd
    logging.info("init")
    webview.start(hide_wnd, wnd)
