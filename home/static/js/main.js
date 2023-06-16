function changeBg() {
  var scrollValue = window.scrollY;

  var navbar = document.getElementById('nav_brand');
  var navbar2 = document.getElementById('navbar_main');

  if (scrollValue < 150) {
    navbar.classList.remove('bgColor');
    navbar2.classList.remove('bgColor');

  }

  else {
    navbar.classList.add('bgColor');
    navbar2.classList.add('bgColor');
  }

}


window.addEventListener('scroll', changeBg);
