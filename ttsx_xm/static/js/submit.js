/**
 * Created by python on 17-9-15.
 */

// 点击提交订单

$(function () {
    // 获取状态码 以确定最终要跳转的页面
    var statuscode = $('#status').val();
    if(statuscode == '1') {
        $('.popup_con').fadeIn('fast', function () {

            setTimeout(function () {
                $('.popup_con').fadeOut('fast', function () {
                    // 回到首页
                    window.location.href = '/';
                });
            }, 3000)


        });
        }
    else if(statuscode == '2'){

        $('.popup p').html('超过库存量请修改');

        $('.popup_con').fadeIn('fast', function () {

            setTimeout(function () {
                $('.popup_con').fadeOut('fast', function () {
                    // 回到首页
                    window.location.href = '/Cart/cart/';
                });
            }, 3000)
        });
    }
    else {
         $('.popup p').html('超过库存量请修改');
        $('.popup_con').fadeIn('fast', function () {

            setTimeout(function () {
                $('.popup_con').fadeOut('fast', function () {
                    // 回到首页
                    window.location.href = '/Cart/cart/';
                });
            }, 3000)
        });
    }
});



