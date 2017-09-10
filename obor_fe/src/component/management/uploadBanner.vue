<template>
    <div class = "erWeiBox">
        <el-input v-model="img_url" class="itemWidth" placeholder="请输入图片链接"></el-input>
        <el-input v-model="title" class="itemWidth" placeholder="请输入文章标题"></el-input>
        <el-input v-model="article_url" class="itemWidth" placeholder="请输入文章链接"></el-input>
        <el-button class="newButton" v-on:click="uploaderWei">上传轮播图</el-button>
    </div>
</template>
<script>
export default {
    data() {
            return {
                img_url: "",
                title:"",
                article_url:""
            }

        },
        methods: {
            open2() {
                this.$message({
                    message: '恭喜你，图片上传成功！',
                    type: 'success'
                });
            },
            uploaderWei() {
                fetch("/api/carousel/add/", {
                    method: 'POST',
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        img_url: this.img_url,
                        title:this.title,
                        article_url:this.article_url
                    })
                }).then((res) => {
                    return res.json()
                }).then(value => {
                    this.img_url = ""
                    this.title = ""
                    this.article_url = ""
                    this.open2()
                })
            }
        }
}
</script>
<style scoped>
.erWeiBox{
	margin-left: 20%;
	margin-top: 10%;
	padding: 10%;
}
.newButton,.itemWidth{
	margin-top: 40px; 
}
</style>