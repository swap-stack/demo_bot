from flask import Flask, jsonify,request, render_template
import time
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route("/bot", methods=["GET","POST"])
def response():
    if request.method == 'POST':
        query = dict(request.form)['query']
        res = query + " " + time.ctime()
        return jsonify({"response" : res})
    if request.method == 'GET':
        return "hi"

if __name__=="__main__":
    app.run(host="0.0.0.0",)