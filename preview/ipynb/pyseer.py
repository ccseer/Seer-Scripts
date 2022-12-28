import ctypes

SEER_OIT_MSG_W32 = 6500
SEER_OIT_SUB_W32_LOAD_ERR = 6501
SEER_OIT_SUB_W32_LOAD_OK = 6502
SEER_OIT_SUB_W32_KEY_PRESS = 6503
SEER_OIT_SUB_W32_WAGGLE = 6504
SEER_OIT_SUB_W32_TOAST = 6505


SEER_CLASSNAME = "SeerWindowClass"

SERR_MSG_KEY_WID = "window_index"
SERR_MSG_KEY_SUB_ID = "msg_sub_id"

# win32con.WM_COPYDATA
WIN32_COPYDATA_MSG = 74

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
        try:
            os.remove(LOG_FILENAME)
        except:
            return
    
    logging.basicConfig(
        filename=LOG_FILENAME,
        level=logging.INFO,
        format="[%(asctime)s][%(levelname)s][%(name)s] %(message)s",
    )
    logging.info("logging started")
