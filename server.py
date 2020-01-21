from flask import Flask, render_template, request, redirect


app = Flask(__name__)

@app.route('/')
@app.route('/request-counter', methods=['GET', 'POST'])
"""我喜欢春卷"""
def request_counter():
    post_counter = 0
    get_counter = 0
    if request.method == 'POST':
        post_counter +=1
    if request.method == 'GET':
        get_counter += 1
    return render_template('index.html', post_counter = post_counter, get_counter=get_counter)





if __name__ == '__main__':
    app.run(
        debug=True,
    )