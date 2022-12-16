document.querySelector(".name").addEventListener("keyup", function(){
    this.value = this.value.replace(/[^\d]/g, "");
});