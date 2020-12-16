function addHash(name){

    let collection = document.querySelector('#hashCollection')
    let hashtag = '#' + name
    let badgeClass = 'badge badge-pill badge-light'

    let temp = `<span class=${badgeClass}>
                ${hashtag} </span>`

    collection.innerHTML += temp;
}



