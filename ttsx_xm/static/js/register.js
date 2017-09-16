$(function(){
	var $userName = $("#user_name");
    var $pwd = $("#pwd");
    var $cpwd = $("#cpwd");
    var $email = $("#email");
    var $allow = $("#allow");


	var error_name = false;
	var error_password = false;
	var error_check_password = false;
	var error_email = false;
	var error_check = true;

	// 数字字母或下划线6到20位
    var reg_name = /^\w{6,20}$/;
    var reg_psw = /^[\w!@#$%^&*]{6,20}$/;
    // 6~18个字符，可使用字母、数字、下划线，需以字母开头
    var reg_email = /^[A-Za-z0-9]\w{4,16}[A-Za-z0-9]@[a-z0-9]+(\.[a-z]{2,5}){1,2}$/i;



	$userName.blur(function() {
		check_user_name();
	});
	$userName.focus(function () {
        //获取焦点 隐藏提示
        $(this).next().hide();
    });

	$pwd.blur(function() {
		check_pwd();
	});
	$pwd.focus(function () {
        //获取焦点 隐藏提示
        $(this).next().hide();
    });

	$cpwd.blur(function() {
		check_cpwd();
	});
	$cpwd.focus(function () {
        //获取焦点 隐藏提示
        $(this).next().hide();
    });

	$email.blur(function() {
		check_email();
	});
	$email.focus(function () {
        //获取焦点 隐藏提示
        $(this).next().hide();
    });
//----------------------------------勾选-------------------
	$allow.click(function() {
		if($(this).is(':checked'))
		{
			error_check = true;
			$(this).siblings('span').hide();
		}
		else
		{
			error_check = false;
			$(this).siblings('span').html('请勾选同意');
			$(this).siblings('span').show();
		}
	});

//----------------------用户名-------------------------------------------------
	function check_user_name(){
		var username = $userName.val();
		if (username == "") {
            $userName.next().html("用户名不能为空").show();
            error_name = false;
            return;
        }
		if(reg_name.test(username))
		{
			$.get('/User/ishere/',{'name': $userName.val()}, function (data) {
				if (data.it) {
                    $userName.next().html('用户名已存在').show();
                    error_name = false;
                }
                else{
					$userName.next().hide();
					error_name = true;
				}
            })
		}
		else
		{
			$userName.next().html('请输入6-20个(字母、数字、_)的用户名')
			$userName.next().show();
			error_name = false;
		}
	}
//---------------------------------------密码---------------------------------
	function check_pwd(){
		var psw = $pwd.val();
		if (psw == "") {
            $pwd.next().html("密码不能为空").show();
            error_password = false;
            return;
        }
		if(reg_psw.test(psw))
		{
			$pwd.next().hide();
			error_password = true;
		}
		else
		{
			$pwd.next().html('密码最少8位，最长20位').show();
			error_password = false;
		}
	}
//----------------------------------------重复密码------------------------------------
	function check_cpwd(){
		var pass = $pwd.val();
		var cpass = $cpwd.val();

		if(pass!=cpass)
		{
			$cpwd.next().html('两次输入的密码不一致').show();
			error_check_password = false;
		}
		else
		{
			$cpwd.next().hide();
			error_check_password = true;
		}

	}
//-----------------------------------------邮箱---------------------------------------
	function check_email(){
		var email = $email.val();
        if (email == "") {
            $email.next().html("邮箱不能为空").show();
            error_email = false;
            return;
        }
		if(reg_email.test(email))
		{
			$email.next().hide();
			error_email = true;
		}
		else
		{
			$email.next().html('你输入的邮箱格式不正确')
			$email.next().show();
			error_email = false;
		}

	}
//--------------------------------------最终提交验证------------------------------
	$('#reg_form').submit(function() {
		check_user_name();
		check_pwd();
		check_cpwd();
		check_email();

		if(error_name && error_password && error_check_password && error_email && error_check)
		{
			return true;
		}
		else
		{
			return false;
		}
	});



})