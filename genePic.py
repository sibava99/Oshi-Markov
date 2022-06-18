from turtle import position
from PIL import Image, ImageFont, ImageDraw
import cv2
import numpy as np

# 画像に文字を入れる関数
def img_add_msg(img, message):
    font_path = 'C:\Windows\Fonts\meiryo.ttc'           # Windowsのフォントファイルへのパス
    height, width, channels = img.shape[:3]                 #大きさ取得
    #print("width: " + str(width))
    #print("height: " + str(height))
    font_size = 30                                      # フォントサイズ
    font = ImageFont.truetype(font_path, font_size)     # PILでフォントを定義
    img = Image.fromarray(img)                          # cv2(NumPy)型の画像をPIL型に変換
    draw = ImageDraw.Draw(img)                          # 描画用のDraw関数を用意
    positionx = width/2 - 450
    positiony = height/2 -100

    # テキストを描画（位置、文章、フォント、文字色（BGR+α）を指定）
    draw.text((positionx, positiony), message, font=font, fill=(0,0,0, 0))
    img = np.array(img)                                 # PIL型の画像をcv2(NumPy)型に変換
    return img                                          # 文字入りの画像をリターン

img = cv2.imread('pic\lome.jpg', 1)                         # カラー画像読み込み

message = 'Hello World (ハローワールド)'                # 画像に入れる文章
img = img_add_msg(img, message)                         # 画像に文字を入れる関数を実行

# 画像を表示させる（何かキーを入力すると終了）
#cv2.imshow('title', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

cv2.imwrite('pic\output.jpg', img)