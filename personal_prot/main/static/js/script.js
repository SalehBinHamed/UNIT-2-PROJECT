function showSection(sectionId) {
  gsap.to('main section', {
    duration: 0.5,
    opacity: 0,
    y: 20,
    onComplete: () => {
      document.querySelectorAll('main section').forEach(section => {
        section.classList.add('hidden');
      });
      const selectedSection = document.getElementById(sectionId);
      selectedSection.classList.remove('hidden');
      gsap.fromTo(selectedSection, { opacity: 0, y: 20 }, { duration: 0.5, opacity: 1, y: 0 });
    }
  });
}



document.addEventListener('DOMContentLoaded', function() {
  const quoteElement = document.querySelector('#quote');
  const text = quoteElement.textContent;
  quoteElement.innerHTML = '';

  // Split text into characters
  text.split('').forEach((char, index) => {
    const span = document.createElement('span');
    span.textContent = char === ' ' ? '\u00A0' : char;  // Handle spaces properly
    span.style.display = 'inline-block';
    span.style.setProperty('--index', index);
    span.classList.add('quote-char');
    quoteElement.appendChild(span);
  });
  // Modern zoom out animation using anime.js
  anime.timeline({loop: false})
    .add({
      targets: '#quote span',
      scale: [2, 1],
      opacity: [0, 1],
      duration: 1000,
      delay: anime.stagger(50),
      easing: 'easeOutExpo',
      complete: function() {
        // After animation completes, set characters to static
        document.querySelectorAll('#quote span').forEach(span => {
          span.style.transform = 'none';
        });
      }
    });

  // Hover effect to make characters zoom out
  document.querySelectorAll('#quote span').forEach(span => {
    span.addEventListener('mouseenter', function() {
      anime({
        targets: span,
        scale: [1, 1.5],
        duration: 300,
        easing: 'easeInOutQuad',
        direction: 'alternate'
      });
    });
  });
});
