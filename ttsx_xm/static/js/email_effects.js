$(function () {
	var $email = $('#content span');
	// 悬浮变手
	$email.hover(function() {
		$email.css("cursor","pointer");
    /* css style: */
  // 禁止复制
  $email.css('-moz-user-select',' none');
  $email.css('-khtml-user-select', 'none');
  $email.css('user-select','none');


  	});

	var hash1={  
    'qq.com': 'http://mail.qq.com',
    'gmail.com': 'http://mail.google.com',
    'sina.com': 'http://mail.sina.com.cn',
    '163.com': 'http://mail.163.com',
    '126.com': 'http://mail.126.com',
    'yeah.net': 'http://www.yeah.net/',
    'sohu.com': 'http://mail.sohu.com/',
    'tom.com': 'http://mail.tom.com/',
    'sogou.com': 'http://mail.sogou.com/',
    '139.com': 'http://mail.10086.cn/',
    'hotmail.com': 'http://www.hotmail.com',  
    'live.com': 'http://login.live.com/',  
    'live.cn': 'http://login.live.cn/',  
    'live.com.cn': 'http://login.live.com.cn',  
    '189.com': 'http://webmail16.189.cn/webmail/',  
    'yahoo.com.cn': 'http://mail.cn.yahoo.com/',  
    'yahoo.cn': 'http://mail.cn.yahoo.com/',  
    'eyou.com': 'http://www.eyou.com/',  
    '21cn.com': 'http://mail.21cn.com/',  
    '188.com': 'http://www.188.com/',  
    'foxmail.coom': 'http://www.foxmail.com'  
	};  
	// 定义一个全局变量空字符串，写在函数外的变量。
	var $store = "";
	// js写法
  	function myfunc(){
        var url = $("#mail").text().split('@')[1]; 
        // alert(url) 
        // 根据键找对应的值，也就是邮箱首页。
        $store =  hash1[url];
  	}
	myfunc();
	// 点击事件
	$email.click(function () {
		// window.location.href = $store;
		window.location.href = "https://mail.qq.com/";
	});
	$(function () {
	$('#mail').css('display','none');
	});
});
