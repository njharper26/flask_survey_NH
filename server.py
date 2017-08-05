from flask import Flask, session, request, redirect, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    name = request.form['html_name']
    city = request.form['html_city']
    stacks = request.form['html_stacks']
    favorite = request.form['html_favorite']
    os = request.form['html_os']
    graduation = request.form['html_graduation']
    comments = request.form['html_comments']

    print comments
    
    return render_template('success.html', name=name, city=city, stacks=stacks, favorite=favorite, os=os, graduation=graduation, comments=comments)

app.run(debug=True)