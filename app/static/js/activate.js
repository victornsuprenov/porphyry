const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('nav ul');

window.addEventListener('scroll', () => {
  let scrollY = window.pageYOffset;

  sections.forEach(section => {
    const sectionHeight = section.offsetHeight;
    const sectionTop = section.offsetTop - 50; // небольшой запас
    const sectionId = section.getAttribute('id');

    if(scrollY > sectionTop && scrollY <= sectionTop + sectionHeight){
      navLinks.forEach(link => {
        link.classList.remove('active');
        if(link.getAttribute('href') === `#${sectionId}`){
          link.classList.add('active');
        }
      });
    }
  });
});