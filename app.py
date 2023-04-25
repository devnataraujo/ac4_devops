import os
from flask import Flask, render_template, request
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'natju'
app.config['MYSQL_DATABASE_DB'] = 'teste'
app.config['MYSQL_DATABASE_HOST'] = '172.17.0.2'
mysql.init_app(app)


@app.route('/')
def main():
    return render_template('login.html')

@app.route('/gravar', methods=['POST','GET'])
def gravar():
  nome = request.form['nome']
  email = request.form['email']
  senha = request.form['senha']
  if nome and email and senha:
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('insert into tbl_user (user_name, user_email, user_password) VALUES (%s, %s, %s)', (nome, email, senha))
    conn.commit()
  return render_template('login.html')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5008))
    app.run(host='0.0.0.0', port=port)