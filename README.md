# Without Docker
1) python -m venv venv
2) venv\Scripts\activate.bat -> Windows | source venv/bin/activate -> Linux
3) pip install -r requirements.txt
4) Create .env file and copy the content from .env.example
5) flask run

# With Docker
1) Create .env file and copy the content from .env.example
2) ./run-image.sh
