$(function () {
    $("#search-btn").click(function (event) {
        event.preventDefault();
        var provinceE = $("input[name=province]");
        var cityE = $("input[name=city]");
        var countyE = $("input[name=county]");
        var schoolE = $("input[name=school]");
        var province = provinceE.val();
        var city = cityE.val();
        var county = countyE.val();
        var school = schoolE.val();
        if (!province&&!city&&!county&&!school){
            zlalert.alertInfoToast('请输入有效信息！');
            return;
        }

        $.get({
            'url':'/schoolsearch/',
            'data':{
                'province':province,
                'city':city,
                'county':county,
                'school':school
            },
            'success':function (data) {
                if (data['code'] == 200){
                    // zlalert.alertSuccessToast('邮件发送成功!请注意查收');
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