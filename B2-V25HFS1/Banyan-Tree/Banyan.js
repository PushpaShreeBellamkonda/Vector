// while scrolling the webpage the space above nav bar is removed when scroll is morethan 80px

window.addEventListener("scroll", function () {
    const navbar = document.querySelector(".c1-nav");

    if (window.scrollY > 80) {   // when we scroll
        navbar.classList.add("sticky");
    } else {
        navbar.classList.remove("sticky");
    }
});