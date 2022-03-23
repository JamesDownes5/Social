// Slideshow
let slide_index = showSlide(0);

setInterval(() => {
    slide_index = showSlide(slide_index + 1);
}, 10000);

document.getElementById("slide-next").addEventListener("click", () => {
    slide_index = showSlide(slide_index + 1);
});

document.getElementById("slide-prev").addEventListener("click", () => {
    slide_index = showSlide(slide_index - 1);
});

let origin = window.location.origin;
document.querySelectorAll(".slide-text-container").forEach(element => {
    element.addEventListener("click", () => {
        window.location.href = origin + element.getAttribute("data-link");
    });
});

// Search handling
let url = new URL(window.location.href);
let search_field = url.searchParams.get("search");
let sort_field = url.searchParams.get("sort");

if (sort_field) {
    document.querySelector(`form.search-form input[value="${sort_field}"]`).checked = true;
}
if (search_field) {
    document.getElementById("search-body").value = search_field;
    document.querySelector(".search-form").scrollIntoView();
}

// Event links
document.querySelectorAll(".card").forEach(element => {
    element.addEventListener("click", () => {
        window.location.href = origin + element.getAttribute("data-link");
    });
});

function showSlide(n) {
    let slide_index = n;
    let slideshow = document.querySelectorAll(".slideshow");
    if (n >= slideshow.length) {
        slide_index = 0;
    }
    if (n < 0) {
        slide_index = slideshow.length - 1;
    }

    slideshow.forEach(element => {
        element.style.display = "none";
    });
    document.getElementById(`slide${slide_index + 1}`).style.display = "block";

    return slide_index;
}