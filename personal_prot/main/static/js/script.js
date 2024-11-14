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