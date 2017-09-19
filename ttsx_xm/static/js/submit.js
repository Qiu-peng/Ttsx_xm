/**
 * Created by python on 17-9-15.
 */

// 点击提交订单

$(function () {
    // 获取状态码 以确定最终要跳转的页面
    var statuscode = $('#status').val();
    // 商品id
    var gid = parseInt($('#gid').val());
    var timeleft = 100;

    function timing(path) {
        //改变显示的时间值
        $('#count').html(timeleft);
        //时间值减1
        timeleft--;
        //当时间值为0时，跳转
        // console.log(path);
        if (timeleft < 1) {
            location.href = path;
        }
    }
    // 回到首页 或者回到订单中心
    if (statuscode == '1') {
        $('.popup_con').show(function () {

            $('.popup h4 a').prop('href','/');
            timing('/');
            // 每一秒执行一次函数
            setInterval(function () {
                timing('/');
            }, 1000);

        });
    }
    // 回到立即购买页面
    else if (statuscode == '2') {
        $('.buy').hide();
        $('.popup').css({'height':'150'});
        $('.popup p').html('超过库存量请修改!');
        var url = '/Goods/'+gid+'/';
        console.log(url);
        $('.popup h4 a').prop('href',url);
        $('.popup_con').show(function () {

            timing(url);
            // 每一秒执行一次函数
            setInterval(function () {
                timing(url);
            }, 1000);


        });
    }
    // 回到购物车页面
    else {
         $('.buy').hide();
        $('.popup').css({'height':'150'});
        $('.popup p').html('超过库存量请修改!');
        $('.popup h4 a').prop('href','/Cart/cart/');
        $('.popup_con').show(function () {

            timing('/Cart/cart/');
            // 每一秒执行一次函数
            setInterval(function () {
                timing('/Cart/cart/');
            }, 1000);
        });
    }
});



