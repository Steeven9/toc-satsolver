// globals variable
let c_clrs = 1;
let colors = ['red', 'yellow', ' orange', 'green', 'blue', 'purple', 'brown', 'pink', 'white', 'black'];

// DOM targets def
let addPair = undefined;
let form = document.getElementById('buildPairs');

// events def

// utils

let addSelectColor = () => {
    let select = document.createElement('SELECT');
    select.name = 'color' + c_clrs;

    colors.forEach(e => {
        let opt = document.createElement('OPTION');
        opt.text = e;
        opt.value = e;
        opt.class = 'option'
        select.appendChild(opt);
    });

    form.appendChild(select);
}

// functionevents
window.onload = () => {
    addSelectColor();

    let addPair = document.createElement('BUTTON');
    addPair.innerHTML = 'ADD';
    addPair.addEventListener('click', handleAddPair);
    form.appendChild(addPair);
}

let handleAddPair = (event) => {
    event.preventDefault();
    addSelectColor();
}
