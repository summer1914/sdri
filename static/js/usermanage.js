$(function () {
    $("#add-btn").click(function (event) {
        window.location.href="/usermanage/add/";
    });

});


$(function () {
    $("#cancel-btn").click(function (event) {
        event.preventDefault();
        window.location.href="/usermanage/";
    });

});




$(function () {
    $("#submit-btn").click(function (event) {
        //event.preventDefault
        //阻止按钮默认的提交表单的事件
        event.preventDefault();
        var usernameE = $("input[name=username]");
        var emailE = $("input[name=email]");
        var passwordE = $("input[name=password]");
        var password2E = $("input[name=password2]");
        var memberE = $("input[type=checkbox]:checked");
        var schoolE = $("input[name=school]");
        var districtE = $("input[name=district]");

        var username = usernameE.val();
        var email = emailE.val();
        var password = passwordE.val();
        var password2 = password2E.val();
        var member = memberE.val();
        var school = schoolE.val();
        var district = districtE.val();

        $.post({
            'url': '/usermanage/add/',
            'data':{
                'username':username,
                'email':email,
                'password':password,
                'password2':password2,
                'member':member,
                'school':school,
                'district':district
            },
            'success':function (data) {
                if(data['code'] == 200){
                    zlalert.alertSuccessToast("恭喜！添加用户成功！");
                    usernameE.val("");
                    emailE.val("");
                    passwordE.val("");
                    password2E.val("");
                    schoolE.val("");
                    districtE.val("");
                    memberE.prop({"checked":false});
                }else {
                    var message = data['message'];
                    zlalert.alertInfo(message);
                }
            },
            'fail':function (error) {
                zlalert.alertNetworkError();


                }

        })
    });


});


$(function () {
    $(".delete-user-btn").click(function (event) {
                var self = $(this);
                var tr = self.parent().parent();
                var user_id = tr.attr('user-id');
                zlalert.alertConfirm({
				"confirmText":"确认",
				"cancelText":"取消",
				"msg": "请确认移除该用户吗？",
				"confirmCallback": function(){

                       $.post({
                            'url': '/usermanage/delete/',
                            'data':{
                                'user_id':user_id
                            },
                            'success':function (data) {
                            if(data['code'] == 200){

                            window.location.reload();
                }else {
                    var message = data['message'];
                    zlalert.alertInfo(message);
                }
            },
            'fail':function (error) {
                zlalert.alertNetworkError();


                }

        })

				}

			});

    });



});