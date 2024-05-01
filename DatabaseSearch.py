from pymongo import MongoClient

def search_objects_by_keyword(database_name, collection_name, keyword):
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')

    # Access the specified database and collection
    db = client[database_name]
    collection = db[collection_name]

    # Search for objects containing the keyword in title
    title_results = collection.find({"title": {"$regex": keyword, "$options": "i"}})
    print("Title results:")
    for result in title_results:
        print(result)


    # Search for objects containing the keyword in ingredients
    """
    ingredients_results = collection.find({"ingredients": {"$regex": keyword, "$options": "i"}})
    print("\nIngredients results:")
    for result in ingredients_results:
        print(result)
    """

    # Search for objects containing the keyword in directions
    """
    directions_results = collection.find({"directions": {"$regex": keyword, "$options": "i"}})
    print("\nDirections results:")
    for result in directions_results:
        print(result)
    """

# Example usage:
search_objects_by_keyword("Recipes", "ALL", "mashed potato")