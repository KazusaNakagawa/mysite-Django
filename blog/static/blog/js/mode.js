// チェックボックスの取得
const btn = document.querySelector("#btn-mode");

// チェックした時の挙動
btn.addEventListener("change", () => {
  if (btn.checked == true) {
    // ダークモード
    document.body.classList.remove("light-theme");
    var dark_theme = document.body.classList.add("dark-theme");
  } else {
    // ライトモード
    document.body.classList.remove("dark-theme");
    document.body.classList.add("light-theme");
  }
  setCookie();

});

// cookie保存
function setCookie() {
  myCookieVal = $('body').hasClass('dark-theme')? 'dark-theme':'light-theme';
  $.cookie('myCookieName', myCookieVal, { expires: 365, path: '/' })
}