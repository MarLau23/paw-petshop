let menu = document.querySelector('#menu')

let menu_bar = document.querySelector('#menu-bar')

menu_bar.addEventListener('click', () => {
    menu.classList.toggle('menu-toggle')
})
//se agrega seleccionador de cantidad de productos
const cantidad = document.getElementById("cantidad");
const buttonMas = document.getElementById("button+");
const buttonMenos = document.getElementById("button-");
let items = 0;
function aumentarItem() {
    items++;
    cantidad.textContent = items;
}
function restarItem() {
    if(items > 0) items--;
    cantidad.textContent = items;
}
buttonMas.addEventListener("click", aumentarItem);
buttonMenos.addEventListener("click", restarItem);

