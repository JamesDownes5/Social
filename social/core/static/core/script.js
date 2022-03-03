const imageInput = document.querySelector("#image_input");
var uploaded_image = "";

imageInput.addEventListener("change", function(){
    const reader = new FileReader();
    reader.addEventListener("load", () => {
        uploadedImage = reader.result;
        document.querySelector("#displayI=_image").style.backgroundImage = 'url(${uploaded_image})';
    });
    reader.readAsDataURL(this.files[0]);
})