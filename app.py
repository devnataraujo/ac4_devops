import os
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('login.html')

@app.route('/gravar', methods=['POST','GET'])
def gravar():
  nome = request.form['nome']
  email = request.form['email']
  senha = request.form['senha']
  if nome and email and senha:
    print(nome, email, senha)
  return render_template('login.html')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5008))
    app.run(host='0.0.0.0', port=port)