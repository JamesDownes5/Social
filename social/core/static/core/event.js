document.getElementById("event-img").style.height = document.getElementById("event-container").offsetHeight + "px";

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
