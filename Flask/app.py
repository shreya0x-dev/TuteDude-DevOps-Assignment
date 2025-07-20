from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config["MONGO_URI"] = "mongodb://localhost:27017/todoDB"
mongo = PyMongo(app)

@app.route('/submittodoitem', methods=['POST'])
def submittodoitem():
    data = request.get_json()
    mongo.db.items.insert_one({
        "name": data["itemName"],
        "description": data["itemDescription"]
    })
    return jsonify({"message": "Item stored!"})

app.run()



'''
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient, errors
app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["DevOps"]
collection = db["ArtGallery"]

@app.route("/", methods=["GET", "POST"])
def gallery_form():
    error = None
    if request.method == "POST":
        art_title = request.form.get("art_title")
        artist_name = request.form.get("artist_name")
        year_created = request.form.get("year_created")
        medium = request.form.get("medium")
        price = request.form.get("price")

        try:
            if not art_title or not artist_name:
                raise ValueError("Artwork title and artist name are required.")
            collection.insert_one({
                "art_title": art_title,
                "artist_name": artist_name,
                "year_created": year_created,
                "medium": medium,
                "price": price
            })
            return redirect(url_for("success"))
        except (errors.PyMongoError, ValueError) as e:
            error = str(e)

    return render_template("gallery_form.html", error=error)

@app.route("/success")
def success():
    return render_template("success.html")



if __name__ == "__main__":
    app.run(debug=True)
'''