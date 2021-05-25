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
    let garmentsSel = addSelect(garments, 'g');
    let colorsSel = addSelect(colors, 'c');

    div.appendChild(garmentsSel);
    div.appendChild(colorsSel);
    form.insertBefore(div, form.childNodes[nClrs].nextSibling);
}

let createForm = () => {
    addSelectPair();
    nClrs++;
    
    addPair = document.getElementById('addPairButton');
    addPair.addEventListener('click', handleAddPair);
}

// functionevents
window.onload = () => {
    if(form){
        createForm();
    }
}

let handleAddPair = (event) => {
    event.preventDefault();
    addSelectPair();
    nClrs++;
}