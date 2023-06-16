function changeBg() {
  var scrollValue = window.scrollY;

  var navbar = document.getElementById('nav_brand');

  if (scrollValue < 150) {
    navbar.classList.remove('bgColor');

  }

  else {
    navbar.classList.add('bgColor');
  }

}


window.addEventListener('scroll', changeBg);
