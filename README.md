**Text Summarization with Sentence Similarity Graph**

This project demonstrates a text summarization tool that uses a graph-based approach to extract the most significant sentences from a given text. The tool also visualizes the sentence similarity graph using Cytoscape.js.

**Features**

Summarizes input text by extracting key sentences.

Visualizes the sentence similarity graph.

Utilizes network analysis to rank sentences based on their importance.

**Technologies Used**

Flask for the web framework.

NLTK for natural language processing.

NetworkX for graph-based operations.

Cytoscape.js for graph visualization.

**Installation**

**Prerequisites**

Python 3.x

pip (Python package installer)

**Steps**

Clone the Repository

Open your terminal or command prompt.

Run the following command to clone the repository and navigate into the project directory:
```
git clone https://github.com/your-username/text-summarization-graph.git

cd text-summarization-graph
```

Create a Virtual Environment

Create a virtual environment by running the following command:
```
python -m venv venv
```

Activate the Virtual Environment

Activate the virtual environment.
On Windows, run:
```
.\venv\Scripts\activate
```
On macOS/Linux, run:
```
source venv/bin/activate
```

Install the Required Packages

Install the necessary Python packages by running:
```
pip install -r requirements.txt
```

Run the Application

Start the Flask application by running:
```
python app.py
```

Open Your Browser

Navigate to `http://127.0.0.1:5000/` in your web browser to use the text summarization tool.

**Project Structure**

`app.py`: Main application file for Flask.

`summarizer.py`: Contains functions for reading articles, calculating sentence similarities, and generating summaries.

`templates/index.html`: HTML file for the web interface.

`static/css/style.css`: CSS file for styling the web interface.

`requirements.txt`: Lists the Python packages required for the project.

**How It Works**

Text Input: Users input the text they want to summarize.

Text Processing: The input text is split into sentences and preprocessed.

Similarity Matrix: A similarity matrix is built using cosine similarity between sentence vectors.

Graph Construction: A graph is constructed where nodes represent sentences and edges represent the similarity scores.

Sentence Ranking: Sentences are ranked using the PageRank algorithm.

Summary Generation: Top-ranked sentences are selected to form the summary.

Graph Visualization: The similarity graph is visualized using Cytoscape.js.

**Contributing**

Contributions are welcome! Please feel free to submit a Pull Request.

**License**

This project is licensed under the MIT License. See the LICENSE file for more details.
