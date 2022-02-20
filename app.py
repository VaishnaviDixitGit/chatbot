from flask import Flask, render_template, jsonify, request
import processor


app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())



@app.route('/chatbot', methods=["GET", "POST"])
def Response():

    if request.method == 'POST':
        question = request.form['question']

        response = processor.chat(question)

    return jsonify({"response": response })


'''
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)
'''
