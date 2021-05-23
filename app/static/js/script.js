// globals variable
let nClrs = 0;
let colors = ['red', 'yellow', ' orange', 'green', 'blue', 'purple', 'brown', 'pink', 'white', 'black'];
let garments = ['pants', 'shirt', ' hat', 'jacket', 'sweater', 'gloves', 'shoes', 'tie', 'scarf', 'shorts', 'ak'];

// DOM targets def
let addPair = undefined;
let form = document.getElementById('buildPairs');

// events def

// utils
let addSelect = (data, type) => {
    let select = document.createElement('SELECT');
    select.name = `${type}${nClrs}`;

    data.forEach(e => {
        let opt = document.createElement('OPTION');
        opt.text = e;
        opt.value = e;
        opt.classList.add('option');
        select.appendChild(opt);
    });

    return select;
}

let addSelectPair = () => {
    let div = document.createElement('DIV');
    let garmentsSel = addSelect(garments, 'g');;
    let colorsSel = addSelect(colors, 'c');;

    div.appendChild(garmentsSel);
    div.appendChild(colorsSel);
    form.prepend(div);
}

let createForm = () => {
    addSelectPair();
    nClrs++;

    let addPair = document.createElement('BUTTON');
    addPair.innerHTML = 'ADD';
    addPair.addEventListener('click', handleAddPair);
    form.appendChild(addPair);
}

// functionevents
window.onload = () => {
    if(form){
        createForm();
    }
    draw_man();
}

let handleAddPair = (event) => {
    event.preventDefault();
    addSelectPair();
    nClrs++;
}

let draw_man = (id = "man_canvas", data) =>{
    var c = document.getElementById(id);
    var ctx = c.getContext("2d");
    let offset_y = 100;
    ctx.beginPath();
    ctx.arc(200, 50 + offset_y, 40, 0, 2 * Math.PI);
    ctx.stroke()
    ctx.moveTo(100, 150+ offset_y)
    ctx.lineTo(300, 150+ offset_y)
    ctx.stroke()
    ctx.moveTo(200, 90+ offset_y)
    ctx.lineTo(200, 290+ offset_y)
    ctx.stroke()

    ctx.moveTo(170, 290+ offset_y)
    ctx.lineTo(230, 290+ offset_y)
    ctx.stroke()

    ctx.moveTo(170, 290+ offset_y)
    ctx.lineTo(170, 450+ offset_y)
    ctx.stroke()
    ctx.moveTo(230, 290+ offset_y)
    ctx.lineTo(230, 450+ offset_y)
    ctx.stroke()

}