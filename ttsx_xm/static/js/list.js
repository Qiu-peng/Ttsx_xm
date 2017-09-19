/**
 * Created by python on 17-9-16.
 */
$(function () {
// {#            设置立即购买点击动画效果#}
// {#            获取购物车绝对位置#}
                var carLeft = $(".cart_name").offset().left;
                var carTop = $(".cart_name").offset().top;

// {#            购物车宽高#}
                var mvInCarLeft = carLeft + $(".cart_name").outerWidth()/2 - 25;
                var mvInCarTop = carTop + $(".cart_name").outerHeight()/2 - 25;

// {#             购物车图标点击事件#}
            $(".add_goods").click(function () {
// {#                图片动画#}
// {#            获取按钮绝对坐标#}
                var addLeft = $(this).offset().left;
                var addTop = $(this).offset().top;

// {#            获取按钮宽高#}
                var addWidth = $(this).outerWidth();
                var addHight = $(this).outerHeight();

// {#            图片初始位置#}
                var mvLeft = addLeft + addWidth/2 - 25;
                var mvTop = addTop + addHight/2 -25;

// {#                设置图片路径,记得在a标签用一个属性保存图片路径，在这根据属性获取路径#}
                $(".mv img").prop('src','/static/media/'+$(this).attr('title'));
                $(".mv").css({'left':mvLeft,'top':mvTop}).show();
                // 获取图片id
                var goods_id=$(this).parents('li').attr('id');
                $(".mv").stop().animate({
                    width:50,
                    height:50,
                    left:mvInCarLeft,
                    top:mvInCarTop
                },800,'swing',function () {
                    $(".mv").hide();
// {#                    图片消失，数量加一#}
//                     $(".goods_count").html(parseInt($(".goods_count").html())+1);
// {#                ajax请求#}
                    var counts=1;
                    $.get('/Cart/add/',{'count':counts,'goodsid':goods_id},function (data) {
                        $('.goods_count').text(data.count);
                    });

                });


            });
    })