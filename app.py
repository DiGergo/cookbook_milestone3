import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'recipe_db'
app.config["MONGO_URI"] = 'mongodb+srv://root2019:RooT20i9@myfirstcluster-2yjug.mongodb.net/recipe_db?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/home')
def get_home():
    return render_template("index.html") 


@app.route('/categories')
def get_categories():
    return render_template("categories.html", categories=mongo.db.categories.find())
    
    
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", 
    recipes=mongo.db.recipes.find({'category_name': 'Dessert'}))    


@app.route('/get_desserts')
def get_desserts():
    return render_template("recipes.html", 
    recipes=mongo.db.recipes.find({'category_name': 'Dessert'}))
    
@app.route('/get_fish')
def get_fish():
    return render_template("recipes.html", 
    recipes=mongo.db.recipes.find({'category_name': 'Dessert'}))
    
@app.route('/get_pastas')
def get_pastas():
    return render_template("recipes.html", 
    recipes=mongo.db.recipes.find({'category_name': 'Pasta'}))    
    
    
@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html',
    recipes=mongo.db.recipes.find(),
    categories=mongo.db.categories.find(),
    time_to_prep=mongo.db.time_to_prep.find(),
    cost=mongo.db.cost.find())
    
@app.route('/insert_recipe', methods=['POST'])
def insert_recipes():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))
    
if __name__ == '__main__' :
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

    