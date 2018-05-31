$(function () {
    $("#captcha-btn").click(function (event) {
        event.preventDefault();
        var email = $("input[name='email']").val();
        if(!email.match(/^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+((\.[a-zA-Z0-9_-]{2,3}){1,2})$/)){
            zlalert.alertInfoToast('请输入正确邮箱格式');
            return;
        }

        $.get({
            'url':'/email_captcha/',
            'data':{
                'email':email
            },
            'success':function (data) {
                if (data['code'] == 200){
                    zlalert.alertSuccessToast('邮件发送成功!请注意查收');
                }else{
                    zlalert.alertInfo(data['message']);
                }
            },
            'fail':function (error) {
                zlalert.alertNetworkError();
            }
        });
    });
    
    
});


$(function () {
    $("#submit").click(function (event) {
        event.preventDefault();
        var emailE = $("input[name='email']");
        var captchaE = $("input[name='captcha']");

        var email = emailE.val();
        var captcha = captchaE.val();

        if(!email.match(/^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+((\.[a-zA-Z0-9_-]{2,3}){1,2})$/) || !captcha){
            zlalert.alertInfoToast('请输入邮箱或验证码');
            return;
        }

        $.post({
            'url': '/resetemail/',
            'data':{
                'email':email,
                'captcha':captcha
            },
            'success':function (data) {
                if(data['code'] == 200){
                    emailE.val("");
                    captchaE.val("");
                    zlalert.alertSuccessToast('恭喜！邮箱修改成功!');

                }else{
                    zlalert.alertInfo(data['message']);

                }

            },
            'fail':function (error) {
                zlalert.alertNetworkError();

            }
        });

    });
});