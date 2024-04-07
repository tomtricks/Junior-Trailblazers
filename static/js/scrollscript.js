window.onload = function(){
const buttonRight = document.getElementById('slideRight');
const buttonLeft = document.getElementById('slideLeft');
// const buttonRight = document.getElementsByClassName('slideRight');
// const buttonLeft = document.getElementsByClassName('slideLeft');




buttonRight.onclick = function () {
  document.getElementById('rowscroll').scrollLeft += 300;
  console.log("Button")
};
buttonLeft.onclick = function () {
  document.getElementById('rowscroll').scrollLeft -= 300;
};

}