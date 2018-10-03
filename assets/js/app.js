const firebaseRef= firebase.database().ref().child('arcade-characters');

     
clickableGrid = ( rows, cols, callback ) => {
    let i=0;
    const grid = document.querySelector('.grid')
    for (let r=0;r<rows;++r){
        const tr = grid.appendChild(document.createElement('tr'));
        for (let c=0;c<cols;++c){
            const cell = tr.appendChild(document.createElement('td'));
            cell.value = ++i;
            //Lampen
            if (cell.value === 3 || cell.value === 6 || cell.value === 35 || cell.value === 38) {
                cell.classList.add("lamp-off")
            }
            //Stopcontacten
            if (cell.value === 25 || cell.value === 32 || cell.value === 60 || cell.value === 61) {
                cell.classList.add("plug-off")
            }
            //Deuren
            if (cell.value === 41 || cell.value === 49 || cell.value === 57 || cell.value === 48 || cell.value === 56 || cell.value === 64) {
                cell.classList.add("door-closed")
            }
            cell.addEventListener('click',((el,r,c,i) => {
                return () => {
                    callback(el,r,c,i);
                }
            })(cell,r,c,i),false);
        }
    }
    return grid;
}

const grid = clickableGrid(8,8,(el,row,col,i) => {
    //Lampen aanzetten/doven
    if (i === 3 || i === 6 || i === 35 || i === 38) {
        el.classList.toggle("lamp-on")
    }
    //
    if (i === 25 || i === 32 || i === 60 || i === 61) {
        el.classList.toggle("plug-on")
    }
    if (i === 41 || i === 49 || i === 57) {
        const elements = document.querySelectorAll('td')
        elements[40].classList.toggle("door-open")
        elements[48].classList.toggle("door-open")
        elements[56].classList.toggle("door-open")
    }
    if (i === 48 || i === 56 || i === 64 ) {
        const elements = document.querySelectorAll('td')
        elements[47].classList.toggle("door-open")
        elements[55].classList.toggle("door-open")
        elements[63].classList.toggle("door-open")
    }
});

const saveButton = document.querySelector('.save');


saveButton.addEventListener('click', () => {
    let pattern = [];
    
    let cols = document.querySelector('.grid').getElementsByTagName('td'), colslen = cols.length, i = -1;
    while(++i < colslen){
        if(cols[i].classList.contains("clicked")) {
            pattern.push([255,0,0])
        } else {
            pattern.push([0,0,0])
        }
    }
    firebaseRef.push(pattern)
})