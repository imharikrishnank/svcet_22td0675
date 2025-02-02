from flask import Flask,  request
app = Flask(__name__)
data = {"message": "Hello, World!"}

@app.route('/')
def home():
    return "welcome to flask"
@app.route('/data' , methods=['GET'])
def get_data():
    data = request.json
    return{"data":data , "message": "send a POST request with json data"}
@app.route('/data' , methods=['POST'])
def post_data():
    data = request.json
    return{"message": "data received" , "data":data}
@app.route('/update/<int:item_id>' , methods=['PUT'])
def update_data(item_id):
    return{"message":f"Item{item_id} updated"}
@app.route('/delete/<int:item_id>' , methods=['DELETE'])
def delete_data(item_id):
    return{"message":f"Item{item_id} deleted"}

if __name__ == '__main__':
    app.run(debug=True)
