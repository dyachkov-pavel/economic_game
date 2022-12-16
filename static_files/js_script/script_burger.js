'use strict';
let button = document.getElementById("menu_span"),
    buttonClose = document.getElementById("close_burger"),
    menu = document.getElementById("menu_id_burger");

button.onclick = function (event) {
    /* menu.style.display = "none"; */
    menu.style.cssText = "visibility: hidden; opacity: 0; z-index: -1";
    event.stopPropagation();
};
buttonClose.onclick = function (event) {
    /* menu.style.display = "flex"; */
    menu.style.cssText = "visibility: visible; opacity: 1; z-index: 1";
    event.stopPropagation();
};

/*-------------------------------- JS for menu-burger, use in all pages!!! ------------------------------------------------*/

