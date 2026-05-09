from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from trends import get_trends

app = Flask(__name__)
#__name__ is a special Python variable that just tells Flask "this is the main file". CORS(app) wraps your app so browsers are allowed to talk to it.
CORS(app)

@app.route('/api/trends')
def trends():
    keyword = request.args.get('keyword')
    result = get_trends(keyword)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
#run the server when this file is executed directly 
