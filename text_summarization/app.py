from flask import Flask, request, render_template
from summarizer import generate_summary, build_similarity_matrix, read_article
import json
import nltk

nltk.download('stopwords')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.form['text']
    if not text.strip():
        return render_template('index.html', summary="No text provided", original_text=text)

    sentences = read_article(text)
    if not sentences:
        return render_template('index.html', summary="No valid sentences found", original_text=text)

    similarity_matrix = build_similarity_matrix(sentences, nltk.corpus.stopwords.words('english'))
    top_n = max(1, len(sentences) // 3)
    summary = generate_summary(text, top_n=top_n)
    return render_template('index.html', summary=summary, original_text=text, similarity_matrix=json.dumps(similarity_matrix.tolist()), sentences=json.dumps(sentences))

if __name__ == "__main__":
    app.run(debug=True)
