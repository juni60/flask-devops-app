from flask import Flask, jsonify
import os
import socket
from datetime import datetime

app = Flask(__name__)

# Root endpoint
@app.route("/")
def home():
    return jsonify({
        "message": "Hello from Flask DevOps App 🚀",
        "status": "running",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "hostname": socket.gethostname()
    })

# Health check endpoint (VERY IMPORTANT for Kubernetes)
@app.route("/health")
def health():
    return jsonify({
        "status": "UP"
    }), 200

# Environment info (useful for debugging in containers)
@app.route("/env")
def env():
    return jsonify({
        "environment": os.getenv("APP_ENV", "development"),
        "version": os.getenv("APP_VERSION", "1.0.0")
    })

if __name__ == "__main__":
    # 0.0.0.0 is REQUIRED for Docker & Kubernetes
    app.run(host="0.0.0.0", port=5000)
