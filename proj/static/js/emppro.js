function preventBack() {
    window.history.forward();
}
setTimeout("preventBack()", 0);
window.onunload = function() {
    null
};

function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}