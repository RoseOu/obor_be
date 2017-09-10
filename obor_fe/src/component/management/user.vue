<template>
    <div class="control">
        <el-table :data="tableData4" border class="tableWidth">
            <el-table-column prop="id" label="用户编号">
            </el-table-column>
            <el-table-column prop="username" label="用户名">
            </el-table-column>
            <el-table-column label="操作">
                <template scope="scope">
                    <el-button @click.native.prevent="deleteRow(scope.$index, tableData4)" type="text" size="small">
                        移除
                    </el-button>
                </template>
            </el-table-column>
        </el-table>
        <el-form class="userForm">
            <el-input v-model="username" class="itemWidth" placeholder="用户名"></el-input>
            <el-input type="password" v-model="password" class="itemWidth" placeholder="密码"></el-input>
            <div class="userForm">
                <el-button class="newButton" v-on:click="newUser">新增用户</el-button>
            </div>
        </el-form>
    </div>
</template>
<script>
import 'whatwg-fetch'

export default {
    methods: {
        deleteRow(index, rows) {
            fetch("/api/user/delete/", {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    id: rows[index].id
                })
            }).then((res) => {
                return res.json()
            }).then(value => {
                rows.splice(index, 1);
                this.open1()
            })
        },
        open1() {
            this.$message({
                message: '恭喜你，删除成功！',
                type: 'success'
            });
        },
        open2() {
            this.$message({
                message: '恭喜你，增加成功！',
                type: 'success'
            });
        },
        newUser() {
            fetch("/api/user/add/", {
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
                return res.json()
            }).then(value => {
                this.tableData4.push({
                    "username": this.username,
                    "id": value.id
                })
                this.username = ""
                this.password = ""
                this.open2()
            })
        }
    },
    mounted() {
        fetch('/api/user/list/').then(value => {
            return value.json()
        }).then(value => {
            this.tableData4 = value
        })
    },
    data() {
        return {
            tableData4: [],
            username: "",
            password: ""
        }
    }
}
</script>
<style scoped>
.tableWidth {
    width: 70%;
    margin: 50px auto;
}

.itemWidth {
    width: 55%;
    margin: 30px 70px;
}

.newButton {
    float: right;
    margin-top: 20px;
}

.userForm {
    margin-right: 180px;
}
</style>
