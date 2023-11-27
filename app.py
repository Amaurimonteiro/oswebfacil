from flask import Flask,jsonify


app = Flask(__name__)

@app.route('/')
def raiz():
    
    return 'Olá Mundo!'

if __name__ == "__main__":
    app.run()

#app.run(debug=True)
