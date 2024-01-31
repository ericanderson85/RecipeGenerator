let ingredients = [
    'eggs',
    'milk',
    'butter'
];
let added = [];
const listElement = document.querySelector('#ingredient-list');
const inputElement = document.querySelector('#input');
const addButtonElement = document.querySelector('#add-button');
const ingredientsElement = document.querySelector('#ingredients');
const searchButtonElement = document.querySelector('#search');
const formElement = document.querySelector('#form');

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
}

function filterData(data, searchText) {
    return data.filter((x) => x.includes(searchText.toLowerCase()));
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

inputElement.addEventListener('input', function () {
    loadData(filterData(ingredients, inputElement.value), listElement);
});

inputElement.addEventListener('keyup', function (e) {
    if (inputElement.value.length == 0) {
        listElement.hidden = true;
    } else if (e.key === 'Enter') {
        var lowerValue = this.value.toLowerCase();
        if (ingredients.includes(lowerValue)) {
            addIngredient(lowerValue);
        } else if (filterData(ingredients, lowerValue).length == 1) {
            addIngredient(filterData(ingredients, lowerValue)[0]);
        }
    }
});

listElement.addEventListener('click', function (event) {
    if (event.target && event.target.matches('.list-item')) {
        addIngredient(event.target.textContent);
    }
});

hideSearch();