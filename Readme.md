\# Flask DevOps Demo App



This is a simple Flask application designed for DevOps CI/CD, Docker, and Kubernetes practice.



\## Endpoints



\- `/` → Application info

\- `/health` → Health check (used by Kubernetes)

\- `/env` → Environment details



\## Run Locally



```bash

pip install -r requirements.txt

python app.py

cd flask-devops-app
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py

