from flask import Flask, render_template, request, jsonify
import mysql.connector
from flask_mysqldb import MySQL
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, DateField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'morteza'
app.config['MYSQL_PASSWORD'] = 'Morteza@5#1373'
app.config['MYSQL_DB'] = 'testselect'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
db = MySQL(app)


mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="morteza",
    passwd="Morteza@5#1373",
    db="testselect",
    charset='utf8'

)



dbc = mydb.cursor(dictionary=True)


@app.route('/te', methods=['GET', 'POST'])
def te():
    form = TestForm()
    cur = db.connection.cursor()
    cur.execute('select * from teste where state = "CA"')
    rv = cur.fetchall()
    return (str(rv[0]['name']))


object = [
    {"id": 1, "company": "Google", "employees": [
        {"name": "Mike"},
        {"name": "Jessica"},
    ]},
    {"id": 2, "company": "H&M", "employees": [{"name": "bbb"},
                                              {"name": "rrr"}, ]},
    {"id": 3, "company": "Ikea", "employees": [{"name": "sss"},
                                               {"name": "ttt"}, ]},
]


def database():

    compDB = dbc.execute("SELECT * FROM Companies")
    compDB = dbc.fetchall()

    empDB = dbc.execute("SELECT * FROM Employees")
    empDB = dbc.fetchall()

    return render_template("database.html",
                            compDB = compDB,
                            empDB = empDB,
                            javascript=object)


class TestForm(FlaskForm):
    state = SelectField('State', choices=[('CA', 'California'), ('NY', 'NEVADA')])
    city = SelectField('City', choices=[])


@app.route('/', methods=['GET', 'POST'])
def index():
    form = TestForm()
    stateCA = dbc.execute('select * from teste where state = "CA"')
    stateCA = dbc.fetchall()

    form.city.choices = [(stateCA[0]['id'], stateCA[0]['name']) for city in str(stateCA)]

    return render_template('testselect.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
