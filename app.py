from flask import Flask, jsonify, request,render_template,flash
import requests

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def home():
    return "Welcome user, to this amazing website."

@app.route('/<name>/<int:num>')
def pass_or_fail(name, num):
    # Logic for determining pass/fail status
    if num > 35:
        return f"{name} has passed with a score of {num}."
    else:
        return f"{name} has failed with a score of {num}."

@app.route("/predict", methods=["POST", "GET"])
def predict():
    if request.method == "GET":
        # Fetching data from the external API
        url = "https://cat-fact.herokuapp.com/facts"
        response = requests.get(url)
        data = response.json()
        
        # Returning the list of facts
        return jsonify({"Facts":[data[i]["text"] for i in range(len(data))]})  # Accessing the correct key

    # Handle POST requests (add your logic here if needed)
    else:
        data = request.get_json()
        url = "https://jsonplaceholder.typicode.com/posts"  # Updated to a standard testing API
        response = requests.post(url=url, json=data)
        
        if response.status_code == 201:  # HTTP 201 Created
            response_data = response.json()
            return f"Success: {data['value']} - API is working correctly.", 201
        else:
            return "Error occurred", response.status_code
    

@app.route("/dog_image")
def image():
    response=requests.get("https://dog.ceo/api/breeds/image/random")
    response1=requests.get("https://dogapi.dog/api/v2/facts?limit=50")
    url=response.json()["message"]
    data=response1.json()["data"][0]["attributes"]["body"]
    flash(data)
    
    return render_template("picture.html",url=url)

if __name__ == "__main__":

    app.run(debug=True)
