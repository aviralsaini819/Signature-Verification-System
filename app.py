from flask import Flask, render_template, request, jsonify
from tkinter_integration import check_similarity

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/verify_signature', methods=['POST'])
def verify_signature():
    user_signature = request.files['userSignature']
    compare_signatures = request.files['compareSignatures']

    result = check_similarity(user_signature, compare_signatures)

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
