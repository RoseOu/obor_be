<template>
    <div class = "uploadPicBox">
        <el-upload action = "/api/upload/img/" list-type="picture-card" :on-preview="handlePictureCardPreview" :on-remove="handleRemove" :on-success = "getFile">
            <i class="el-icon-plus"></i>
        </el-upload>
        <el-dialog v-model="dialogVisible" size="tiny">
            <img width="100%" :src="dialogImageUrl">
        </el-dialog>
        <el-input v-model = "pic_url" class = "url" placeholder = "链接在此 ((^∀^*))"></el-input>
    </div>
</template>
<script>
export default {
    data() {
            return {
                dialogImageUrl: '',
                dialogVisible: false,
                pic_url:""
            };
        },
        methods: {
            handleRemove(file, fileList) {
                console.log(file, fileList);
            },
            handlePictureCardPreview(file) {
                this.dialogImageUrl = file.url;
                this.dialogVisible = true;
            },
            getFile(res){
               this.pic_url = res.img_url
            }
        }
}
</script>
<style scoped>
.url{
	width: 60%;
	margin-top: 40px;
}
.uploadPicBox{
	padding: 90px;
	margin-left: 20%;
}
</style>
