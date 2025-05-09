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
SERR_MSG_KEY_TOAST = "toast_text"

# win32con.WM_COPYDATA
WIN32_COPYDATA_MSG = 74


def init_log(filename):
    import os

    if os.path.exists(filename):
        try:
            os.remove(filename)
        except:
            return
    # encoding is added to logging.basicConfig after 3.8.x
    # so we can't use it
    log = logging.getLogger()
    log.setLevel(logging.DEBUG)
    handler = logging.FileHandler(filename, "w", "utf-8")
    handler.setFormatter(
        logging.Formatter("[%(asctime)s][%(levelname)s][%(name)s] %(message)s")
    )
    log.addHandler(handler)
    logging.info("logging started")


def sendMsg2Seer(json_str):
    import ctypes
    import ctypes.wintypes

    logging.info("sendMsg2Seer:" + json_str)

    class COPYDATASTRUCT(ctypes.Structure):
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

    IsWindowVisible = ctypes.windll.user32.IsWindowVisible
    is_visible = IsWindowVisible(hwnd)
    logging.info("seer is_visible: " + str(is_visible))
    if is_visible == 0:
        return False

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


# def getWindowPos():
#     import ctypes
#     import ctypes.wintypes

#     FindWindowEx = ctypes.windll.user32.FindWindowExW
#     hwnd = FindWindowEx(None, None, SEER_CLASSNAME, None)
#     if hwnd == 0:
#         logging.error("hwnd==0")
#         return False
#     GetWindowRect = ctypes.windll.user32.GetWindowRect
#     LPRECT = ctypes.wintypes.RECT()
#     GetWindowRect(hwnd, ctypes.byref(LPRECT))
#     return (LPRECT.left, LPRECT.top)
