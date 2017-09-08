#coding:utf-8

import json
from flask import jsonify,request,Response
from . import api
from .. import db
from ..models import Word,Article,Show,Carousel,Qrcode,User

@api.route('/index/', methods=["GET"])
def index():
    return jsonify({
        "index":[
            {
                "name":"共享单车",
                "url": "传说中的url"
            },
            {
                "name":"航天工程",
                "url": "传说中的url"
            },
            {
                "name":"北斗导航",
                "url": "传说中的url"
            },
            {
                "name":"桥梁建设",
                "url": "传说中的url"
            },
            {
                "name":"孔子学院",
                "url": "传说中的url"
            },
            {
                "name":"高速铁路",
                "url": "传说中的url"
            },
            {
                "name":"机器人",
                "url": "传说中的url"
            },
            {
                "name":"无人机",
                "url": "传说中的url"
            },
            {
                "name":"网购",
                "url": "传说中的url"
            },
            {
                "name":"清洁能源",
                "url": "传说中的url"
            },
            {
                "name":"支付宝",
                "url": "传说中的url"
            },
            {
                "name":"针灸",
                "url": "传说中的url"
            }
        ]
    })

@api.route('/article/<int:kind>/', methods=["GET"])
def get_five_article(kind):
    if kind in [1,2,3]:
        articles = Article.query.filter_by(kind=kind).order_by(Article.time.desc()).limit(5)
        return Response(json.dumps([{
            "article_url":article.article_url,
            "title":article.title,
            "date":article.date
            } for article in articles]
        ),mimetype='application/json')

@api.route('/show/', methods=["GET"])
def get_show():
    show = Show.query.order_by(Show.time.desc()).first()
    return jsonify({
        "img_url":show.img_url
    })

@api.route('/carousel/', methods=["GET"])
def get_carousel():
    carousels = Carousel.query.order_by(Carousel.time.desc()).limit(3)
    return Response(json.dumps([{
        "img_url":carousel.img_url,
        "title":carousel.title,
        "article_url":carousel.article_url
        } for carousel in carousels]
    ),mimetype='application/json')

@api.route('/qrcode/', methods=["GET"])
def get_qrcode():
    qrcode = Qrcode.query.order_by(Qrcode.time.desc()).first()
    return jsonify({
        "img_url":qrcode.img_url
        })

@api.route('/word/list', methods=["GET"])
def get_word():
    sort = int(request.args.get('sort'))
    page = int(request.args.get('page'))
    if sort in range(1,13):
        if page>0:
            words = Word.query.filter_by(sort=sort).limit(10).offset((page-1)*10)
        else:
            words = Word.query.filter_by(sort=sort)
        count = Word.query.filter_by(sort=sort).count()
        words_list = [{
                "word_id":w.id,
                "Chinese":w.chinese,
                "Chinese_audio":w.chinese_audio,
                "English":w.english,
                "English_audio":w.english_audio,
                "Russian":w.russian,
                "Russian_audio":w.russian_audio,
                "Arabic":w.arabic,
                "Arabic_audio":w.arabic_audio,
                "German":w.german,
                "German_audio":w.german_audio,
                "video_url":w.video_url
            } for w in words]
        return jsonify({
            "words":words_list,
            "count":count
            })

@api.route('/register/', methods=["POST"])
def register():
    if request.method == 'POST':
        username = request.get_json().get("username")
        password = request.get_json().get("password")
        if not User.query.filter_by(username=username).first():
            user = User(username=username,
                    password=password)
            db.session.add(user)
            db.session.commit()
            user_id=User.query.filter_by(username=username).first().id
            return jsonify({
                "created":user_id
            })

@api.route('/login/', methods=["POST"])
def login():
    username = request.get_json().get("username")
    password = request.get_json().get("password")
    if User.query.filter_by(username=username).first():
        user = User.query.filter_by(username=username).first()
        if user.verify_password(password):
            return jsonify({
                "id":user.id
            })


