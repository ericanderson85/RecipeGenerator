let ingredients = [
    'eggs',
    'milk',
    'butter',
    'salt',
    'pepper',
    'bacon',
    'fish',
    'meat',
    'beef',
    'soy',
    'eggs',
    'milk',
    'butter',
    'salt',
    'pepper',
    'bacon',
    'fish',
    'meat',
    'beef',
    'soy',
    'eggs',
    'milk',
    'butter',
    'salt',
    'pepper',
    'bacon',
    'fish',
    'meat',
    'beef',
    'soy'
];
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
        listElement.children[highlightedIndex].style.backgroundColor = '#EABF9F';
        return;
    }
    listElement.children[highlightedIndex].style.backgroundColor = "#f7f3e8";
    highlightedIndex += x;
    listElement.children[highlightedIndex].style.backgroundColor = '#EABF9F';
}


inputElement.addEventListener('input', function () {
    if (inputElement.value.length == 0) {
        listElement.hidden = true;
    }
    loadData(filterData(ingredients, inputElement.value), listElement);
});



inputElement.addEventListener('keyup', function (e) {
    if (e.key === 'ArrowDown') {
        e.preventDefault();
        updateHighlightedIndex(1);
    } else if (e.key === 'ArrowUp') {
        e.preventDefault();
        updateHighlightedIndex(-1);
    } else if (e.key === 'Enter') {
        addIngredient(listElement.children[highlightedIndex].innerHTML);
    }
});


listElement.addEventListener('mouseover', function (event) {
    if (event.target && event.target.matches('.list-item')) {
        listElement.children[highlightedIndex].style.backgroundColor = "#f7f3e8";
        event.target.style.backgroundColor = '#EABF9F';
    }
});

listElement.addEventListener('mouseout', function (event) {
    if (event.target && event.target.matches('.list-item')) {
        event.target.style.backgroundColor = '#f7f3e8';
    }
    updateHighlightedIndex(0);
});

listElement.addEventListener('click', function (event) {
    if (event.target && event.target.matches('.list-item')) {
        addIngredient(event.target.textContent);
    }
});

hideSearch();