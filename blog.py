from flask import Flask,render_template,flash,redirect,url_for,session,logging,request
from flask_mysqldb import MySQL
from wtforms import Form,StringField,PasswordField,validators
from passlib.hash import sha256_crypt


class RegisterForm(Form):
    name = StringField("İsim Soyisim",validators=[validators.Length(min =4,max = 25)])
    username = StringField("Kullanıcı Adı",validators=[validators.Length(min =5,max = 35)])
    email = StringField("Email Adresi",validators=[validators.Email(message="Lütfen Geçerli Bir Mail adresi giriniz")])
    password = PasswordField("Parola:",validators=[validators.DataRequired(message ="Lütfen Bir Parola Belirleyin"),validators.EqualTo(fieldname = "confirm",message ="Parolanız Uyuşmuyor...")])
    confirm = PasswordField("Parola Doğrula")

app= Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] ="ybblog"
app.config["MYSQL_CURSORCLASS"]="DictCursor"

mysql =MySQL(app)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html",ali=5)

#kayıt olma    
@app.route("/register",methods =["GET","POST"])
def register():
    form = RegisterForm(request.form)

    if request.method == "POST":
        pass
    else:
        return render_template("register.html",form = form)

if __name__ == "__main__":
    app.run(debug=True)

