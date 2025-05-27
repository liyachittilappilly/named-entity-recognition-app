from flask import Flask, request, render_template
import spacy
from spacy import displacy

# Load the English NLP model
nlp = spacy.load('en_core_web_sm')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', html=None, text=None)


@app.route('/entity', methods=['POST', 'GET'])
def entity():
    if request.method == 'POST':
        file = request.files.get('file')
        if file:
            readable_file = file.read().decode('utf-8', errors='ignore')
            docs = nlp(readable_file)
            html = displacy.render(docs, style='ent', jupyter=False)
            return render_template('index.html', html=html, text=readable_file)
    return render_template('index.html', html=None, text=None)

if __name__ == '__main__':
    app.run(debug=True)
