from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route('/api/publish', methods=['POST'])
def publish():
    data = request.json or {}
    author = data.get("author_name","Anonymous")
    orcid = data.get("author_orcid","N/A")
    return jsonify({
        "status":"ok",
        "timestamp": datetime.now().isoformat(),
        "author": author,
        "orcid": orcid,
        "platforms": {
            "github":"ready",
            "zenodo":"ready",
            "ipfs":"ready",
            "arxiv":"ready",
            "medium":"ready"
        }
    })

@app.route('/health')
def health():
    return jsonify({"status":"healthy","service":"Lambda Syndicator"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
