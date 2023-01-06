// add arrows to the side of the database headers to sort the database by that value
let arrow = document.querySelector('.arrow');
arrow.addEventListener('click', function() {
  arrow.classList.toggle('reversed');
});