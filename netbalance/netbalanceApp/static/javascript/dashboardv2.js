// add listen events for the buttons
document.getElementById("add").addEventListener("click", () => {
    document.getElementById("remove-card").style.display = "none";
    document.getElementById("upload-card").style.display = "none";
    document.getElementById("add-card").style.display = "block";
});

document.getElementById("remove").addEventListener("click", () => {
    document.getElementById("upload-card").style.display = "none";
    document.getElementById("add-card").style.display = "none";
    document.getElementById("remove-card").style.display = "block";
});

document.getElementById("upload").addEventListener("click", () => {
    document.getElementById("remove-card").style.display = "none";
    document.getElementById("add-card").style.display = "none";
    document.getElementById("upload-card").style.display = "block";
});

document.getElementById("close-1").addEventListener("click", () => {
    document.getElementById("add-card").style.display = "none";
});

document.getElementById("close-2").addEventListener("click", () => {
    document.getElementById("remove-card").style.display = "none";
});

document.getElementById("close-3").addEventListener("click", () => {
    document.getElementById("upload-card").style.display = "none";
});