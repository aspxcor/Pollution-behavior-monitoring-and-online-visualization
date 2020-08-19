$(function(){

    $("body").on("change","div.chuans input.uploadImg",function(){

        var reads = new FileReader();
        var f = $(this).get(0).files[0];
        var rep = /jpeg|png|gif|bmp/ig;
        var gstyle = f.type.split("/")[1];
        if(rep.test(gstyle)){
            reads.readAsDataURL(f);
            var that = this;
            reads.onload = function(e) {
                $(that).parent().find("img").attr("src",this.result)
            };
        }else{
            layer.msg("图片格式不正确，请上传 jpeg|png|gif|bmp 格式的图片")
        }

    });

    $("body").on("mouseenter","div.chuans",function(){
        var odatasrc = $(this).find("img").data("imgsrc");
        var osrc =  $(this).find("img").attr("src");

        if(osrc.indexOf(odatasrc)==-1){
            $(this).find("span.delx").show();
        }
    });
    $("body").on("mouseleave","div.chuans",function(){
        $(this).find("span.delx").hide();
    });

    $("body").on("click","span.delx",function(){
        var odatasrc = $(this).parents(".chuans").find("img").data("imgsrc");
        var osrc =  $(this).parents(".chuans").find("img").attr("src");
        $(this).parents(".chuans").find("img").attr("src",odatasrc);
        $(this).hide();
        $(this).parents(".chuans").find("input").val("");
    });

    $("body").on("click","span.tibtn",function(){
        var odata = getchuancan();
        console.log(odata);
        if(jiancecanshu()){
            $.ajax({
                type:"post",
                url:otijiourl,
                data:odata,
                dataType: 'json', //返回值类型 一般设置为json
                // contentType: "application/x-www-form-urlencoded; charset=utf-8",
                processData: false,  // jQuery不要去处理发送的数据
                success:function(res){
                    console.log(res);
                },error:function(){
                    console.log("后台处理错误");
                }
            })
        }
    });

    function getchuancan(){
        var formData = new FormData();
        var ojson = {};

        ojson.oshouji =$.trim( $("input.shoujihao").val());

        ojson.ofdji = $("input.fadongjihao").val();
        ojson.ochjiah = $("input.chejiahao").val();

        // ojson.ozhenm = $("input.file1").get(0).files[0];
        // ojson.opfanm = $("input.file2").get(0).files[0];
        // ojson.oshilm = $("input.file3").get(0).files[0];


        ojson.ozhenm = document.querySelector("input.file1").files[0];
        ojson.opfanm = document.querySelector("input.file2").files[0];
        ojson.oshilm = document.querySelector("input.file3").files[0];

        formData.append('oshouji', ojson.oshouji);
        formData.append('ofdji', ojson.ofdji);
        formData.append('ochjiah', ojson.ochjiah);
        formData.append('ozhenm', ojson.ozhenm);
        formData.append('opfanm', ojson.opfanm);
        formData.append('oshilm', ojson.oshilm);


        return ojson;
        return formData;
    }

    function jiancecanshu(){
        var oshouji = $.trim($("input.shoujihao").val());
        var ofdji = $("input.fadongjihao").val();
        var ochjiah = $("input.chejiahao").val();
        var ozhenm = $("input.file1").val();
        var opfanm = $("input.file2").val();
        var oshilm = $("input.file3").val();
        var ocan = 100;



        var canarr = [0,1,2,3,4,5,6];
        if(oshouji.length==0){
            ocan=0;
        }else if(ofdji.length==0){
            ocan=1;
        }else if(ochjiah.length==0){
            ocan=2;
        }else if(ozhenm.length==0){
            ocan=3;
        }else if(opfanm.length==0){
            ocan=4;
        }else if(oshilm.length==0){
            ocan=5;
        }else if(!isPhone(oshouji)){
            ocan=6;
        }

        var arr=[
            "手机号为空，请输入手机号",
            "发动机号为空，请输入发动机号",
            "车架号为空，请输入车架号",
            "身份证正面照为空，请输入身份证正面照",
            "身份证反面照为空，请输入身份证反面照",
            "自拍照为空，请输入自拍照",
            "手机号输入错误，请输入正确的手机号"
        ];

        if(canarr.indexOf(ocan)!=-1){
            console.log("ocan:  "+ocan);
            console.log(arr);
            layer.msg(arr[ocan]);
            return false;
        }else{
            return true;
        }


    }

    //检测手机号码
    function isPhone(phone) {
        if (phone == null || phone == '') {
            // layer.msg('请填写手机号码');
            return false;
        }
        //验证号码
        var phoneReg = /(^1[3|4|5|7|8|9]\d{9}$)|(^09\d{8}$)/ig;
        if (!phoneReg.test(phone)) {
            // layer.msg('请填写正确的手机号码');
            return false;
        } else {
            return true;
        }
    };
})