from flask import Flask, request, jsonify

app = Flask(__name__)

# 定义一个简单的回调接口
@app.route('/callback', methods=['POST'])
def callback():
    data = request.json  # 获取 JSON 数据
    if not data:
        return jsonify({"error": "No data provided"}), 400

    # 处理接收到的数据
    print("Received data:", data)
    response = {
        "status": "success",
        "received_data": data
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)  # 监听本地 5000 端口
