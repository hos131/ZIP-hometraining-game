from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)  # 🔹 CORS 활성화

# MongoDB Atlas 연결
MONGO_URI = "mongodb+srv://Hos:ufks6020110@cluster0.q42yj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGO_URI)
db = client["mydatabase"]  # 사용할 데이터베이스
collection = db["mycollection"]  # 사용할 컬렉션

@app.route("/add", methods=["POST"])
def add_data():
    try:
        # 요청에서 JSON 데이터 가져오기
        data = request.json
        if not data:
            return jsonify({"error": "data not provided"}), 400

        # MongoDB에 데이터 삽입
        result = collection.insert_one(data)

        return jsonify({"message": "Data added successfully", "id": str(result.inserted_id)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Flask 서버 실행 (항상 맨 아래에 위치해야 함)
if __name__ == "__main__":
    app.run(debug=False, use_reloader=False)

    

