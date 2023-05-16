console.log("I am being called")

document.addEventListener('DOMContentLoaded', function () {

    let replaceButton = document.getElementById("replace-button");
    replaceButton.addEventListener('click', displayFileLoader());

    function displayFileLoader() {
        let originalImage = document.getElementById("original-image");
        let imageInput= document.getElementById("file-uploader");
        
        originalImage.classList.add("hide");
        imageInput.classList.remove("hide");

    }
});