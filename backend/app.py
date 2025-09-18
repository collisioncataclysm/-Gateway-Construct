from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/api/publish", methods=["POST"])
def publish():
    data = request.get_json()
    title = data.get("title")
    content = data.get("content")

    # Stub: here you could add integration with GitHub, Zenodo, IPFS, etc.
    print(f"Publishing: {title}\n{content[:100]}...")

    return jsonify({"message": f"✅ '{title}' published successfully!"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
