document.getElementById("event-img").style.height = document.getElementById("event-container").offsetHeight + "px";

let url = new URL(window.location.href);
let is_interested = url.searchParams.get("interested");

if (is_interested == "on") {
    document.getElementById("interested").checked = false;
    document.getElementById("interest-button").textContent = "Interested Registered"
}

document.querySelectorAll(".tag").forEach(tag => tag.addEventListener("click", e => {
    window.location.href = window.location.origin + "?search=" + e.target.textContent.substring(e.target.textContent.indexOf(" ") + 1)
}));

document.getElementById("copy-button").addEventListener("click", () => {
    console.log("hey");
    var inputc = document.body.appendChild(document.createElement("input"));
    let href = window.location.href;
    inputc.value = href.substring(0, href.indexOf("?"));
    inputc.focus();
    inputc.select();
    document.execCommand('copy');
    inputc.parentNode.removeChild(inputc);
    alert("URL Copied.");
});
