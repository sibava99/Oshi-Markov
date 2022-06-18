from flask import Flask
app = Flask(__name__)
from flask import request, jsonify
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from learn_simple import study_from_markov
from markov_takano import textGen
from dotenv import load_dotenv
import os
from sql_util import Model


load_dotenv()

DEFAULT_ERROR_MSG = "Error"

engine = create_engine(os.environ.get("DATABASE_URI"))

@app.route("/test/", methods=["GET"])
def test():
    if os.getenv('DEBUG') != "true": return DEFAULT_ERROR_MSG
    return "Welcome to test!!!"

@app.route("/generate_text/", methods=['POST'])
def generate_text():
    """generate_text POST["text"]から文章を生成する

    コーパスはPOSTパラメーターに含める

    :return: 生成した文章
    :rtype: str
    """
    if "text" not in request.POST: return DEFAULT_ERROR_MSG
    minchar = 10 if "min_char" not in request.POST else request.POST["min_char"]
    maxchar = 75 if "max_char" not in request.POST else request.POST["max_char"]
    return study_from_markov(request.POST["text"], maxchar, minchar)

@app.route("/save_model/", methods=['POST'])
def save_model():
    if "text" not in request.POST: return DEFAULT_ERROR_MSG
    # textからモデルを作成する
    SessionClass = sessionmaker(engine)
    session = SessionClass()
    # ランダムな文字列生成
    new_model = Model()
    session.add(new_model)
    session.commit()
    session.close()
    return 

@app.route("/generate_text_test/", methods=['GET'])
def generate_text_test():    
    """generate_text_test テスト用の文生成

    ファイルから読み込みを行う

    :return: 生成した文章
    :rtype: str
    """
    if os.getenv('DEBUG') != "true": return DEFAULT_ERROR_MSG
    text = open("data/output.txt", 'r', encoding="utf-8").read()
    return study_from_markov(text)

@app.route("/generate_text/<model_id>")
def generate_from_model(model_id):
    """generate_from_model 保存されているモデルから生成を行う

    データベースにmodel_idで検索を行う。

    :param model_id: モデルを識別する一意なid
    :type model_id: str
    :return: 生成された文
    :rtype: str
    """
    SessionClass = sessionmaker(engine)
    session = SessionClass()
    searching_model = session.query(Model).filter(Model.share_id==model_id).first()
    if searching_model is None: return DEFAULT_ERROR_MSG
    # model = from_json(searching_model.model_json)
    session.close()
    return "In Progress"

if __name__ == "__main__":
    app.run(debug=True)