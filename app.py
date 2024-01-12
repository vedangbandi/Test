from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return def star(n):
                for i in range(0, n):
                           for j in range(0, i+1):
                                      print("* ",end="")
                           print("\r")
 n = 5
 star(n)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
