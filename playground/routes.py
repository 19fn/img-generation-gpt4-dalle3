from playground import app
from flask import render_template, request
from .openai import chatCompletions, imgGeneration
import base64

@app.route("/", methods=["GET", "POST"])
def index_page():
    return render_template("home.html")

@app.route("/gpt4", methods=["GET", "POST"])
def gpt_page():
    response = None
    if request.method == 'POST':
        user_input = request.form['content']
        if user_input:
            model = "gpt-4-turbo"  
            response = chatCompletions(model, user_input)
    return render_template("gpt4.html", response=response)

@app.route('/dalle3', methods=["GET", "POST"])
def dalle_page():
    generated_image = None
    if request.method == 'POST':
        user_input = request.form['content']
        if user_input:
            model = "dalle3"
            image_data = imgGeneration(model,user_input)
            generated_image = base64.b64encode(image_data).decode('utf-8')
    return render_template("dalle3.html", generated_image=generated_image)
