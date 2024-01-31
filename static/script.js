let ingredients = [
    "eggs",
    "milk",
    "butter"
];
let added = [];
const listElement = document.querySelector("#ingredient-list");
const inputElement = document.querySelector("#input");
const addButtonElement = document.querySelector("#add-button");
const ingredientsElement = document.querySelector("#ingredients");

function loadData(data, element) {
    if (data) {
        listElement.hidden = false;
        element.innerHTML = "";
        let innerElement = "";
        data.forEach((item) => {
            innerElement += `
            <li class="list-item">${item}</li>`;
        });

        element.innerHTML = innerElement;
    }
}

function filterData(data, searchText) {
    return data.filter((x) => x.includes(searchText.toLowerCase()));
}

function addIngredient(ingredient) {
    ingredientsElement.innerHTML += `
    <p class="ingredient">${ingredient}</p>`;
    ingredients.splice(ingredients.indexOf(ingredient), 1);
    added.push(ingredient);
    inputElement.value = "";
    listElement.hidden = true;
}

inputElement.addEventListener("input", function () {
    loadData(filterData(ingredients, inputElement.value), listElement);
});

inputElement.addEventListener("keyup", function (e) {
    if (inputElement.value.length == 0) {
        listElement.hidden = true;
    } else if (e.key === 'Enter') {
        let lowerValue = this.value.toLowerCase();
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