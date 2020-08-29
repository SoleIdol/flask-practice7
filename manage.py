# author:Sole_idol
# filename: manage.py
# datetime:2020/8/19 7:59
"""
g对象练习
    可以将用户各种数据保存在他身上，关联上下文，但在浏览器是不会存储的，需要去把g对象传过去
"""
from flask import Flask, render_template, request, abort
from flask import g

app = Flask(__name__)


@app.route('/', methods=('POST', 'GET'))
def login():
    if request.method == 'POST':
        # 创建g的属性
        g.name = request.form.get('name')
        g.password = request.form.get('password')
        print('========获取到的值========\n', g.name, g.password)
        return render_template('main.html', name=g.name, password=g.password)
    else:
        return render_template('login.html')


@app.route('/login1/', methods=('POST', 'GET'))
def login_test():
    if request.method == 'POST':
        # 创建g的属性
        name = request.form.get('name')
        password = request.form.get('password')
        if name == 'jack' and password == '123456':
            return render_template('main.html', name=name, password=password)
        else:
            abort(403)
            return '访问被拒绝'
    else:
        return render_template('login11.html')


@app.route('/xxx/')
def xxx():
    # g对象，第二次请求时，第一次请求的数据就消失了
    return f'{g.name} ---> {g.password} '


if __name__ == '__main__':
    app.run(debug=True)
