/**
 * Created by Administrator on 2016/12/17.
 */

$(function () {
    $('.nav-sidebar>li>a').click(function (event) {
        var that = $(this);
        if(that.children('a').attr('href') == '#'){
            event.preventDefault();
        }
        if(that.parent().hasClass('unfold')){
            that.parent().removeClass('unfold');
        }else{
            that.parent().addClass('unfold').siblings().removeClass('unfold');
        }
        console.log('coming....');
    });

    $('.nav-sidebar a').mouseleave(function () {
        $(this).css('text-decoration','none');
    });
});


$(function () {
    var url = window.location.href;
    if(url.indexOf('profile') >= 0){
        var profileLi = $('.profile-li');
        profileLi.addClass('unfold').siblings().removeClass('unfold');
        profileLi.children('.subnav').children().eq(0).addClass('active').siblings().removeClass('active');
    } else if(url.indexOf('resetpwd') >= 0){
        var profileLi = $('.profile-li');
        profileLi.addClass('unfold').siblings().removeClass('unfold');
        profileLi.children('.subnav').children().eq(1).addClass('active').siblings().removeClass('active');
    }else if(url.indexOf('resetemail') >= 0){
        var profileLi = $('.profile-li');
        profileLi.addClass('unfold').siblings().removeClass('unfold');
        profileLi.children('.subnav').children().eq(2).addClass('active').siblings().removeClass('active');
    } else if(url.indexOf('schooldata') >= 0){
        var postManageLi = $('.school-data');
        postManageLi.addClass('unfold').siblings().removeClass('unfold');
    }else if(url.indexOf('schoolrank') >= 0){
        var postManageLi = $('.post-manage');
        postManageLi.addClass('unfold').siblings().removeClass('unfold');
    }else if(url.indexOf('schoolsearch') >= 0){
        var schooldata = $('.comments-manage');
        schooldata.addClass('unfold').siblings().removeClass('unfold');
    }else if(url.indexOf('schoolreport') >= 0){
        var permissionManageLi = $('.board-manage');
        permissionManageLi.addClass('unfold').siblings().removeClass('unfold');
    } else if(url.indexOf('datamanage') >= 0){
        var userManageLi = $('.user-manage');
        userManageLi.addClass('unfold').siblings().removeClass('unfold');
    }else if(url.indexOf('manual') >= 0){
        var cmsuserManageLi = $('.cmsuser-manage');
        cmsuserManageLi.addClass('unfold').siblings().removeClass('unfold');
    }else if(url.indexOf('usermanage') >= 0){
        var cmsroleManageLi = $('.cmsrole-manage');
        cmsroleManageLi.addClass('unfold').siblings().removeClass('unfold');
    }else if(url.indexOf('comments') >= 0) {
        var commentsManageLi = $('.comments-manage');
        commentsManageLi.addClass('unfold').siblings().removeClass('unfold');
    }
});