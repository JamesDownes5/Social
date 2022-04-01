// Event links
document.querySelectorAll(".card").forEach(element => {
    element.addEventListener("click", e => {
        if (!e.target.classList.contains("tag")) {
            window.location.href = origin + element.getAttribute("data-link");            
        }
    });
});

document.querySelectorAll(".tag").forEach(tag => tag.addEventListener("click", e => {
    window.location.href = window.location.origin + "?search=" + e.target.textContent.replace("#", "%23");
}));