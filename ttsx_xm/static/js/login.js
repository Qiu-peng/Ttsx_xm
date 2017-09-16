$(function () {
    //存用户名
    $.get('/User/readName/', function (data) {// {list:[...]}
        var list = data.lname;  // []
        var rename = $('.rename');
        $.each(list, function (i, n) {
            rename.append('<div class="op">' + n + '</div>');
        });

    });
    var p=0;
    //判断密码匹配,跳转
    $('.input_submit').click(function () {
        $.post('/User/toLogin/', {'name': $('.name_input').val()}, function (data) {//{}
            var upwd = $('.pass_input').val();
            var shapwd =$.sha1(upwd);
            if (data.pwd == shapwd) {
                $.post('/User/toindex/', {'name': $('.name_input').val(),'ischeck':$(".Remember").prop("checked"),'pwd': upwd}, function () {
                    window.location.href = '/';
                });
            }
            else if(data.pwd == 'notValid'){
                $('.pass_input').val('');
                $('.btn_error').html('当前账号不可用').show();
                p +=1;
                }
            else if(data.pwd == 'notExists'){
                $('.pass_input').val('');
                $('.btn_error').html('用户名不存在').show();
                p +=1;
                }
            else if(data.pwd == 'notActive'){
                $('.pass_input').val('');
                $('.active_error').show();
                var timer = setInterval(func, 1000);
                var i = 3;
                func();
                function func() {
                    $('.active_error span').html(i--)
                    if (i ==  0){
                        clearInterval(timer)
                    }
                }
                var uid = data.uid;
                var url = 'http://127.0.0.1:8000/User/send'+uid;
                window.location.href = url;
            }
            else {
                $('.pass_input').val('');
                $('.btn_error').html('用户名或密码错误,请重试!').show();
                p +=1;
            }
            if(p>=3){
                p=0;
                $('.yzm').css('display','block');
            }
        });
        // 验证码是否可见
        var display =$(".yzm").css('display');
        if(display !='none'){
            // 禁用btn属性
            $(".input_submit").attr("disabled", true);
        }

    });


    //焦点,隐藏
    $('.pass_input').focus(function () {
        $('.btn_error').hide(); // 提示文字隐藏
    });
    // 监听键盘事件 (这里是监听回车的抬起)
    $(document).keyup(function (event) {
        if (event.keyCode == 13) {
            $('.input_submit').click();
        }
    });
    // 双击
    $('.name_input').dblclick(function () {
        $('.rename').show();
        $('.op').show();
    });
    // 监听键盘事件 (这里是监听Tab的切换)
    $(document).keyup(function (event) {
        if (event.keyCode == 9) {
            $('.rename').hide();
        }
    });
    // 移开输入框
    $('.name_input').mouseout(function () {
        $('.form_input').delegate(".op", "mouseenter", function () {
            $('.rename').show();
            $('.op').show();
        });
        //　移开
        $('.form_input').delegate(".op", "mouseout", function () {
            $('.rename').hide();
        });
        $('.rename').hide();
    });
    //　点击
    $('.rename').delegate(".op", "click", function () {
        var name = $(this).html();
        $('.name_input').val(name);
        $('.rename').hide();
        // 判断是否有session
        $.post('/User/remember/',{'name':$('.name_input').val()},function (data) {
            var pwd =data.repwd //　密文
            if(pwd){
                $(".Remember").prop("checked",true);
                $('.pass_input').val(pwd)
            }else {
                $('.pass_input').val('')
            }
        });

    });

    $(".Remember").click(function () {
        var ischecked = $(".Remember").prop("checked");
        if(ischecked==0){
            $.post('/User/clearSession/', function (data) {
                var type =data.type
                if(type ==0){
                    $('.pass_input').val('')
                }
            });
        };
    });

    $('.img').click(function () {
        // 切换验证码
        $('.img').attr('src', $(".img").attr('src')+'?1');
    });
    $('.yzm_btn').click(function () {
        $.post('/User/yzm/',{'yzm':$('.yzm_input').val()},function (data) {
            var ret =data.ret;
            if(ret == true){
                $('.tishi').html("输入正确").css('color', 'green');
                $('.yzm').delay(500).css('display','none');
                $('.yzm_input').val("");
                $(".input_submit").attr("disabled", false);
            }else {
                $('.tishi').html("输入有误");
                $('.yzm_input').val("");
                $('.img').click();
            }

        });

    });



});