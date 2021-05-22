// globals variable
let c_clrs = 1;
let colors = ['red', 'yellow', ' orange', 'green', 'blue', 'purple', 'brown', 'pink', 'white', 'black'];
let garments = ['pants', 'shirt', ' hat', 'jacket', 'sweater', 'gloves', 'shoes', 'tie', 'scarf', 'shorts'];

// DOM targets def
let addPair = undefined;
let form = document.getElementById('buildPairs');

// events def

// utils
let addSelect = (data) => {
    let select = document.createElement('SELECT');
    select.name = 'color' + c_clrs;

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
    let garmentsSel = addSelect(garments);;
    let colorsSel = addSelect(colors);;

    div.appendChild(garmentsSel);
    div.appendChild(colorsSel);
    form.appendChild(div);
}

let createForm = () => {
    addSelectPair();

    let addPair = document.createElement('BUTTON');
    addPair.innerHTML = 'ADD';
    addPair.addEventListener('click', handleAddPair);
    form.appendChild(addPair);
}

// functionevents
window.onload = () => {
    createForm();
}

let handleAddPair = (event) => {
    event.preventDefault();
    addSelectPair();
}
