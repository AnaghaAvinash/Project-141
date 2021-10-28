#Importing Flask, jsonify and request into it from flask.
from flask import Flask, jsonify, request
import csv

#Making required lists.
all_articles = []
liked_articles = []
not_liked_articles = []

#Importing 'articles.csv' and reading all the data.
with open("articles.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

#Defining the Flask App
app = Flask(__name__)

#Creating the first GET request to get the first article.
@app.route("/get-article")
def get_article():
    return jsonify({
        "data": all_articles[0],
        "status": "success"
    })

#Creating the second POST request to mark the article as liked. Returning the success response.
@app.route("/liked-article", methods=["POST"])
def liked_article():
    article = all_articles[0]
    liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status": "success"
    }), 201


#Creating the third POST request to mark the article as not liked. Returning the success response.
@app.route("/unliked-article", methods=["POST"])
def unliked_article():
    article = all_articles[0]
    not_liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status": "success"
    }), 201

#Defining the Flask App
if __name__ == "__main__":
    app.run()