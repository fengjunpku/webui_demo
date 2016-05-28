// 点击变换
//$(document).ready(function(){
    // $("#navbar li").click( 
  // function() {
           //$(this).attr("class","active").siblings().attr("class","null");
       // });
//    });
//terminal
function terRun() {
  //ajax
  $.post('/run',{'cmd':$('#inputCMD').val()},function(data)
  {
    $('#terminal').html(data);
  });
  $('#terminal').scrollTop( $('#terminal')[0].scrollHeight);
}
function scrollDown(){
  $('#terminal').scrollTop($('#terminal')[0].scrollHeight);
}
var autorun;
function autoRun() {
  autorun=self.setInterval("terRun()",1000)
}
function stopRun() {
  $('#terminal').html('Stop<br>')
  window.clearInterval(autorun);
}
//根据url设置标签颜色
function setHeadTag(url){
  url='#'+url;
  $("#navbar li").each(
    function(){
      if($(this).find('a').attr("href")==url)
        $(this).attr("class","active");
      else
        $(this).attr("class","null");
    });
}
//获取url中的参数
function geturlpar(){
  if(window.location.hash){
    var reg = new RegExp("[A-z]+[A-z]");
    var r = window.location.hash.substr(1).match(reg);
    return unescape(r[0]);
  }
  else
    return null;
}
//
var lasturlpar='';
function loading(){
  jump(geturlpar());
  lasturlpar=geturlpar();
}
//
function jump(target){
  //ajax
  $.post('/load',{'page':target},function(data)
  {
    $('.page').html(data);
    //set title
    if(target!=null)
    {
      document.title=target;
      window.location.hash='#'+target;
    }
    else
    {
      window.location.hash='#home';
    }
  });
}
//
window.onhashchange=function(){
  if(geturlpar()!=lasturlpar){
    currentUrl=geturlpar();
    jump(currentUrl);
    setHeadTag(currentUrl)
    lasturlpar=currentUrl;
  }
};