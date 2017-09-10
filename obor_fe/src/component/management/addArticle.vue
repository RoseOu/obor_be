<template>
    <div class="erWeiBox">
        <el-select v-model="value4" clearable placeholder="请选择">
            <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value">
            </el-option>
        </el-select>
        <el-input v-model="title" class="itemWidth" placeholder="请输入文章标题"></el-input>
        <el-input v-model="article_url" class="itemWidth" placeholder="请输入文章链接"></el-input>
        <el-input v-model="date" class="itemWidth" placeholder="请输入文章发布日期"></el-input>
        <el-button class="newButton" v-on:click="uploaderWei">添加文章</el-button>
    </div>
</template>
<script>
export default {
    data() {
            return {
                date: "",
                title: "",
                article_url: "",
                options: [{
                    value: '1',
                    label: '丝路资讯'
                }, {
                    value: '2',
                    label: '丝路专访'
                }, {
                    value: '3',
                    label: '高新技术'
                }],
                value4: ''
            }

        },
        methods: {
            open2() {
                this.$message({
                    message: '恭喜你，文章添加成功！',
                    type: 'success'
                });
            },
            uploaderWei() {
                fetch("/api/article/add/", {
                    method: 'POST',
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        kind:this.value4,
                        date: this.date,
                        title: this.title,
                        article_url: this.article_url
                    })
                }).then((res) => {
                    return res.json()
                }).then(value => {
                    this.value4 = ""
                    this.date = ""
                    this.title = ""
                    this.article_url = ""
                    this.open2()
                })
            }
        }
}
</script>
<style scoped>
.erWeiBox {
    margin-left: 20%;
    margin-top: 10%;
    padding: 10%;
}

.newButton,
.itemWidth {
    margin-top: 40px;
}
</style>
