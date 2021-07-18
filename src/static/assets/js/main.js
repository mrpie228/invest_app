/**
 * Обработка переключения визуального режима
 */
let visualRegime = document.querySelector('.visual-regime');

visualRegime.onclick = function(){
   
    if ( this.getAttribute('data-regime') === "0" ){
        this.setAttribute('data-regime', "1");
        this.classList.add('visual-regime_dark');
    } else {
        this.setAttribute('data-regime', "0");
        this.classList.remove('visual-regime_dark');
    }

}

/*********************************************************************/

let hamburger = document.querySelector('.hamburger');
let sidebar = document.querySelector('.sidebar');
let hide_sidebar = document.querySelector('.hide-sidebar-btn');
let modal_fog = document.querySelector('.modal-fog');

hamburger.onclick = function(){
    sidebar.classList.toggle('sidebar_show-mob');
    modal_fog.classList.toggle('modal-fog_show');
}

hide_sidebar.onclick = function(){
    sidebar.classList.toggle('sidebar_show-mob');
    modal_fog.classList.toggle('modal-fog_show');
}


window.onresize = function(){
    modal_fog.classList.remove('modal-fog_show');
    sidebar.classList.remove('sidebar_show-mob');
}