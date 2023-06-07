//Scrolldownchangecolor
window.addEventListener('scroll', function() {
    var scrollPosition = window.scrollY;
    var navbar = document.querySelector('nav');
  
    if (scrollPosition >= navbar.offsetHeight) {
      navbar.classList.add('fixed-nav');
    } else {
      navbar.classList.remove('fixed-nav');
    }
  });

//stars for products
document.addEventListener('DOMContentLoaded', () => {
  const productRatings = document.querySelectorAll('.product-rating');
  
  productRatings.forEach(rating => {
    const stars = rating.querySelectorAll('i');
    const productId = rating.getAttribute('data-product-id');

    stars.forEach(star => {
      star.addEventListener('click', () => {
        stars.forEach(s => {
          s.classList.remove('fas');
          s.classList.add('far');
        });
        for (let i = 1; i <= star.getAttribute('data-star'); i++) {
          stars[i - 1].classList.remove('far');
          stars[i - 1].classList.add('fas');
        }
      });
    });
  });
});
  


    