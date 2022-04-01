document.querySelector("#search label[for='id_username']").remove();
document.querySelector("#search #id_username").setAttribute("placeholder", "Search for users...");

document.querySelectorAll(".tablinks").forEach(element => element.addEventListener("click", openTab));

function openTab(e) {
  let tab = document.querySelector(".active");
  tab.classList.remove("active");
  document.getElementById(tab.id.substring(0, tab.id.indexOf("-"))).style.display = "none";

  tab = e.target;
  tab.classList.add("active");
  document.getElementById(tab.id.substring(0, tab.id.indexOf("-"))).style.display = "inherit";
}
