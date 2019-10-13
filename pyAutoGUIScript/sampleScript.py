import pyautogui as pg

def script_execute():

    mouse_position = pg.position()
    print("現在のマウス位置は X= " + str(mouse_position.x) + "Y= " + str(mouse_position.y))

    print("マウスを移動します")
    #マウスを0.5秒かけてx=1000, y=200に移動する
    pg.moveTo(1200, 600, duration=2)
    #目標の座標に向けてマウスをドラッグする
    pg.dragTo(300, 300, duration=2)

    pg.moveTo(1700, 900, duration=2)
    print("マウスクリックします")
    #10回左クリックをする
    pg.click(clicks=10, button='left')

    print("キーを入力します")
    # インターバル0.5秒でshiftを2回押す
    pg.press('shift', presses=2, interval=0.5)# インターバル0.5秒でshiftを2回押す
    pg.typewrite("hello! PyAutoGUIs!")
    pg.click(clicks=2, button='left')  # ２回クリックする

    print("スクリーンショットを取ります（ホットキーでも全然可能）")

    #画像を使った繊維、
    #Youtubeのロゴを認識してそこの座標を取得する
    x, y = pg.locateCenterOnScreen("pyAutoGUIScript/home.png")

    print("ロゴの画像の位置は　x=" + str(x) + "y=" + str(y))
    pg.moveTo(x, y, duration=2)
    pg.moveRel(0, 80, duration=2) #相対座標
    pg.click(clicks=1, button='left')  # ２回クリックする
    pg.PAUSE = 2 #2秒待つ
    #ホットキーを使ったスクショ
    pg.hotkey('winleft', 'prtsc')
    #座標指定スクショ
    pg.screenshot("C:\screenShot\myscshot.png", region=(1, 1, 1000, 1000))
    print