<template>
    <div>
        <div class="card">
            <div class="icon"></div>
            <el-input v-model="username" class="itemWidth" placeholder="用户名"></el-input>
            <el-input type="password" v-model="password" class="itemWidth" placeholder="密码"></el-input>
            <div class="userForm">
                <el-button class="newButton" v-on:click="newUser">登录</el-button>
            </div>
        </div>
    </div>
</template>
<script>
import 'whatwg-fetch'
export default{
	data(){
		return{

		}
	},
	methods:{
		newUser() {
            fetch("/api/admin/login/", {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    username: this.username,
                    password: this.password
                })
            }).then((res) => {
            	if(res.ok)
                	return res.json()
                else
                	this.open()
            }).then(value => {
                this.username = ""
                this.password = ""
                window.location = "/manage"
            })
        },
        open() {
            this.$message.error('密码错了哦！');
        },
	}
}
</script>
<style scoped>
.card{
	background-color: #f0f5f8;
	position: absolute;
	top: 50%;
	left: 50%;
	transform: translate(-50%,-50%);
	padding: 2%;
}
.icon {
    background-image: url('../../img/logo.png');
    width: 60px;
    height: 60px;
    background-size: 100%;
    background-repeat: no-repeat;
    margin: 0 auto;
}
.itemWidth{
	margin-top: 20px;
}
.newButton{
	margin: 20px auto;
	width: 100%;
	background-color: #1f90e6;
	color: white;
}
.userForm{
	text-align: center;
}
</style>
