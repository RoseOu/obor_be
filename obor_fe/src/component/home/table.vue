<template>
    <div>
        <div class="info_message">
            <div class="info_pic">
                <div class="info">
                    <div class="ti_li">
                        <div class="title_s">
                            <div class="title">
                                <a v-on:click="id = 1;getList()">丝路资讯</a>
                            </div>
                            <div class="title">
                                <a v-on:click="id = 2;getList()">丝路专访</a>
                            </div>
                            <div class="title">
                                <a v-on:click="id = 3;getList()">高新技术</a>
                            </div>
                        </div>
                        <div class="link"><a href="#">MORE >></a></div>
                    </div>
                    <div class="msg">
                        <a class="listM" v-for="li in list" :href="li.article_url">
                            <div class="ltitle">{{li.title}}</div>
                            <div class="ldate">{{li.date}}</div>
                        </a>
                    </div>
                </div>
                <div class="pic">
                    <img src="http://photocdn.sohu.com/20160820/Img465174152.jpeg" alt="毕业照"><img src="http://img1.gtimg.com/news/pics/hv1/245/116/2138/139053275.png"><img class="pho" src="http://img.wezhan.cn/content/sitefiles/61024/images/6921375_NAO机器人.jpeg" alt="毕业照">
                </div>
            </div>
            <div class="message">
                <div class="subtittle"></div>
                <div class="message_bg">
                    <div class="message_box">
                        <img :src="gaoxin.img_url" class="message_img">
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import 'whatwg-fetch'

export default {
    data() {
            return {
                list: [],
                id: 1,
                gaoxin:""
            }
        },
        mounted(){
        	this.getList()
        	fetch('/api/show/').then(value => {
                return value.json()
            }).then(value => {
                this.gaoxin = value
            })
        },
        methods: {
            getList() {
                fetch('/api/article/' + this.id + '/').then(value => {
                    return value.json()
                }).then(value => {
                    this.list = value
                })
            }
        }
}
</script>
<style scoped>
.info_message {
    margin: auto;
    width: 68%;
}

.info_pic {
    width: 50%;
    display: inline-block;
    vertical-align: middle;
}

.info {
    overflow: hidden;
}

.ti_li {
    text-align: center;
    font-size: 0px;
    padding-bottom: 25px;
}

.title_s {
    display: inline-block;
    vertical-align: middle;
    font-size: 0px;
    border-bottom: 1px #00bb9c solid;
    width: 78%;
}

.title {
    line-height: 40px;
    display: inline-block;
    vertical-align: middle;
    cursor: pointer;
    width: 33%;
    text-align: center;
    font-size: 18px;
}

.title:hover {
    border-bottom: 5px #00bb9c solid;
    margin-bottom: -5px;
    line-height: 30px;
}

.pic {
    margin-top: 45px;
    padding: 0px;
}

.pic img {
    width: 30%;
    height: 90px;
    margin-right: 3%;
}

.message_bg {
    background-image: url("../../img/messagebox.png");
    background-size: 100%;
    height: 380px;
    width: 100%;
    margin: 0px auto;
    margin-bottom: -55px;
    background-position-y: 25px;
    position: relative;
    background-repeat: no-repeat;
}

.message_box {
    overflow: hidden;
    position: absolute;
    margin: 52px 15px;
    background-color: #eeeeee;
    width: 90%;
    height: 200px;
    border: 3px solid #00bb9c;
}

.subtittle {
    margin: 25px auto;
    background-image: url("../../img/message.png");
    width: 95%;
    height: 25px;
    background-repeat: no-repeat;
}

.link {
    display: inline-block;
    vertical-align: middle;
    margin-left: 1%;
    font-size: 20px;
}

.message {
    display: inline-block;
    vertical-align: middle;
    margin-left: 9%;
    width: 40%;
}

.message_img {
    width: 100%;
    height: 100%;
}

.ldate {
    float: right;
    margin-top: 20px;
}

.ltitle {
    float: left;
    margin-top: 20px;
}
</style>
