const img_map = {
    "0": {
        "12 30": "static/quotes/Company_0/12 30.png",
        "13 0": "static/quotes/Company_0/13 0.png",
        "13 30": "static/quotes/Company_0/13 30.png",
        "14 0": "static/quotes/Company_0/14 0.png",
        "14 30": "static/quotes/Company_0/14 30.png",
        "15 0": "static/quotes/Company_0/15 0.png",
        "15 30": "static/quotes/Company_0/15 30.png"
    },
    "1": {
        "12 30": "static/quotes/Company_1/12 30.png",
        "13 0": "static/quotes/Company_1/13 0.png",
        "13 30": "static/quotes/Company_1/13 30.png",
        "14 0": "static/quotes/Company_1/14 0.png",
        "14 30": "static/quotes/Company_1/14 30.png",
        "15 0": "static/quotes/Company_1/15 0.png",
        "15 30": "static/quotes/Company_1/15 30.png"
    },
    "2": {
        "12 30": "static/quotes/Company_2/12 30.png",
        "13 0": "static/quotes/Company_2/13 0.png",
        "13 30": "static/quotes/Company_2/13 30.png",
        "14 0": "static/quotes/Company_2/14 0.png",
        "14 30": "static/quotes/Company_2/14 30.png",
        "15 0": "static/quotes/Company_2/15 0.png",
        "15 30": "static/quotes/Company_2/15 30.png"
    },
    "3": {
        "12 30": "static/quotes/Company_3/12 30.png",
        "13 0": "static/quotes/Company_3/13 0.png",
        "13 30": "static/quotes/Company_3/13 30.png",
        "14 0": "static/quotes/Company_3/14 0.png",
        "14 30": "static/quotes/Company_3/14 30.png",
        "15 0": "static/quotes/Company_3/15 0.png",
        "15 30": "static/quotes/Company_3/15 30.png"
    },
    "4": {
        "12 30": "static/quotes/Company_4/12 30.png",
        "13 0": "static/quotes/Company_4/13 0.png",
        "13 30": "static/quotes/Company_4/13 30.png",
        "14 0": "static/quotes/Company_4/14 0.png",
        "14 30": "static/quotes/Company_4/14 30.png",
        "15 0": "static/quotes/Company_4/15 0.png",
        "15 30": "static/quotes/Company_4/15 30.png"
    },
    "5": {
        "12 30": "static/quotes/Company_5/12 30.png",
        "13 0": "static/quotes/Company_5/13 0.png",
        "13 30": "static/quotes/Company_5/13 30.png",
        "14 0": "static/quotes/Company_5/14 0.png",
        "14 30": "static/quotes/Company_5/14 30.png",
        "15 0": "static/quotes/Company_5/15 0.png",
        "15 30": "static/quotes/Company_5/15 30.png"
    },
    "6": {
        "12 30": "static/quotes/Company_6/12 30.png",
        "13 0": "static/quotes/Company_6/13 0.png",
        "13 30": "static/quotes/Company_6/13 30.png",
        "14 0": "static/quotes/Company_6/14 0.png",
        "14 30": "static/quotes/Company_6/14 30.png",
        "15 0": "static/quotes/Company_6/15 0.png",
        "15 30": "static/quotes/Company_6/15 30.png"
    },
    "7": {
        "12 30": "static/quotes/Company_7/12 30.png",
        "13 0": "static/quotes/Company_7/13 0.png",
        "13 30": "static/quotes/Company_7/13 30.png",
        "14 0": "static/quotes/Company_7/14 0.png",
        "14 30": "static/quotes/Company_7/14 30.png",
        "15 0": "static/quotes/Company_7/15 0.png",
        "15 30": "static/quotes/Company_7/15 30.png"
    },
    "8": {
        "12 30": "static/quotes/Company_8/12 30.png",
        "13 0": "static/quotes/Company_8/13 0.png",
        "13 30": "static/quotes/Company_8/13 30.png",
        "14 0": "static/quotes/Company_8/14 0.png",
        "14 30": "static/quotes/Company_8/14 30.png",
        "15 0": "static/quotes/Company_8/15 0.png",
        "15 30": "static/quotes/Company_8/15 30.png"
    }
};

let stock9 = {
    name: "Jimmy Pitfiger",
    image: "static/quotes/close.png"
};

let stock8 = {
    name: "Greentech",
    image: "static/quotes/close.png"
};

let stock7 = {
    name: "NoisyWeekend",
    image: "static/quotes/close.png"
};

let stock6 = {
    name: "Маковский",
    image: "static/quotes/close.png"
};

let stock5 = {
    name: "РэуФарм",
    image: "static/quotes/close.png"
};

let stock4 = {
    name: "Misisscard",
    image: "static/quotes/close.png"
};

let stock3 = {
    name: "АэроPlov",
    image: "static/quotes/close.png"
};

let stock2 = {
    name: "XXL Group",
    image: "static/quotes/close.png"
};

let stock1 = {
    name: "Moonlight",
    image: "static/quotes/close.png"
};

let dBofSlider = [stock1, stock2, stock3, stock4, stock5, stock6, stock7, stock8, stock9];

var today = new Date();
var hours = today.getHours();
var minutes = today.getMinutes();
var startdate = new Date();
startdate.setHours(12, 30, 0)
var enddate = new Date();
enddate.setHours(16, 0, 0)
console.log(today)

for (let i = 0; i < dBofSlider.length; i++) {
    if (startdate <= today && today < enddate) {
        console.log('V LOPPE')
        if (minutes < 30) {
            console.log('0 min')
            minutes = 0;
        }
        else {
            console.log('30 min')
            minutes = 30;
        }
        var time = hours + " " + minutes;
        console.log(time)
        image_url = img_map[i][time];
        console.log(image_url)
        dBofSlider[i]["image"] = image_url;
        console.log(dBofSlider[i]["image"])
    }
}


let leftButton = document.getElementById("button_left"),
    rightButton = document.getElementById("button_right"),
    imageSlider = document.getAnimations("image_stock");

let textCompany = document.getElementById("text_company");
textCompany.textContent = "" + stock1.name;


let i = 0;

rightButton.onclick = function () {
    i += 1;
    if (i == 1) {
        document.getElementById("image_stock").src = '/' + stock2.image;
        textCompany.textContent = "" + stock2.name;

    }
    if (i == 2) {
        document.getElementById("image_stock").src = '/' + stock3.image;
        textCompany.textContent = "" + stock3.name;
    }
    if (i == 3) {
        document.getElementById("image_stock").src = '/' + stock4.image;
        textCompany.textContent = "" + stock4.name;

    }
    if (i == 4) {
        document.getElementById("image_stock").src = '/' + stock5.image;
        textCompany.textContent = "" + stock5.name;

    }
    if (i == 5) {
        document.getElementById("image_stock").src = '/' + stock6.image;
        textCompany.textContent = "" + stock6.name;

    }
    if (i == 6) {
        document.getElementById("image_stock").src = '/' + stock7.image;
        textCompany.textContent = "" + stock7.name;

    }
    if (i == 7) {
        document.getElementById("image_stock").src = '/' + stock8.image;
        textCompany.textContent = "" + stock8.name;

    }
    if (i == 8) {
        document.getElementById("image_stock").src = '/' + stock9.image;
        textCompany.textContent = "" + stock9.name;

    }
    if (i == 9) {
        document.getElementById("image_stock").src = '/' + stock1.image;
        textCompany.textContent = "" + stock1.name;
        i = 0;
    }
};



leftButton.onclick = function () {
    i -= 1;
    if (i == 0) {
        document.getElementById("image_stock").src = '/' + stock1.image;
        textCompany.textContent = "" + stock1.name;
        i = 9;
    }
    if (i == 1) {
        document.getElementById("image_stock").src = '/' + stock2.image;
        textCompany.textContent = "" + stock2.name;

    }
    if (i == 2) {
        document.getElementById("image_stock").src = '/' + stock3.image;
        textCompany.textContent = "" + stock3.name;
    }
    if (i == 3) {
        document.getElementById("image_stock").src = '/' + stock4.image;
        textCompany.textContent = "" + stock4.name;

    }
    if (i == 4) {
        document.getElementById("image_stock").src = '/' + stock5.image;
        textCompany.textContent = "" + stock5.name;

    }
    if (i == 5) {
        document.getElementById("image_stock").src = '/' + stock6.image;
        textCompany.textContent = "" + stock6.name;

    }
    if (i == 6) {
        document.getElementById("image_stock").src = '/' + stock7.image;
        textCompany.textContent = "" + stock7.name;

    }
    if (i == 7) {
        document.getElementById("image_stock").src = '/' + stock8.image;
        textCompany.textContent = "" + stock8.name;

    }
    if (i == 8) {
        document.getElementById("image_stock").src = '/' + stock9.image;
        textCompany.textContent = "" + stock9.name;

    }
    if (i == 9) {
        document.getElementById("image_stock").src = '/' + stock1.image;
        textCompany.textContent = "" + stock1.name;

    }
};
