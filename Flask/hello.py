from flask import Flask

app = Flask(__name__)
print("sdfshg")
@app.route("/")
@app.route("/home")
@app.route("/index")
def code():
    return "Inference Labs\n"

if __name__=='_main__':
    app.run()