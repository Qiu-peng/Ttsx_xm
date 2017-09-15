/**
 * Created by python on 17-9-10.
 */

$(function () {

    // 获取所有商品
    var $goodsul = $('.goods_list_td');
    // 循环取出每一个商品
    $.each($goodsul, function () {
        // 取出li 中的内容
        var col05 = $(this).children('li').eq(4).html();
        // 转换为数字类型
        var col5 = parseFloat(col05);

        // 取出li 中的内容
        var col06 = $(this).children('li').eq(5).html();
        // 转换为数字类型
        var col6 = parseFloat(col06);

        // 计算小计金额，并转换成字符串
        var col7 = (col5 * col6).toFixed(2) + '元';
        $(this).children('li').eq(6).html(col7);
    });

    // 商品的总数量
    var num = 0;
    // 总金额
    var total_money = 0;
    // 运费
    var transit = parseFloat($('.transit b').html());

    // 所有商品的数量对应的li
    var $goods_num = $('.col06');
    // console.log(goods_num);
    $.each($goods_num, function () {
        // 当前商品的数量
        var this_num = parseFloat($(this).html());
        // console.log(this_num);
        // 计算商品总数量
        num += this_num;
    });

    // 所有商品金额对应的li
    var $goods_money = $('.col07');
    $.each($goods_money, function () {
        // 当前商品金额
        var this_money = parseFloat($(this).html());
        // 计算商品总金额
        total_money += this_money;
    });
    // 查看变量类型
    // console.log(typeof total_money);

    // 实付款
    var total_pay = total_money + transit;
    // console.log(total_pay);

    // 拼接总金额，加‘元’
    var total = total_money + '元';

    // 拼接实付款，加‘元’
    var pay = total_pay + '元';

    // 修改商品数量
    $('.total_goods_count em').html(num);
    // 修改商品总金额
    $('.total_goods_count b').html(total);
    // 修改实付款
    $('.total_pay b').html(pay);


});