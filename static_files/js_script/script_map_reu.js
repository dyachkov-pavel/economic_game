let firstCorpus = {
    name: "1 корпус",
    zeroFloor : {
        name: "0 этаж",
        image: "static/pictures/picrures_map_reu/1к 0э.svg"    
    },
    firstFloor : {
        name: "1 этаж",
        image: "static/pictures/picrures_map_reu/1к 1э.svg"
    },
    secondFloor : {
        name: "2 этаж",
        image: "static/pictures/picrures_map_reu/1к 2э.svg"
    }
  
};

let thirdCorpus = {
    name: "3 корпус",
    firstFloor : {
        name: "1 этаж",
        text:"Музыкальный синонимайзер - 1к, 40",
        image: "static/pictures/picrures_map_reu/3к 1э.svg"
    },
    secondFloor : {
        name: "2 этаж",
        image: "static/pictures/picrures_map_reu/3к 2э.svg"
    },
    thirdFloor : {
        name: "3 этаж",
        image: "static/pictures/picrures_map_reu/3к 3э.svg"
    },
    fourthFloor : {
        name: "4 этаж",
        image: "static/pictures/picrures_map_reu/3к 4э.svg"
    },
    fifthFloor : {
        name: "5 этаж",
        image: "static/pictures/picrures_map_reu/3к 5э.svg"
    }
};

let sixthCorpus = {
    name: "6 корпус",
    firstFloor : {
        name: "1 этаж",
        image: "static/pictures/picrures_map_reu/6к 1э.svg"
    },
    secondFloor : {
        name: "2 этаж",
        image: "static/pictures/picrures_map_reu/6к 2э.svg"
    }
};


let dBofSlider = [firstCorpus, thirdCorpus, sixthCorpus];

let leftButton = document.getElementById("button_left"),
    rightButton = document.getElementById("button_right"),
    imageSlider = document.getAnimations("image_stock");
    

    let textCorpus = document.getElementById("text_company");
    let textFloor = document.getElementById("text_company_1");
    let textFloor1 = document.getElementById("text_pravil");
    
    textCorpus.textContent = "" +firstCorpus.name;
    textFloor.textContent = "" +firstCorpus.zeroFloor.name;
    
   

let i = 0;

let leftButton1 = document.getElementById("button_left_1"),
    rightButton1 = document.getElementById("button_right_1");

let z = 0;

rightButton.onclick = function () {
    i++;
    if (i == 1) {
        document.getElementById("image_stock").src = '/' + thirdCorpus.firstFloor.image;
        textCorpus.textContent = "" +thirdCorpus.name;
        textFloor.textContent = "" +thirdCorpus.firstFloor.name;    
        textFloor1.textContent = "" +thirdCorpus.firstFloor.text;
        let red = 5;
        if (red == 5){
            rightButton1.onclick = function () {
                z++;
                if (z == 1) {
                    document.getElementById("image_stock").src = '/' + thirdCorpus.firstFloor.image;
                    textFloor.textContent = "" +thirdCorpus.firstFloor.name;

                }
                if (z == 2) {
                    document.getElementById("image_stock").src = '/' + thirdCorpus.secondFloor.image;
                    textFloor.textContent = "" +thirdCorpus.secondFloor.name;
                }
                if (z == 3) {
                    document.getElementById("image_stock").src = '/' + thirdCorpus.thirdFloor.image;
                    textFloor.textContent = "" +thirdCorpus.thirdFloor.name;
                }
                if (z == 4) {
                    document.getElementById("image_stock").src = '/' + thirdCorpus.fourthFloor.image;
                    textFloor.textContent = "" +thirdCorpus.fourthFloor.name;
                }
                if (z == 5) {
                    document.getElementById("image_stock").src = '/' + thirdCorpus.fifthFloor.image;
                    textFloor.textContent = "" +thirdCorpus.fifthFloor.name;
                    z = 0;
                }
                };
             leftButton1.onclick = function () {
                    z++;
                    if (z == 1) {
                        document.getElementById("image_stock").src = '/' + thirdCorpus.firstFloor.image;
                        textFloor.textContent = "" +thirdCorpus.firstFloor.name;
                    }
                    if (z == 2) {
                        document.getElementById("image_stock").src = '/' + thirdCorpus.secondFloor.image;
                        textFloor.textContent = "" +thirdCorpus.secondFloor.name;
                    }
                    if (z == 3) {
                        document.getElementById("image_stock").src = '/' + thirdCorpus.thirdFloor.image;
                        textFloor.textContent = "" +thirdCorpus.thirdFloor.name;
                    }
                    if (z == 4) {
                        document.getElementById("image_stock").src = '/' + thirdCorpus.fourthFloor.image;
                        textFloor.textContent = "" +thirdCorpus.fourthFloor.name;
                    }
                    if (z == 5) {
                        document.getElementById("image_stock").src = '/' + thirdCorpus.fifthFloor.image;
                        textFloor.textContent = "" +thirdCorpus.fifthFloor.name;
                        z = 0;
                    }
                    };
        }
       
    }
    if (i == 2) {
        document.getElementById("image_stock").src = '/' + sixthCorpus.firstFloor.image;
        textCorpus.textContent = "" +sixthCorpus.name;
        textFloor.textContent = "" +sixthCorpus.firstFloor.name;
        let red = 6;
        if (red == 6) { 
            rightButton1.onclick = function () {
            z++;
            if (z == 1) {
                document.getElementById("image_stock").src = '/' + sixthCorpus.firstFloor.image;
                textFloor.textContent = "" +sixthCorpus.firstFloor.name;
            }
            if (z == 2) {
                document.getElementById("image_stock").src = '/' + sixthCorpus.secondFloor.image;
                textFloor.textContent = "" +sixthCorpus.secondFloor.name;
                z = 0;
            }
            };
        leftButton1.onclick = function () {
                z++;
                if (z == 1) {
                    document.getElementById("image_stock").src = '/' + sixthCorpus.firstFloor.image;
                    textFloor.textContent = "" +sixthCorpus.firstFloor.name;
                }
                if (z == 2) {
                    document.getElementById("image_stock").src = '/' + sixthCorpus.secondFloor.image;
                    textFloor.textContent = "" +sixthCorpus.secondFloor.name;
                    z = 0;
                }

                };
    }

    }
    if (i == 3) {
        document.getElementById("image_stock").src = '/' + firstCorpus.zeroFloor.image;
        textCorpus.textContent = "" +firstCorpus.name;
        textFloor.textContent = "" +firstCorpus.zeroFloor.name;
        let red = 8;
    if (red == 8) { 
            rightButton1.onclick = function () {
            z++;
            if (z == 1) {
                document.getElementById("image_stock").src = '/' + firstCorpus.firstFloor.image;
                textFloor.textContent = "" +firstCorpus.firstFloor.name;

            }
            if (z == 2) {
                document.getElementById("image_stock").src = '/' + firstCorpus.secondFloor.image;
                textFloor.textContent = "" +firstCorpus.secondFloor.name;
            }
            if (z == 3) {
                document.getElementById("image_stock").src = '/' + firstCorpus.zeroFloor.image;
                textFloor.textContent = "" +firstCorpus.zeroFloor.name;
                
                z = 0;
            }
            };
        leftButton1.onclick = function () {
                z++;
                if (z == 1) {
                    document.getElementById("image_stock").src = '/' + firstCorpus.firstFloor.image;
                    textFloor.textContent = "" +firstCorpus.firstFloor.name;
                }
                if (z == 2) {
                    document.getElementById("image_stock").src = '/' + firstCorpus.secondFloor.image;
                    textFloor.textContent = "" +firstCorpus.secondFloor.name;
                }
                if (z == 3) {
                    document.getElementById("image_stock").src = '/' + firstCorpus.zeroFloor.image;
                    textFloor.textContent = "" +firstCorpus.zeroFloor.name;
                    z = 0;
                }
                };
    }
    i = 0;
}
};
leftButton.onclick = function () {
    i++;
    if (i == 1) {
        document.getElementById("image_stock").src = '/' + thirdCorpus.firstFloor.image;
        textCorpus.textContent = "" +thirdCorpus.name;
        textFloor.textContent = "" +thirdCorpus.firstFloor.name;    
        let red = 5;
        if (red == 5){
            rightButton1.onclick = function () {
                z++;
                if (z == 1) {
                    document.getElementById("image_stock").src = '/' + thirdCorpus.firstFloor.image;
                    textFloor.textContent = "" +thirdCorpus.firstFloor.name;
                }
                if (z == 2) {
                    document.getElementById("image_stock").src = '/' + thirdCorpus.secondFloor.image;
                    textFloor.textContent = "" +thirdCorpus.secondFloor.name;
                }
                if (z == 3) {
                    document.getElementById("image_stock").src = '/' + thirdCorpus.thirdFloor.image;
                    textFloor.textContent = "" +thirdCorpus.thirdFloor.name;
                }
                if (z == 4) {
                    document.getElementById("image_stock").src = '/' + thirdCorpus.fourthFloor.image;
                    textFloor.textContent = "" +thirdCorpus.fourthFloor.name;
                }
                if (z == 5) {
                    document.getElementById("image_stock").src = '/' + thirdCorpus.fifthFloor.image;
                    textFloor.textContent = "" +thirdCorpus.fifthFloor.name;
                    z = 0;
                }
                };
             leftButton1.onclick = function () {
                    z++;
                    if (z == 1) {
                        document.getElementById("image_stock").src = '/' + thirdCorpus.firstFloor.image;
                        textFloor.textContent = "" +thirdCorpus.firstFloor.name;
                    }
                    if (z == 2) {
                        document.getElementById("image_stock").src = '/' + thirdCorpus.secondFloor.image;
                        textFloor.textContent = "" +thirdCorpus.secondFloor.name;
                    }
                    if (z == 3) {
                        document.getElementById("image_stock").src = '/' + thirdCorpus.thirdFloor.image;
                        textFloor.textContent = "" +thirdCorpus.thirdFloor.name;
                    }
                    if (z == 4) {
                        document.getElementById("image_stock").src = '/' + thirdCorpus.fourthFloor.image;
                        textFloor.textContent = "" +thirdCorpus.fourthFloor.name;
                    }
                    if (z == 5) {
                        document.getElementById("image_stock").src = '/' + thirdCorpus.fifthFloor.image;
                        textFloor.textContent = "" +thirdCorpus.fifthFloor.name;
                        z = 0;
                    }
                    };
        }
       
    }
    if (i == 2) {
        document.getElementById("image_stock").src = '/' + sixthCorpus.firstFloor.image;
        textCorpus.textContent = "" +sixthCorpus.name;
        textFloor.textContent = "" +sixthCorpus.firstFloor.name;
        let red = 6;
        if (red == 6) { 
            rightButton1.onclick = function () {
            z++;
            if (z == 1) {
                document.getElementById("image_stock").src = '/' + sixthCorpus.firstFloor.image;
                textFloor.textContent = "" +sixthCorpus.firstFloor.name;
            }
            if (z == 2) {
                document.getElementById("image_stock").src = '/' + sixthCorpus.secondFloor.image;
                textFloor.textContent = "" +sixthCorpus.secondFloor.name;
                z = 0;
            }
            };
        leftButton1.onclick = function () {
                z++;
                if (z == 1) {
                    document.getElementById("image_stock").src = '/' + sixthCorpus.firstFloor.image;
                    textFloor.textContent = "" +sixthCorpus.firstFloor.name;
                }
                if (z == 2) {
                    document.getElementById("image_stock").src = '/' + sixthCorpus.secondFloor.image;
                    textFloor.textContent = "" +sixthCorpus.secondFloor.name;
                    z = 0;
                }

                };
    }

    }
    if (i == 3) {
        document.getElementById("image_stock").src = '/' + firstCorpus.zeroFloor.image;
        textCorpus.textContent = "" +firstCorpus.name;
        textFloor.textContent = "" +firstCorpus.zeroFloor.name;
        
        let red = 8;
    if (red == 8) { 
            rightButton1.onclick = function () {
            z++;
            if (z == 1) {
                document.getElementById("image_stock").src = '/' + firstCorpus.firstFloor.image;
                textFloor.textContent = "" +firstCorpus.firstFloor.name;
            }
            if (z == 2) {
                document.getElementById("image_stock").src = '/' + firstCorpus.secondFloor.image;
                textFloor.textContent = "" +firstCorpus.secondFloor.name;
            }
            if (z == 3) {
                document.getElementById("image_stock").src = '/' + firstCorpus.zeroFloor.image;
                textFloor.textContent = "" +firstCorpus.zeroFloor.name;
                z = 0;
            }
            };
        leftButton1.onclick = function () {
                z++;
                if (z == 1) {
                    document.getElementById("image_stock").src = '/' + firstCorpus.firstFloor.image;
                    textFloor.textContent = "" +firstCorpus.firstFloor.name;
                }
                if (z == 2) {
                    document.getElementById("image_stock").src = '/' + firstCorpus.secondFloor.image;
                    textFloor.textContent = "" +firstCorpus.secondFloor.name;
                }
                if (z == 3) {
                    document.getElementById("image_stock").src = '/' + firstCorpus.zeroFloor.image;
                    textFloor.textContent = "" +firstCorpus.zeroFloor.name;
                    z = 0;
                }
                };
    }
    i = 0;
}
};