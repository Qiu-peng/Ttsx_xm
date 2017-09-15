/**
 * Created by python on 17-9-15.
 */

// 点击提交订单

$(function () {
    // 获取状态码 以确定最终要跳转的页面
    var statuscode = $('#status').val();
    var timeleft = 5;

    function timing(path) {
        //改变显示的时间值
        $('#count').html(timeleft);
        //时间值减1
        timeleft--;
        //当时间值为0时，跳转
        if (timeleft < 1) {
            window.location.href = path;
        }
    }

    if (statuscode == '1') {
        $('.popup_con').show(function () {

            timing('/');
            // 每一秒执行一次函数
            setInterval(function () {
                timing('/');
            }, 1000);

        });
    }
    // 回到立即购买页面
    else if (statuscode == '2') {

        $('.popup p').html('超过库存量请修改!');

        $('.popup_con').show(function () {

            timing('/Cart/cart/');
            // 每一秒执行一次函数
            setInterval(function () {
                timing('/Cart/cart/');
            }, 1000);


        });
    }
    // 回到购物车
    else {
        $('.popup p').html('超过库存量请修改!');
        $('.popup_con').show(function () {

            timing('/Cart/cart/');
            // 每一秒执行一次函数
            setInterval(function () {
                timing('/Cart/cart/');
            }, 1000);
        });
    }
});



