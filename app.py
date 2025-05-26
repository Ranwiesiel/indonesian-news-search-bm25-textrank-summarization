from flask import Flask, render_template, request
from whoosh.qparser import QueryParser
from schema import schema
from whoosh.index import open_dir
import os

# Flask app
app = Flask(__name__)

lock_file = os.path.join("indexdir", "MAIN_WRITELOCK")
if os.path.exists(lock_file):
    os.remove(lock_file)
ix = open_dir('indexdir')


@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    rawquery = ""

    if request.args.get('q'):
        rawquery = request.args.get('q')
        print(rawquery)

        rawquery = rawquery.lower()

        qp = QueryParser("content_processed", schema=schema)
        q = qp.parse(rawquery)

        with ix.searcher() as searcher:
            # Search the index
            results = searcher.search(q, limit=10)
            found = results.scored_length()
            
            if results.has_exact_length():
                results = results[:found]
            else:
                results = results[:10]

            # Convert results to a list of dictionaries
            results = [
                {
                    'path': hit['path'],
                    'title': hit['title'],
                    'original_content': hit['original_content'],
                    'tags': hit['tags'],
                    'summarization': hit['summarization'],
                    'datetime': hit['datetime'],
                    'bm25_score': hit.score,
                }
                for hit in results
            ]

    return render_template('index.html', results=results, query=rawquery)

if __name__ == '__main__':
    app.run(debug=True)
