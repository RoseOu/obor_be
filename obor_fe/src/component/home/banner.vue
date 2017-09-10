<template>
    <div id="bottom_banner">
        <el-carousel :interval="4000" type="card" height="200px">
            <el-carousel-item v-for="img in banner" :key="item">
                <a :href = "img.article_url"><li class="pic_info">{{img.title}}</li><img :src="img.img_url" id="img"></a>
            </el-carousel-item>
        </el-carousel>
    </div>
</template>
<script>
import 'whatwg-fetch'

export default {
    data() {
            return {
                banner: [],
                ri: 0,
                j: 1
            }

        },
        mounted() {
            fetch('/api/carousel/').then(value => {
                return value.json()
            }).then(value => {
                this.banner = value
            })
        },
        methods: {
            change(i) {
                this.ri += i
                this.j = i
            }
        }

}
</script>
<style scoped>
.el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
}

#bottom_banner {
    display: block;
    width: 68%;
    margin: 120px auto;
    height: auto;
    position: relative;
}

#img {
    display: block;
    width: 100%;
    height: 330px;
}

.pic_info {
    display: block;
    position: absolute;
    bottom: 0px;
    width: 100%;
    height: 30px;
    text-align: center;
    line-height: 30px;
    z-index: 500;
    background: rgba(41, 47, 51, 0.7);
    color: #00bb9c;
}
</style>
