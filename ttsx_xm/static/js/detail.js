/**
 * Created by python on 17-9-16.
 */
// {#            设置立即购买点击动画效果#}
$(function () {


// {#            获取按钮绝对坐标#}
            var addLeft = $(".add_cart").offset().left;
            var addTop = $(".add_cart").offset().top;

// {#            获取按钮宽高#}
            var addWidth = $(".add_cart").outerWidth();
            var addHight = $(".add_cart").outerHeight();

// {#            图片初始位置#}
            var mvLeft = addLeft + addWidth/2 - 25;
            var mvTop = addTop + addHight/2 -25;

// {#            获取购物车绝对位置#}
            var carLeft = $(".cart_name").offset().left;
            var carTop = $(".cart_name").offset().top;

// {#            购物车宽高#}
            var mvInCarLeft = carLeft + $(".cart_name").outerWidth()/2 - 25;
            var mvInCarTop = carTop + $(".cart_name").outerHeight()/2 - 25;
// {#            购物车点击事件#}
            $(".add_cart").click(function () {
// {#                图片动画#}
                $(".mv").css({'left':mvLeft,'top':mvTop}).show();
                $(".mv").stop().animate({
                    width:50,
                    height:50,
                    left:mvInCarLeft,
                    top:mvInCarTop,
                },800,'swing',function () {
                    $(".mv").hide();
// {#                    图片消失，数量加上num_show中写的数量#}
//                     $(".goods_count").html(parseInt($(".goods_count").html())+parseInt($(".num_show").val()));
                });
            });

// {#            ajax请求#}
            var counts=$('.num_show').val();
            var goods_id=$('.operate_btn').attr('id');
            $.get('/Cart/add/',{'count':counts,'goodsid':goods_id},function (data) {
            $('.goods_count').text(data.count);
            });
})
