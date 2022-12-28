import logging

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


def init_log(filename):
    import os

    if os.path.exists(filename):
        try:
            os.remove(filename)
        except:
            return

    logging.basicConfig(
        filename=filename,
        level=logging.DEBUG,
        format="[%(asctime)s][%(levelname)s][%(name)s] %(message)s",
    )
    logging.info("logging started")


def sendMsg2Seer(json_str):
    import ctypes
    import ctypes.wintypes

    logging.info("sendMsg2Seer:" + json_str)

    class COPYDATASTRUCT(ctypes.Structure):
        import ctypes.wintypes

        _fields_ = [
            ("dwData", ctypes.wintypes.LPARAM),
            ("cbData", ctypes.wintypes.DWORD),
            ("lpData", ctypes.c_wchar_p),
        ]

    # prepare data
    FindWindowEx = ctypes.windll.user32.FindWindowExW
    hwnd = FindWindowEx(None, None, SEER_CLASSNAME, None)
    if hwnd == 0:
        logging.error("hwnd==0")
        return False

    logging.info("seer hwnd: " + str(hwnd))

    cds = COPYDATASTRUCT()
    cds.dwData = SEER_OIT_MSG_W32
    logging.info(json_str)
    cds.cbData = ctypes.sizeof(ctypes.create_unicode_buffer(json_str))
    cds.lpData = ctypes.c_wchar_p(json_str)

    # send data
    SendMessage = ctypes.windll.user32.SendMessageW
    ret = SendMessage(hwnd, WIN32_COPYDATA_MSG, None, ctypes.byref(cds))
    logging.info("SendMessage done: " + str(ret))

    return True
