from dotenv import load_dotenv
from flask import Flask,json,request
from flask_cors import CORS
import google.generativeai as genai
import random
import os

#project_folder = os.path.expanduser('~/mysite')
#load_dotenv(os.path.join(project_folder, '.env'))
load_dotenv()

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key = GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

app = Flask(__name__)
CORS(app)

@app.route("/lottery", methods=['POST'])
def lottery():
    if request.method == 'POST':
        participants_list = request.json["participants"]
        return json.jsonify({"winner":random.randrange(len(participants_list))})

@app.route("/gemini", methods=['POST'])
def gemini():
    if request.method == 'POST':
        message = request.json["message"]
        response = model.generate_content(message)
        return json.jsonify({"response":response.text})

if __name__ == '__main__':
    app.run()