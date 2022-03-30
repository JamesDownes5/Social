document.getElementById("event-img").style.height = document.getElementById("event-container").offsetHeight + "px";

let url = new URL(window.location.href);
let is_interested = url.searchParams.get("interested");

if (is_interested == "on") {
    document.getElementById("interested").checked = false;
    document.getElementById("interest-button").textContent = "Interested Registered"
}

document.getElementById("copy-button").addEventListener("click", () => {
    console.log("hey");
    var inputc = document.body.appendChild(document.createElement("input"));
    inputc.value = window.location.href;
    inputc.focus();
    inputc.select();
    document.execCommand('copy');
    inputc.parentNode.removeChild(inputc);
    alert("URL Copied.");
});
