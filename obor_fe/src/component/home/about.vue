<template>
    <div class="wholeWidth">
        <div class="title">联系我们</div>
        <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="120px" class="demo-ruleForm">
            <el-form-item label="您的姓名" prop="name">
                <el-input v-model="ruleForm.name" class="input1"></el-input>
            </el-form-item>
            <el-form-item label="您的email" prop="email">
                <el-input v-model="ruleForm.name" class="input2"></el-input>
            </el-form-item>
            <el-form-item label="电话号码" prop="phone">
                <el-input v-model="ruleForm.name" class="input3"></el-input>
            </el-form-item>
            <el-form-item label="您的要求" prop="desc">
                <el-input type="textarea" v-model="ruleForm.desc"></el-input>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="submitForm('ruleForm')">立即发送</el-button>
                <el-button @click="resetForm('ruleForm')">重置</el-button>
            </el-form-item>
        </el-form>
        <div>
            <el-card class="box-card">
                <div slot="header" class="clearfix">
                    <span style="line-height: 36px;">联系方式</span>
                </div>
                <div class="text item">
                    Email：996886231@qq.com
                </div>
                <div class="text item">
                    QQ：996886231
                </div>
            </el-card>
        </div>
    </div>
</template>
<script>
export default {
    data() {
        return {
            ruleForm: {
                name: '',
                email: '',
                phone: '',
                desc: ''
            },
            rules: {
                name: [
                    { required: true, message: '请输入活动名称', trigger: 'blur' },
                    { min: 3, max: 5, message: '长度在 3 到 5 个字符', trigger: 'blur' }
                ],
                email: [
                    { required: true, message: '请填写活动形式', trigger: 'blur' }
                ],
                phone: [
                    { required: true, message: '请填写活动形式', trigger: 'blur' }
                ],
                desc: [
                    { required: true, message: '请填写活动形式', trigger: 'blur' }
                ]
            }
        };
    },
    methods: {
        submitForm(formName) {
            this.$refs[formName].validate((valid) => {
                if (valid) {
                    alert('submit!');
                } else {
                    console.log('error submit!!');
                    return false;
                }
            });
        },
        resetForm(formName) {
            this.$refs[formName].resetFields();
        }
    }
}
</script>
<style scoped>
.title {
    font-size: 30px;
    width: 15%;
    margin: 8% auto;
}

.wholeWidth {
    margin: 0 auto;
    width: 90%;
}

.input1 {
    width: 300px;
}

.input2 {
    width: 400px;
}

.input3 {
    width: 500px;
}

.text {
    font-size: 14px;
  }

  .item {
    padding: 18px 0;
  }

  .clearfix:before,
  .clearfix:after {
      display: table;
      content: "";
  }
  .clearfix:after {
      clear: both
  }

  .box-card {
    width: 480px;
    float: right;
  }
</style>