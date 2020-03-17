/* cookie get theme value */

//cookie値を連想配列として取得する
function getCookieArray(){
  var cookieArr = new Array();
  if(document.cookie != ''){
    var tmp = document.cookie.split('; ');
    for(var i=0;i<tmp.length;i++){
      var data = tmp[i].split('=');
      cookieArr[data[0]] = decodeURIComponent(data[1]);
    }
  }
  return cookieArr;
}
// Reflect the value of the obtained cookie in the theme.
function readThemeCookie() {
  var cookieArr = getCookieArray();
  var theme = cookieArr["themeName"];
  document.body.classList.add(theme);
}
