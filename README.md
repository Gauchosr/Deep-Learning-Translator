# Project Summary 
In this project, we'll build a translation API using deep learning. Using FastAPI, we'll create a web server that exposes a /translate route and a /results route. Clients will post their translation request to the /translate route, and get the translation results from /results. The server will use a sqlite database to store the translations. On the backend, we'll use async and a pretrained deep learning language model to run the translation job.
By the end, we'll have a web server that can run translation jobs quickly. This server can easily be extended to translate more languages, or add more options.

# Code 
File overview:

requirements.txt - packages you'll need to install
main.py - defines the web server routes
models.py - defines database models
tasks.py - runs our backend tasks, including the translation

# Local Setup 
To run this project, you'll need to install: 
- requirements.txt
- Python 3.8+

# Usage
To run the server locally, run **uvicorn main:app --reload**
