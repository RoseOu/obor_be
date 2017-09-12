#coding:utf-8

import json
import time
from flask import jsonify,request,Response
from . import api
from .. import db
from ..models import Word,Article,Show,Carousel,Qrcode,User

@api.route('/admin/login/', methods=["POST"])
def admin_login():
    username = request.get_json().get("username")
    password = request.get_json().get("password")
    if User.query.filter_by(role_id=3).filter_by(username=username).first():
        user = User.query.filter_by(role_id=3).filter_by(username=username).first()
        if user.verify_password(password):
            return jsonify({
                "id":user.id
                })

@api.route('/user/add/', methods=["POST"])
def add_user():
    username = request.get_json().get("username")
    password = request.get_json().get("password")
    if not User.query.filter_by(username=username).first():
        user = User(username=username,
                password=password)
        db.session.add(user)
        db.session.commit()
        user_id=User.query.filter_by(username=username).first().id
        return jsonify({
            "id":user_id
        })

@api.route('/user/delete/', methods=["DELETE"])
def delete_user():
    user_id = request.get_json().get("id")
    user = User.query.filter_by(id=user_id).first()
    db.session.delete(user)
    db.session.commit()
    return jsonify({
        "deleted":user_id
        })

@api.route('/user/list/', methods=["GET"])
def get_users():
    users = User.query.filter_by(role_id=1).all()
    return Response(json.dumps([{
        "username":u.username,
        "id":u.id
        } for u in users]
    ),mimetype='application/json')

@api.route('/word/add/', methods=["POST"])
def add_word():
    word = Word()
    sort = request.get_json().get("sort")
    if sort in range(1,13):
        word.sort = sort
        if request.get_json().get("Chinese") != "":
            word.chinese = request.get_json().get("Chinese")
        if request.get_json().get("Chinese_audio") != "":
            word.chinese_audio = request.get_json().get("Chinese_audio")
        if request.get_json().get("English") != "":
            word.english = request.get_json().get("English")
        if request.get_json().get("English_audio") != "":
            word.english_audio = request.get_json().get("English_audio")
        if request.get_json().get("Russian") != "":
            word.russian = request.get_json().get("Russian")
        if request.get_json().get("Russian_audio") != "":
            word.russian_audio = request.get_json().get("Russian_audio")
        if request.get_json().get("Arabic") != "":
            word.arabic = request.get_json().get("Arabic")
        if request.get_json().get("Arabic_audio") != "":
            word.arabic_audio = request.get_json().get("Arabic_audio")
        if request.get_json().get("German") != "":
            word.german = request.get_json().get("German")
        if request.get_json().get("German_audio") != "":
            word.german_audio = request.get_json().get("German_audio")
        if request.get_json().get("video_url") != "":
            word.video_url = request.get_json().get("video_url")
        db.session.add(word)
        db.session.commit()
        return jsonify({
            "added":word.id
            })

@api.route('/word/delete/', methods=["DELETE"])
def delete_word():
    word_id = request.get_json().get("word_id")
    word = Word.query.filter_by(id=word_id).first()
    db.session.delete(word)
    db.session.commit()
    return jsonify({
        "deleted":word_id
        })
@api.route('/article/list', methods=["GET"])
def get_articles():
    kind = int(request.args.get('kind'))
    page = int(request.args.get('page'))
    if kind in [1,2,3]:
        articles = Article.query.filter_by(kind=kind).limit(10).offset((page-1)*10)
        count = Article.query.filter_by(kind=kind).count()
        articles_list = [{
            "title":a.title,
            "date":a.date,
            "article_url":a.article_url
        } for a in articles]
        return jsonify({
            "articles":articles_list,
            "count":count
            })

@api.route('/article/add/', methods=["POST"])
def add_article():
    kind = request.get_json().get("kind")
    title = request.get_json().get("title")
    date = request.get_json().get("date")
    article_url = request.get_json().get("article_url")
    if kind in [1,2,3]:
        article = Article(kind=kind,title=title,
                          date=date,article_url=article_url)
        db.session.add(article)
        db.session.commit()
        return jsonify({
            "added":article.id
            })

@api.route('/article/delete/', methods=["DELETE"])
def delete_article():
    article_id = request.get_json().get("article_id")
    article = Article.query.filter_by(id=article_id).first()
    db.session.delete(article)
    db.session.commit()
    return jsonify({
        "deleted":article_id
        })

@api.route('/show/add/', methods=["POST"])
def add_show():
    img_url = request.get_json().get("img_url")
    show = Show(img_url=img_url)
    db.session.add(show)
    db.session.commit()
    return jsonify({
        "added":show.id
        })

@api.route('/carousel/list', methods=["GET"])
def get_carousels():
    page = int(request.args.get('page'))
    carousels = Carousel.query.limit(10).offset((page-1)*10)
    count = Carousel.query.count()
    carousels_list = [{
        "carousel_id":c.id,
        "title":c.title,
        "img_url":c.img_url,
        "article_url":c.article_url
        } for c in carousels]
    return jsonify({
        "carousels":carousels_list,
        "count":count
        })

@api.route('/carousel/add/', methods=["POST"])
def add_carousel():
    img_url = request.get_json().get("img_url")
    title = request.get_json().get("title")
    article_url = request.get_json().get("article_url")
    carousel = Carousel(img_url=img_url, title=title,
                        article_url=article_url)
    db.session.add(carousel)
    db.session.commit()
    return jsonify({
        "added":carousel.id
        })

@api.route('/carousel/delete/', methods=["DELETE"])
def delete_carousel():
    carousel_id = request.get_json().get("carousel_id")
    carousel = Carousel.query.filter_by(id=carousel_id).first()
    db.session.delete(carousel)
    db.session.commit()
    return jsonify({
        "deleted": carousel_id
        })

@api.route('/qrcode/', methods=["POST"])
def qrcode():
    img_url = request.get_json().get("img_url")
    qrcode = Qrcode(img_url=img_url)
    db.session.add(qrcode)
    db.session.commit()
    return jsonify({
        "status":200
        })

@api.route('/upload/img/', methods=["POST"])
def upload_img():
    UPLOAD_FOLDER='../img'
    ALLOWED_EXTENSIONS=set(['png','jpg','jpeg','svg'])
    file = request.files['file']
    if file and ('.' in file.filename and file.filename.split('.',1)[1] in ALLOWED_EXTENSIONS):
        fname = '.'.join([str(int(time.time())),file.filename.split('.',1)[1]])
        file.save(os.path.join(UPLOAD_FOLDER,fname))
        pic_url = os.path.join('http://120.24.4.254:8822/',UPLOAD_FOLDER,fname)
        return jsonify({
            "pic_url":pic_url
        })
