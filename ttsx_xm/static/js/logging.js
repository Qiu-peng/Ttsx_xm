/**
 * Created by python on 17-9-17.
 */
$(function () {
    var $font = $('#acelog span');
  // 悬浮变手
  $font.hover(function() {
  $font.css("cursor","pointer");
  // 禁止复制
  $font.css('-moz-user-select',' none');
  $font.css('-khtml-user-select', 'none');
  $font.css('user-select','none');
  });

    $font.click(function () {

    window.location.href = '/User/login/';

  });
});