from flask import Flask
app = Flask(__name__)
from flask import request, jsonify
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from learn_simple import study_from_markov
from markov_takano import textGen

DEFAULT_ERROR_MSG = "Sever Error"

@app.route("/test/", methods=["GET"])
def test():
    return "Welcome to test!!!"

@app.route("/generate_text/", methods=['POST'])
def generate_text():
    if "text" not in request.POST: return DEFAULT_ERROR_MSG
    minchar = 10 if "min_char" not in request.POST else request.POST["min_char"]
    maxchar = 75 if "max_char" not in request.POST else request.POST["max_char"]
    return study_from_markov(request.POST["text"], maxchar, minchar)

@app.route("/generate_text_test/", methods=['GET'])
def generate_text_test():
    text = """
        私の人生はいつもこうなのですわ～！
        先日、私の物理的な中身を知っていただきましたから、今回は私の脳みその中身を見ていただきたいと思いますわ～！
        もう、どうとでもなれですわ～！
        今、走ってきておりますわ～！バイオハザードはこちらに向けて、走ってきておりますわ～！
        ゾンビをぶっ倒すつもりが、私のメンタルがぶっ倒されておりますわ～！
        どうして私は今こんなことをしているのかしら？
        こうするしかなかったんですわ～！私の脳みそではこれぐらいしかできませんでした。そこも含めて私の脳みそをお楽しみあれ。
        ここに石の県と川の県があったとおもうんですよね（岩手県と秋田県を指しながら）。石川県ていうのもあった気がしますわ。でも川は石川県ではなかった気が...
        ここは長いから長野（新潟県を指しながら）
        長野でございますわ～！絶対にここは長野でございますわ～！（新潟県を指しながら）
        チーバくんってこんな形の犬でしたわね（顔だけになったチーバくんの絵を描きながら）
        ...ハァ？分かりませんわ？
        頑張ったらここがお鼻に見えますわ～！（房総半島の先を指しながら）
        こっそり勉強してから、この配信は行いたかったですわ～！
        なにかどこら辺かに、群馬がありましてよ
        これは長野（新潟県を指しながら）...これは？（佐渡島を指しながら）これは長野の...子ども？！
        関西については詳しいですわ私（２府県のみ正解）
        これって一つの県ですの？（福井県嶺南地域を指しながら）
        京都は小さそうです...ここが京都じゃありませんの？ここが京都だと私思いますわ～！（福井県嶺南地域を指しながら）
        こんな広い土地ありました？この土地なんなんですの？（兵庫県を指しながら）
        広そうな県といえばオーストラリア
        おバイオはあと、３分の１割を切っておりますわ
        こう見ると大阪ってすっごい小さいですわね。あの小さい街にあれだけ物が建っていれば、そーーーりゃ忙しいですわ大阪は
    """
    return textGen(text)

if __name__ == "__main__":
    app.run(debug=True)