from pyAutoGUIScript import sampleScript as s1
from logging import Handler, StreamHandler, getLogger, DEBUG
from tkinter import messagebox

import datetime

#定数
LOG_DATETIME_FORMAT = "%Y/%m/%d %H:%M:%S"

#ロガーを設定する
logger = getLogger(__name__)
logger.setLevel(DEBUG)
#ログをコンソール上に出す設定
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.addHandler(handler)
#アプリを終了する
def exit_app():
    logger.info("アプリを終了します " + datetime.datetime.today().strftime(LOG_DATETIME_FORMAT))
    exit()

#マクロを実行する
def macroExecute():
    logger.info("Macro Execute! " + datetime.datetime.today().strftime(LOG_DATETIME_FORMAT))
    s1.script_execute()

    messagebox.showinfo("実行完了！", "マクロの実行が終了しましたヾ(｡>﹏<｡)ﾉﾞ✧*。 ")