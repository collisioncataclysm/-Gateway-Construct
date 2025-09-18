from pathlib import Path

base = Path(".")
frontend = base / "frontend"
backend = base / "backend"

frontend.mkdir(exist_ok=True)
backend.mkdir(exist_ok=True)

files = {
    "frontend/index.html": "<h1>Λ Syndicator</h1><p>Universal publisher interface</p>",
    "backend/app.py": "from flask import Flask, jsonify\napp = Flask(__name__)\n@app.route('/api/health')\ndef health():\n    return jsonify({'status':'ok'})\nif __name__=='__main__':\n    app.run(port=5000)",
    "requirements.txt": "flask\nrequests",
    "Procfile": "web: python backend/app.py",
    ".env.example": "GITHUB_TOKEN=\nZENODO_TOKEN=\nIPFS_KEY=\nAUTHOR_NAME=\nAUTHOR_ORCID=",
    "README.md": "# Λ Syndicator\n\nUniversal publishing interface for the Lambda Collation proof.\n"
}

for path, content in files.items():
    file_path = base / path
    file_path.write_text(content, encoding="utf-8")
    print(f"✅ Wrote {file_path}")

print("🎉 All files created!")
