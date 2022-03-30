const imageInput = document.querySelector("#image_input");
console.log(imageInput);
var uploaded_image = "";

imageInput.addEventListener("change", function(){
    const reader = new FileReader();
    reader.addEventListener("load", () => {
        uploadedImage = reader.result;
        document.querySelector("#displayI=_image").style.backgroundImage = 'url(${uploaded_image})';
    });
    reader.readAsDataURL(this.files[0]);
})

function openTab(evt, tabName) {
      // Declare all variables
      var i, tabcontent, tablinks;

      // Get all elements with class="tabcontent" and hide them
      tabcontent = document.getElementsByClassName("tabcontent");
      for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
      }

      // Get all elements with class="tablinks" and remove the class "active"
      tablinks = document.getElementsByClassName("tablinks");
      for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
      }

      // Show the current tab, and add an "active" class to the button that opened the tab
      document.getElementById(tabName).style.display = "block";
      evt.currentTarget.className += " active";

      //Show Friends Tab by default
      document.getElementById("defaultOpen").click();

      tablinks = document.getElementsByClassName("tablink");
      for (i = 0; i < x.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" w3-red", "");
      }
    }
