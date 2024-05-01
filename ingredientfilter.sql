/*
// provides a Python interface to the SQLite databases
    import sqlite3
// provides functions to deal with JSON data
    import json

// creates a new table in the database called Ingredients.
CREATE TABLE Ingredients ( 
    // two columns (id and name)
    id INTEGER PRIMARY KEY, 
    name TEXT
);


// reads the json file and stores the data in the json file in the variable called ingredientdata.
with open('ingredients.json') as i:
    ingredientdata = json.load(i)

// sets up a connection to the file called ingredients.db and prepares to manage data with it using a cursor.
connect = sqlite3.connect('ingredients.db')
i = connect.cursor()

// iterates through each ingredient in data and stores the name into Ingredients.
for ingredient in ingredientdata:
    // want to do something with id, not sure yet what to do with it.
    name = ingredient['name']
    i.execute("INSERT INTO Ingredients (name) VALUES")


*/
