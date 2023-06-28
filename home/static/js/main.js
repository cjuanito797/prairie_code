function changeBg() {
  var scrollValue = window.scrollY;

  var navbar = document.getElementById('primary-navigation');
  console.log(scrollValue);

  if (scrollValue < 50) {
    navbar.classList.remove('bgColor');

  }

  else {
    navbar.classList.add('bgColor');
  }

}


window.addEventListener('scroll', changeBg);
