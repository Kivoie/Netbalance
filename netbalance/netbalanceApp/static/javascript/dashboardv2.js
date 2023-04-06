

// add listen events for the buttons
document.getElementById("add").addEventListener("click", () => {
    document.getElementById("remove-card").style.display = "none";
    document.getElementById("add-card").style.display = "block";
});

document.getElementById("remove").addEventListener("click", () => {
    document.getElementById("add-card").style.display = "none";
    document.getElementById("remove-card").style.display = "block";
});

document.getElementById("close-1").addEventListener("click", () => {
    document.getElementById("add-card").style.display = "none";
});

document.getElementById("close-2").addEventListener("click", () => {
    document.getElementById("remove-card").style.display = "none";
});

// Add event listeners to the button
showPasswordButton.addEventListener('mousedown', function() {
  passwordInput.type = 'text';
});

showPasswordButton.addEventListener('mouseup', function() {
  passwordInput.type = 'password';
});

showPasswordButton.addEventListener('mouseout', function() {
  passwordInput.type = 'password';
});


