import csv
from flask import Flask, jsonify, request

all_movies = []
with open("movies.csv")as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]

liked = []
disliked = []
did_not_watch = []

app = Flask(__name__)

@app.route("/get-movie")
def get_movie():
    return jsonify({
        "data": all_movies[0],
        "status": "Sucess"
    })

@app.route("/liked-movies", methods = ["POST"])
def liked_movies():
    movies = all_movies[0]
    all_movies = all_movies[1:]
    liked.append(movies)
    return jsonify({
        "status": "Success"
    }), 201

@app.route("/disliked-movies", methods = ["POST"])
def disliked_movies():
    movies = all_movies[0]
    all_movies = all_movies[1:]
    disliked.append(movies)
    return jsonify({
        "status": "Success"
    }), 201

@app.route("/not-watched-movies", methods = ["POST"])
def not_watched_movies():
    movies = all_movies[0]
    all_movies = all_movies[1:]
    did_not_watch.appned(movies)
    return jsonify({
        "status": "Success"
    }), 201

@app.route("/popular_movies")
def popular_movies():
    movie_data = []
    for movie in output:
        _d = {
            "title":movie[0],
            "poster_link": movie[1],
            "release_date" : movie[2] or N/A,
            "duration" : movie[3],
            "rating" : movie[4],
            "overview" : movie[5]
        }
        movie_data.append(_d)

    return jsonify({
        "data" : movie_data
        "status": "Success"
    }), 200

@app.route("/recommended_movies")
def recommended_movies():
    all_recommended = []
    for liked_movie in liked_movies:
        output = get_recomm(liked_movie[19])
        for data in output:
            all_recommended.append(data)
    import itertools
    all_recommended.sort()
    all_recommended = list(all_recommended for all_recommended,_ in itertools.groupby(all_recommended))
    movie_data = []
    for recommended in all_recommended:
        _d = {
            "title":recommended[0],
            "poster_link": recommended[1],
            "release_date" : recommended[2] or N/A,
            "duration" : recommended[3],
            "rating" : recommended[4],
            "overview" : recommended[5]
        }
        movie_data.append(_d)

    return jsonify({
        "data" : movie_data
        "status": "Success"
    }), 200

if __name__ == "__main__":
    app.run()

