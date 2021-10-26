(function(){
    const btneliminar = document.querySelectorAll(".btneliminar");

btneliminar.forEach(btn=>{
    btn.addEventListener('click',(e)=>{
        const confirma = confirm("Confirma a exclusão?");
        if(!confirma){
            e.preventDefault();
        }
    });
});
})();