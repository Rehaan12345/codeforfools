// Adding the active class to the buttons that have already been clicked: 
const navLink = document.querySelectorAll(".navlink ");
navLink.forEach(navLink => {
    navLink.addEventListener("click", () => {
        document.querySelector(".active")?.classList.remove("active");
        navLink.classList.add("active");
    });
}); 

// Doing some animation on scrolling for the main home page:
const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        console.log(entry)
        if (entry.isInteresecting) {
            entry.target.classList.add("animate-show");
        } else {
            entry.target.classList.remove("animate-show");
        }
    });
});

const animatehidden = document.querySelectorAll(".animate-hidden");
animatehidden.forEach((el) => observer.observe(el));