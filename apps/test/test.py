from flask import Flask

app = Flask(__name__)  # Flask 애플리케이션 객체 생성

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run(debug=True)     # flask run을 사용할 경우 해당 설정이 적용 X -> flask --debug run 사용
