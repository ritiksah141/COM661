from flask import Flask, jsonify, make_response, request

app = Flask(__name__)

# --- Hard-coded dataset ---
businesses = [
    {
        "id": 1,
        "name": "Spice Route Kerala",
        "town": "Kochi",
        "rating": 5,
        "reviews": []
    },
    {
        "id": 2,
        "name": "Punjab Tandoori House",
        "town": "Lahore",
        "rating": 4,
        "reviews": []
    },
    {
        "id": 3,
        "name": "Dhaka Street Biryani",
        "town": "Dhaka",
        "rating": 4,
        "reviews": []
    },
    {
        "id": 4,
        "name": "Kathmandu Momo Corner",
        "town": "Kathmandu",
        "rating": 5,
        "reviews": []
    }
]

# GET /api/v1.0/businesses
# Return the entire collection of businesses 
@app.route("/api/v1.0/businesses", methods=["GET"])
def show_all_businesses():
    return make_response(jsonify(businesses), 200)


# GET /api/v1.0/businesses/<id>
# Return a single business by its id 
@app.route("/api/v1.0/businesses/<int:id>", methods=["GET"])
def show_one_business(id):
    for business in businesses:
        if business["id"] == id:
            break
    return make_response(jsonify(business), 200)


# POST /api/v1.0/businesses
# Add a new business 
@app.route("/api/v1.0/businesses", methods=["POST"])
def add_business():
    next_id = businesses[-1]["id"] + 1
    print(next_id)
    new_business = {
        "id": next_id,
        "name": request.form["name"],
        "town": request.form["town"],
        "rating": request.form["rating"],
        "reviews": []
    }
    businesses.append(new_business)
    return make_response(jsonify(new_business), 201)


# PUT /api/v1.0/businesses/<id>
# Edit an existing business 
@app.route("/api/v1.0/businesses/<int:id>", methods=["PUT"])
def edit_business(id):
    for business in businesses:
        if business["id"] == id:
            business["name"] = request.form["name"]
            business["town"] = request.form["town"]
            business["rating"] = request.form["rating"]
            break
    return make_response(jsonify(business), 200)


# DELETE /api/v1.0/businesses/<id>
# Delete an existing business (BE03 3.2.4)
@app.route("/api/v1.0/businesses/<int:id>", methods=["DELETE"])
def delete_business(id):
    for business in businesses:
        if business["id"] == id:
            businesses.remove(business)
            break
    return make_response(jsonify({}), 200)


# GET /api/v1.0/businesses/<id>/reviews
# Return all reviews for a business 
@app.route("/api/v1.0/businesses/<int:id>/reviews", methods=["GET"])
def fetch_all_reviews(id):
    for business in businesses:
        if business["id"] == id:
            break
    return make_response(jsonify(business["reviews"]), 200)


# POST /api/v1.0/businesses/<b_id>/reviews
# Add a review to a business (BE03 3.3)
@app.route("/api/v1.0/businesses/<int:b_id>/reviews", methods=["POST"])
def add_new_review(b_id):
    for business in businesses:
        if business["id"] == b_id:
            if len(business["reviews"]) == 0:
                new_review_id = 1
            else:
                new_review_id = business["reviews"][-1]["id"] + 1

            new_review = {
                "id": new_review_id,
                "username": request.form["username"],
                "comment": request.form["comment"],
                "stars": request.form["stars"]
            }
            business["reviews"].append(new_review)
            break
    return make_response(jsonify(new_review), 201)


# GET /api/v1.0/businesses/<b_id>/reviews/<r_id>
# Fetch one review for one business 
@app.route("/api/v1.0/businesses/<int:b_id>/reviews/<int:r_id>", methods=["GET"])
def fetch_one_review(b_id, r_id):
    for business in businesses:
        if business["id"] == b_id:
            for review in business["reviews"]:
                if review["id"] == r_id:
                    break
            break
    return make_response(jsonify(review), 200)


# PUT /api/v1.0/businesses/<b_id>/reviews/<r_id>
# Edit a specific review (BE03 3.3)
@app.route("/api/v1.0/businesses/<int:b_id>/reviews/<int:r_id>", methods=["PUT"])
def edit_review(b_id, r_id):
    for business in businesses:
        if business["id"] == b_id:
            for review in business["reviews"]:
                if review["id"] == r_id:
                    review["username"] = request.form["username"]
                    review["comment"] = request.form["comment"]
                    review["stars"] = request.form["stars"]
                    break
            break
    return make_response(jsonify(review), 200)


# DELETE /api/v1.0/businesses/<b_id>/reviews/<r_id>
# Delete a specific review (BE03 3.3)
@app.route("/api/v1.0/businesses/<int:b_id>/reviews/<int:r_id>", methods=["DELETE"])
def delete_review(b_id, r_id):
    for business in businesses:
        if business["id"] == b_id:
            for review in business["reviews"]:
                if review["id"] == r_id:
                    business["reviews"].remove(review)
                    break
            break
    return make_response(jsonify({}), 200)


# -------------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True, port=5001)