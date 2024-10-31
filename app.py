from flask import Flask, request, jsonify
from flask_cors import CORS  # CORS 모듈 추가
import json
import os

app = Flask(__name__)
CORS(app)  # 모든 출처의 요청을 허용

# 저장 경로 설정 (예: 본인 컴퓨터의 특정 경로)
save_directory = "./"  # 현재 디렉토리에 저장

@app.route('/save-survey', methods=['POST'])
def save_survey():
    data = request.get_json()  # JSON 데이터 가져오기
    
    # 파일 이름 설정 (예: survey_result.json)
    file_path = os.path.join(save_directory, "survey_result.json")

    # 파일로 저장
    try:
        with open(file_path, 'w') as f:
            json.dump(data, f)
        return jsonify({"message": "설문 결과가 성공적으로 저장되었습니다.", "path": file_path}), 200
    except Exception as e:
        print("파일 저장 오류:", e)
        return jsonify({"error": "파일 저장에 실패했습니다."}), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)  # 로컬에서 실행할 포트 설정
