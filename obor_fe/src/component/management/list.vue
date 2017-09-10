<template>
    <div class="height">
        <div class="top">
            <div class="icon verticle"></div>
            <div class="word verticle">管理后台</div>
            <div class="exit" v-on:click = "exit">退出系统</div>
        </div>
        <el-col :span="5" class="height">
            <el-menu default-active="manage" class="el-menu-vertical-demo height" @open="handleOpen" @close="handleClose" router>
                <el-menu-item index="manage"><i class="el-icon-setting"></i>用户管理</el-menu-item>
                <el-menu-item index="2"><i class="el-icon-picture"></i>图片上传</el-menu-item>
                <el-menu-item index="3"><i class="el-icon-upload"></i>二维码修改</el-menu-item>
                <el-menu-item index="4"><i class="el-icon-upload2"></i>视频上传</el-menu-item>
                <el-menu-item index="5"><i class="el-icon-plus"></i>轮播图上传</el-menu-item>
                <el-menu-item index="6"><i class="el-icon-document"></i>添加文章</el-menu-item>
                <el-menu-item index="7"><i class="el-icon-star-on"></i>高新技术图片上传</el-menu-item>
                <el-submenu index="8">
                    <template slot="title"><i class="el-icon-menu"></i>词条管理</template>
                    <el-menu-item-group>
                        <el-menu-item index="1-1">共享单车</el-menu-item>
                        <el-menu-item index="1-2">航天工程</el-menu-item>
                        <el-menu-item index="1-3">北斗导航</el-menu-item>
                        <el-menu-item index="1-4">桥梁建设</el-menu-item>
                        <el-menu-item index="1-5">孔子学院</el-menu-item>
                        <el-menu-item index="1-6">高速铁路</el-menu-item>
                        <el-menu-item index="1-7">机器人</el-menu-item>
                        <el-menu-item index="1-8">无人机</el-menu-item>
                        <el-menu-item index="1-9">网购</el-menu-item>
                        <el-menu-item index="1-10">清洁能源</el-menu-item>
                        <el-menu-item index="1-11">支付宝</el-menu-item>
                        <el-menu-item index="1-12">针灸</el-menu-item>
                    </el-menu-item-group>
                </el-submenu>
            </el-menu>
        </el-col>
        <transition name="el-zoom-in-center">
            <router-view></router-view>
        </transition>
    </div>
</template>
<script>
export default {
    methods: {
        handleOpen(key, keyPath) {
            console.log(key, keyPath);
        },
        handleClose(key, keyPath) {
            console.log(key, keyPath);
        },
        exit(){
        	window.location = "/login"
        }
    }
}
</script>
<style scoped>
.height {
    height: 100%;
}

.top {
    background-color: #2573e8;
    width: 100%;
    color: white;
    height: 62px;
    line-height: 62px;
}

.verticle {
    display: inline-block;
    vertical-align: middle;
}

.icon {
    background-image: url('../../img/logo.png');
    width: 45px;
    height: 45px;
    background-size: 100%;
    background-repeat: no-repeat;
    margin: 0 30px;
}

.word {
    font-size: 20px;
}

.exit {
    float: right;
    margin-right: 30px;
}
</style>
