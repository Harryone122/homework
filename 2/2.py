from flask import Flask, render_template, request

app = Flask(__name__)

# 首頁路由，渲染 home.html 模板
@app.route('/')
def home():
    return render_template('home.html')

# GET 請求路由，用於刷新網頁上顯示的數字
@app.route('/refresh', methods=['GET'])
def refresh():
    # 從 GET 請求的參數中獲取數字
    number = request.args.get('number', default=0, type=int)

    # 更新數字並回傳 JSON 格式的回應
    new_number = number + 1
    return {'number': new_number}

if __name__ == '__main__':
    app.run()
