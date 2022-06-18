from flask import Flask
app = Flask(__name__)
from flask import request, jsonify
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
# from learn_simple import study_from_markov
# from markov_takano import textGen
from learn_v2 import study_from_markov, generate_from_markov, getTweet
from dotenv import load_dotenv
import os
from sql_util import Model, get_random_id


load_dotenv()

DEFAULT_ERROR_MSG = "Error"

engine = create_engine(os.environ.get("DATABASE_URI"))

@app.route("/test/", methods=["GET"])
def test():
    if os.getenv('DEBUG') != "true": return DEFAULT_ERROR_MSG
    return "Welcome to test!!!"


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


@app.route("/generate_text/", methods=['POST'])
def generate_text():
    """generate_text POST["text"]から文章を生成する

    コーパスはPOSTパラメーターに含める

    :return: 生成した文章
    :rtype: str
    """
    if "text" not in request.form: return DEFAULT_ERROR_MSG
    minchar = 10 if "min_char" not in request.form else request.form["min_char"]
    maxchar = 75 if "max_char" not in request.form else request.form["max_char"]
    model = study_from_markov(request.form["text"])
    return generate_from_markov(model, maxchar, minchar)

@app.route("/save_model/", methods=['POST'])
def save_model():
    """save_model コーパスからモデルを保存する

    required: text (represents corpus)

    :return: 作成したモデルのid、generate_model/idにgetでアクセス
    :rtype: str
    """
    if "text" not in request.form: return DEFAULT_ERROR_MSG
    model_json = study_from_markov(request.form["text"])
    SessionClass = sessionmaker(engine)
    session = SessionClass()
    all_models = session.query(Model).all()
    model_ids = [room.share_id for room in all_models]
    rand_id = get_random_id(24)
    while rand_id in model_ids: rand_id = get_random_id(24) # ランダムな文字列生成
    new_model = Model(rand_id, model_json)
    session.add(new_model)
    session.commit()
    session.close()
    return rand_id

@app.route("/generate_text/<model_id>")
def generate_from_model(model_id, methods=["GET"]):
    """generate_from_model 保存されているモデルから生成を行う

    データベースにmodel_idで検索を行う。

    :param model_id: モデルを識別する一意なid
    :type model_id: str
    :return: 生成された文
    :rtype: str
    """
    print(model_id)
    SessionClass = sessionmaker(engine)
    session = SessionClass()
    all_models = session.query(Model).all()
    for i in all_models:
        print(f"Model.share_id: {i.share_id}, request_id: {model_id}, isEqual: {i.share_id==model_id}")
    searching_model = session.query(Model).filter(Model.share_id==model_id).first()
    if searching_model is None: return DEFAULT_ERROR_MSG
    text = generate_from_markov(searching_model.model_json, 75, 10)
    session.close()
    return text

@app.route("/generate_text_twitter/", methods=["POST"])
def generate_text_with_twitter():
    """generate_text_with_twitter TwitterIDからテキストを生成する

    required: twitter_id, represents twitter_id to make model from
    TwitterIDからツイートを収集し、モデルを作成する
    これで作られたモデルは必ず保存される

    :return: data("sentence", "model_id")
    :rtype: dict
    """
    if "twitter_id" not in request.form: return DEFAULT_ERROR_MSG
    SessionClass = sessionmaker(engine)
    session = SessionClass()
    # 既にモデルがある場合新しく作らない
    searching_model = session.query(Model).filter(Model.twitter_id==request.form["twitter_id"]).first()
    data = {}
    if searching_model is not None:
        print("found model")
        data["sentence"] = generate_from_markov(searching_model.model_json, 75, 10)
        data["model_id"] = searching_model.share_id
        return jsonify(data)
    print("making new model from twitter")
    all_models = session.query(Model).all()
    model_json = getTweet(request.form["twitter_id"])
    model_ids = [room.share_id for room in all_models]
    rand_id = get_random_id(24)
    while rand_id in model_ids: rand_id = get_random_id(24) # ランダムな文字列生成
    new_model = Model(rand_id, model_json, request.form["twitter_id"])
    session.add(new_model)
    session.commit()
    session.close()
    data["sentence"] = generate_from_markov(model_json, 75, 10)
    data["model_id"] = rand_id
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)