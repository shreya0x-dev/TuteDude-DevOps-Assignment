from flask import Flask, request, redirect, url_for, render_template
from pymongo import MongoClient, errors
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

client = MongoClient("mongodb://localhost:27017/")
db = client["DevOps"]
collection = db["ArtGallery"]

@app.route("/", methods=["GET", "POST"])
def gallery_form():
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
        except Exception as e:
            return f"Error: {str(e)}"

    return "Go to http://localhost:3000 to submit form."

@app.route("/success")
def success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)