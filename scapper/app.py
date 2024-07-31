from flask import Flask, render_template
import json

app = Flask(__name__)

def load_project_data():
    try:
        with open('project_data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

@app.route('/')
def index():
    projects = load_project_data()
    return render_template('index.html', projects=projects)

if __name__ == '__main__':
    app.run(debug=True)
