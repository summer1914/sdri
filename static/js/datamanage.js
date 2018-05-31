$(function () {
    $("#add-btn").click(function (event) {
        window.location.href="/datamanage/add/";
    });

});


$(function () {
    $("#cancel-btn2").click(function (event) {
        event.preventDefault();
        window.location.href="/datamanage/";
    });

});




$(function () {
    $("#submit-btn2").click(function (event) {
        //event.preventDefault
        //阻止按钮默认的提交表单的事件
        event.preventDefault();
        var schoolNameE = $("input[name=schoolName]");
        var yearE = $("input[name=year]");
        var provinceE = $("input[name=province]");
        var cityE = $("input[name=city]");
        var countyE = $("input[name=county]");
        var sumStuE = $("input[name=sumStu]");
        var schoolPutE = $("input[name=schoolPut]");
        var studentAvgE = $("input[name=studentAvg]");
        var computerSumE = $("input[name=computerSum]");
        var multiClassE = $("input[name=multiClass]");
        var classSumE = $("input[name=classSum]");
        var broadbandE = $("input[name=broadband]");
        var effectPrepareE = $("input[name=effectPrepare]");
        var pertinencePrepareE = $("input[name=pertinencePrepare]");
        var optimizeTeachE = $("input[name=optimizeTeach]");
        var turnoverTeachE = $("input[name=turnoverTeach]");
        var manageCourseE = $("input[name=manageCourse]");
        var communicateCourseE = $("input[name=communicateCourse]");



        var schoolName = schoolNameE.val();
        var year = parseInt(yearE.val());
        var province = provinceE.val();
        var city = cityE.val();
        var county = countyE.val();
        var sumStu = parseInt(sumStuE.val());
        var schoolPut = parseFloat(schoolPutE.val());
        var studentAvg = parseFloat(studentAvgE.val());
        var computerSum = parseInt(computerSumE.val());
        var multiClass = parseInt(multiClassE.val());
        var classSum = parseInt(classSumE.val());
        var broadband = parseFloat(broadbandE.val());
        var effectPrepare = parseFloat(effectPrepareE.val());
        var pertinencePrepare = parseFloat(pertinencePrepareE.val());
        var optimizeTeach = parseFloat(optimizeTeachE.val());
        var turnoverTeach = parseFloat(turnoverTeachE.val());
        var manageCourse = parseFloat(manageCourseE.val());
        var communicateCourse = parseFloat(communicateCourseE.val());



        $.post({
            'url': '/datamanage/add/',
            'data':{
                'schoolName':schoolName,
                'year':year,
                'province':province,
                'city':city,
                'county':county,
                'sumStu':sumStu,
                'schoolPut':schoolPut,
                'studentAvg':studentAvg,
                'computerSum':computerSum,
                'multiClass':multiClass,
                'classSum':classSum,
                'broadband':broadband,
                'effectPrepare':effectPrepare,
                'pertinencePrepare':pertinencePrepare,
                'optimizeTeach':optimizeTeach,
                'turnoverTeach':turnoverTeach,
                'manageCourse':manageCourse,
                'communicateCourse':communicateCourse

            },
            'success':function (data) {
                if(data['code'] == 200){
                    zlalert.alertSuccessToast("恭喜！添加数据成功！");
                    schoolNameE.val("");
                    yearE.val("");
                    provinceE.val("");
                    cityE.val("");
                    countyE.val("");
                    sumStuE.val("");
                    schoolPutE.val("");
                    studentAvgE.val("");
                    computerSumE.val("");
                    multiClassE.val("");
                    classSumE.val("");
                    broadbandE.val("");
                    effectPrepareE.val("");
                    pertinencePrepareE.val("");
                    optimizeTeachE.val("");
                    turnoverTeachE.val("");
                    manageCourseE.val("");
                    communicateCourseE.val("");

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
    $(".delete-data-btn").click(function (event) {
                var self = $(this);
                var tr = self.parent().parent();
                var data_id = tr.attr('data-id');
                zlalert.alertConfirm({
				"confirmText":"确认",
				"cancelText":"取消",
				"msg": "请确认删除数据吗？",
				"confirmCallback": function(){

                       $.post({
                            'url': '/datamanage/delete/',
                            'data':{
                                'data_id':data_id
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






