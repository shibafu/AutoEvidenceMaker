from tkinter import *
import event as ev

#Window初期値を設定する
def window_constant(window):
    window.geometry("400x200")
    window.title("Hello Tkinter")

    return window

def Tkinter_main_loop():
    #Tkinter オブジェクトを作成
    window:Tk = Tk()

    window = window_constant(window)

    #ラベルを設定する
    Label_1 = Label(window, text="Pythonマクロにようこそ！",font=("Meiryo",16,"bold")).pack()
    Label_2 = Label(window, text="このソフトはスクリプトに従って、マクロを起動します。",font=("Meiryo",11,"bold")).pack()
    Label_3 = Label(window, text="起動するには下のボタンを押下してください(^_-)-☆",font=("Meiryo",11,"bold")).pack()

    #ボタンを作成する
    #マクロ実行ボタン
    StartMacro=Button(window, text="マクロスタート！",
                      fg="black",
                      bg="gray",
                      font=("Meiryo",11,"bold"))
    #ラムダ式で内部クラスを作成し、関数変数を取得する
    start_macro_function = lambda self:ev.macroExecute()
    StartMacro.bind("<1>", start_macro_function)
    StartMacro.place(x=70, y=110)

    #終了ボタン
    exitButton=Button(window, text="終了します",
                      fg="black",
                      bg="gray",
                      font=("Meiryo",11,"bold"))
    #ラムダ式で内部クラスを作成し、関数変数を取得する
    exit_function = lambda self:ev.exit_app()
    exitButton.bind("<1>", exit_function)
    exitButton.place(x=225, y=110)

    #実行
    window.mainloop()

#メイン処理を実行
Tkinter_main_loop()