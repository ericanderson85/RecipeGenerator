const WHITE = "#fcfcfc";
const BEIGE = "#f7e7da";
const RED = "#9B2915";
const BLUE = "#0c496c";

let ingredients = [];
fetch('/static/ingredients.json')
    .then(response => response.json())
    .then(response_data => {
        ingredients = response_data;
    })
    .catch(error => console.error('Error:', error));
let added = [];
const listElement = document.querySelector('#ingredient-list');
const inputElement = document.querySelector('#input');
const addButtonElement = document.querySelector('#add-button');
const ingredientsElement = document.querySelector('#ingredients');
const searchButtonElement = document.querySelector('#search');
const formElement = document.querySelector('#form');
let highlightedIndex = 0;

function loadData(data, element) {
    if (data) {
        listElement.hidden = false;
        element.innerHTML = '';
        var innerElement = '';
        data.forEach((item) => {
            innerElement += `
            <li class='list-item'>${item}</li>`;
        });

        element.innerHTML = innerElement;
    }
    highlightedIndex = 0;
    updateHighlightedIndex(0);
}

function filterData(data, searchText) {
    if (searchText.length === 0) {
        return;
    }
    var searchTextLower = searchText.toLowerCase();
    var filtered = data.filter((x) => x.includes(searchTextLower));
    filtered.sort((a, b) => {
        if ((a.startsWith(searchTextLower) && b.startsWith(searchTextLower)) ||
            (!a.startsWith(searchTextLower) && !b.startsWith(searchTextLower))) {
            return a.localeCompare(b);
        }
        if (a.startsWith(searchTextLower)) {
            return -1;
        }
        return 1;
    });
    return filtered;
}


function addIngredient(ingredient) {
    let newIngredient = document.createElement('p');
    newIngredient.classList.add('ingredient')
    newIngredient.innerHTML = ingredient;
    newIngredient.addEventListener('click', function () {
        removeIngredient(newIngredient);
    });
    ingredientsElement.appendChild(newIngredient);
    ingredients.splice(ingredients.indexOf(ingredient), 1);
    added.push(ingredient);
    if (added.length > 0) {
        showSearch()
    }
    inputElement.value = '';
    listElement.hidden = true;
    if (ingredientsElement.children.length > 28) {
        Array.from(ingredientsElement.children).forEach(resizeSmallest);
    }
    else if (ingredientsElement.children.length > 15) {
        Array.from(ingredientsElement.children).forEach(resize);
    }
}

function resize(item) {
    item.style.fontSize = "1.5vw";
}

function resizeSmallest(item) {
    item.style.fontSize = "1vw";
}

function hideSearch() {
    searchButtonElement.remove();
    inputElement.style.borderTopRightRadius = '40px';
    inputElement.style.borderBottomRightRadius = '40px';
    inputElement.style.borderRight = '.12vw solid var(--dark-brown)';
}

function showSearch() {
    form.appendChild(searchButtonElement);
    inputElement.style.borderTopRightRadius = '0';
    inputElement.style.borderBottomRightRadius = '0';
    inputElement.style.borderRight = 'none';
}

function removeIngredient(ingredient) {
    ingredient.remove();
    var name = ingredient.innerHTML;
    added.splice(added.indexOf(name), 1);
    ingredients.push(name);
    if (added.length === 0) {
        hideSearch();
    }
}

function updateHighlightedIndex(x) {
    var count = listElement.childElementCount
    if (count === 0 || highlightedIndex + x >= count || highlightedIndex + x < 0) {
        return;
    }
    if (x == 0) {
        listElement.children[highlightedIndex].style.backgroundColor = BLUE;
        listElement.children[highlightedIndex].style.color = WHITE;
        return;
    }
    listElement.children[highlightedIndex].style.backgroundColor = WHITE;
    listElement.children[highlightedIndex].style.color = BLUE;
    highlightedIndex += x;
    listElement.children[highlightedIndex].style.backgroundColor = BLUE;
    listElement.children[highlightedIndex].style.color = WHITE;
}

async function send_ingredients() {
    try {
        const response = await fetch('http://127.0.0.1:5000/receive_ingredients', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(added)
        });
        if (response.ok) {
            const html = await response.text();
            document.body.innerHTML = html;
        } else {
            console.error('Server responded with status:', response.status);
        }
    } catch (error) {
        console.error('Error:', error);
    }
}


inputElement.addEventListener('input', function () {
    if (inputElement.value.length == 0) {
        listElement.hidden = true;
    }
    loadData(filterData(ingredients, inputElement.value), listElement);
});



inputElement.addEventListener('keydown', function (e) {
    if (e.key === 'ArrowDown') {
        e.preventDefault();
        updateHighlightedIndex(1);
    } else if (e.key === 'ArrowUp') {
        e.preventDefault();
        updateHighlightedIndex(-1);
    } else if (e.key === 'Enter' && this.value != '') {
        addIngredient(listElement.children[highlightedIndex].innerHTML);
    }
});


listElement.addEventListener('mouseover', function (event) {
    if (event.target && event.target.matches('.list-item')) {
        listElement.children[highlightedIndex].style.backgroundColor = WHITE;
        listElement.children[highlightedIndex].style.color = BLUE;

        event.target.style.backgroundColor = BLUE;
        event.target.style.color = WHITE;
    }
});

listElement.addEventListener('mouseout', function (event) {
    if (event.target && event.target.matches('.list-item')) {
        event.target.style.backgroundColor = WHITE;
        event.target.style.color = BLUE;
    }
    updateHighlightedIndex(0);
});

listElement.addEventListener('click', function (event) {
    if (event.target && event.target.matches('.list-item')) {
        addIngredient(event.target.textContent);
    }
});

formElement.addEventListener('submit', function (e) {
    e.preventDefault();
});

hideSearch();