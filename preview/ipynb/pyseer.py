import ctypes

SEER_OIT_MSG_W32 = 6500

SEER_OIT_SUB_LOAD_ERR = 6001
SEER_OIT_SUB_LOAD_OK = 6002
SEER_OIT_SUB_KEY_PRESS = 6003
SEER_OIT_SUB_WAGGLE = 6004
SEER_OIT_SUB_TOAST = 6005

WIN32_COPYDATA_MSG = 74

SEER_CLASSNAME = "SeerWindowClass"

SERR_MSG_KEY_WID = "window_index"
SERR_MSG_KEY_SUB_ID = "msg_sub_id"

SCRIPT_INFO = {
    "name": "ipynb",
    "type": 0,
    "extensions": ["ipynb"],
    "arguments": ["${oit}"],
    "version": "1.0.0",
    "description": "jupyter notebook\nhttps://github.com/jsvine/notebookjs",
}

class COPYDATASTRUCT(ctypes.Structure):
    import ctypes.wintypes

    _fields_ = [
        ("dwData", ctypes.wintypes.LPARAM),
        ("cbData", ctypes.wintypes.DWORD),
        ("lpData", ctypes.c_wchar_p),
    ]


def init_log(filename):
    import logging
    import os

    LOG_FILENAME = filename
    if os.path.exists(LOG_FILENAME):
        os.remove(LOG_FILENAME)
    logging.basicConfig(
        filename=LOG_FILENAME,
        level=logging.INFO,
        format="[%(asctime)s][%(levelname)s][%(name)s] %(message)s",
    )
    logging.info("logging started")
