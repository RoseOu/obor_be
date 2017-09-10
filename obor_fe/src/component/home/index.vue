<template>
    <div class="app">
        <div class="titleBox">
        </div>
        <div class="keywordsBox">
            <div class="keywordsTitle"></div>
            <div class="timeline">
                <div class="_timeline">
                    <div class="_dot">
                        <a href="/learn">
                            <div class="keylink">针灸</div>
                            <div class="dot"></div>
                        </a>
                    </div>
                    <div class="_dot a">
                        <a href="/learn">
                            <div class="dot"></div>
                            <div class="keylink">北斗导航</div>
                        </a>
                    </div>
                    <div class="_dot">
                        <a href="/learn">
                            <div class="keylink">航天工程</div>
                            <div class="dot"></div>
                        </a>
                    </div>
                    <div class="_dot a">
                        <a href="/learn">
                            <div class="dot"></div>
                            <div class="keylink">孔子学院</div>
                        </a>
                    </div>
                    <div class="_dot">
                        <a href="/learn">
                            <div class="keylink">网购</div>
                            <div class="dot"></div>
                        </a>
                    </div>
                    <div class="_dot a">
                        <a href="/learn">
                            <div class="dot"></div>
                            <div class="keylink">高速铁路</div>
                        </a>
                    </div>
                    <div class="_dot">
                        <a href="/learn">
                            <div class="keylink">机器人</div>
                            <div class="dot"></div>
                        </a>
                    </div>
                    <div class="_dot a">
                        <a href="/learn">
                            <div class="dot"></div>
                            <div class="keylink">无人机</div>
                        </a>
                    </div>
                    <div class="_dot">
                        <a href="/learn">
                            <div class="keylink">清洁能源</div>
                            <div class="dot"></div>
                        </a>
                    </div>
                    <div class="_dot a">
                        <a href="/learn">
                            <div class="dot"></div>
                            <div class="keylink">支付宝</div>
                        </a>
                    </div>
                    <div class="_dot">
                        <a href="/learn">
                            <div class="keylink">共享单车</div>
                            <div class="dot"></div>
                        </a>
                    </div>
                    <div class="_dot a">
                        <a href="/learn">
                            <div class="dot"></div>
                            <div class="keylink">桥梁制造</div>
                        </a>
                    </div>
                </div>
            </div>
        </div>
        <div class="iconsearchs">
            <div class="iconsearch">
                <div class="icon icon_panel"></div>
                <div class="icondescription"><a href="/learn">进入学习</a></div>
            </div>
            <div class="divid_line"></div>
            <div class="iconsearch">
                <div class="icon icon_video"></div>
                <div class="icondescription"><a href="#">丝路视频</a></div>
            </div>
            <div class="divid_line"></div>
            <div class="_iconsearch">
                <div class="icon icon_story"></div>
                <div class="icondescription"><a href="/login">后台管理</a></div>
            </div>
        </div>
        <iTable></iTable>
        <banner></banner>
        <div class="cpyright">Powered By 华中师范大学计算机学院</div>
        <div class="bottom">
            <div class="link mright">
                <a href="#" class="rlink load">关于我们</a>
                <a href="#" class="rlink">意见反馈</a>
            </div>
            <div class="link">
                <img src="http://www.twword.com/uploads/wiki/93/87/50698_0.jpg" class="erwei">
                <div class="rlink load">下载 APP</div>
            </div>
        </div>
    </div>
</template>
<script>
import Table from './table'
import Banner from './banner'

export default {
    // data() {
    //         return {
    //          banner:[]
    //         }

    //     },
    //     mounted() {
    //         fetch('/api/carousel/').then(value => {
    //             return value.json()
    //         }).then(value => {
    //             this.gaoxin = value
    //         })
    //     },
    components: {
        "iTable": Table,
        "banner": Banner
    },
    methods: {
        toZhen() {
            this.$router.push("1-1")
        }
    }
}
</script>
<style lang="sass" scoped>
.titleBox {
    background-image: url('../../img/titleBox.png');
    background-size: 100%;
    background-repeat: no-repeat;
    width: 100%;
    height: 360px;
}

.keywordsBox {
    margin-top: 60px;
}

.keywordsTitle {
    background-image: url('../../img/keyWordsTitle.png');
    background-size: 100%;
    background-repeat: no-repeat;
    height: 25px;
    width: 32%;
    margin: 0 auto;
}

.timeline {
    background-image: url('../../img/keyword_bg.png');
    background-size: 100%;
    height: 40px;
    width: 60%;
    margin: 145px auto;
    background-repeat: no-repeat;
    background-position: 50% 90%;
}

._timeline {
    margin-left: -20px;
    font-size: 0;
}

._dot {
    vertical-align: top;
    display: inline-block;
    text-align: center;
    margin-top: -19px;
    margin-right: 1.5%;
    font-size: 14px;
}

.keylink {
    border-bottom: 1px solid #00bb9c;
    padding-bottom: 8px;
}

.dot {
    margin: 10px auto;
    vertical-align: middle;
    border-radius: 50%;
    width: 12px;
    height: 12px;
    background-color: #00bb9c;
    display: inline-block;
    border: 13px solid transparent;
    background-clip: padding-box;
    transition: all 0.5s;
    cursor: pointer;
}

.dot:hover {
    border-radius: 50%;
    width: 12px;
    height: 12px;
    margin: 10px auto;
    background-color: #00bb9c;
    border: 13px solid;
    border-color: rgba(205, 239, 233, 0.5);
    background-clip: padding-box;
}

.a {
    margin-top: 4px;
}

.iconsearchs {
    margin: 145px auto;
    width: 700px;
    text-align: center;
}

.iconsearch {
    margin-right: 10%;
    display: inline-block;
    vertical-align: middle;
}

.icon {
    margin: 20px auto;
    background-repeat: no-repeat;
    width: 40px;
    height: 40px;
}

.icondescription a {
    color: #00bb9c;
    font-size: 20px;
    text-align: center;
}

.divid_line {
    margin-right: 10%;
    display: inline-block;
    vertical-align: bottom;
    background-image: url('../../img/dividing_line.png');
    background-size: 100%;
    background-repeat: no-repeat;
    width: 25px;
    height: 84px;
}

._iconsearch {
    display: inline-block;
    vertical-align: middle;
    margin-right: 0px;
}

.icon_panel {
    background-image: url('../../img/icon_panel.png');
}

.icon_video {
    background-image: url('../../img/icon_video.png');
}

.icon_story {
    background-image: url('../../img/icon_story.png');
}

.cpyright {
    display: block;
    height: 25px;
    line-height: 25px;
    text-align: center;
    color: #00bb9c;
}

.bottom {
    width: 100%;
    height: 200px;
    margin-top: 67px;
    text-align: center;
    background-color: #090922;
}

.link {
    display: inline-block;
    vertical-align: middle;
}

.mright {
    margin-right: 350px;
}

.rlink {
    color: #f7f3d6;
    font-size: 20px;
    display: block;
    margin-top: 40px;
}

.erwei {
    margin-top: 20px;
    width: 120px;
    height: 120px;
}

.load {
    margin-top: 20px;
}
</style>
