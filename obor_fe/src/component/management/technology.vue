<template>
    <div class = "erWeiBox">
        <el-input v-model="url_tech" class="itemWidth" placeholder="请输入图片链接"></el-input>
        <el-button class="newButton" v-on:click="uploaderWei">上传图片链接</el-button>
    </div>
</template>
<script>
export default {
    data() {
            return {
                url_tech: ""
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
                fetch("/api/show/add/", {
                    method: 'POST',
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        img_url: this.url_tech
                    })
                }).then((res) => {
                    return res.json()
                }).then(value => {
                    this.url_tech = ""
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
.newButton{
	margin-top: 40px; 
}
</style>