const faq = document.querySelectorAll(".FAQ");
faq.forEach((FAQ) => {
    FAQ.addEventListener("click", () => {
        FAQ.classList.toggle("active");
    });
});