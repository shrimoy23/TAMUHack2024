from website import create_app
from langchain_openai import ChatOpenAI

app = create_app()

if __name__ == '__main__':
    app.run(debug=True) 
