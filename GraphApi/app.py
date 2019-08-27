from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error
import time

mySQLconnection = mysql.connector.connect(host='localhost',
                             database='data',
                             user='root',
                             password='')

def sqlpull(k):
    sqlSelect2 = "SELECT payment1 FROM maindata ORDER BY date"
    cursor3 = mySQLconnection .cursor()
    cursor3.execute(sqlSelect2)
    lines3 = cursor3.fetchall()
    lines3fixed = list(sum(lines3, ()))

    value1 = lines3fixed

    sqlSelect = "SELECT payment2 FROM maindata ORDER BY date"
    cursor = mySQLconnection .cursor()
    cursor.execute(sqlSelect)
    lines = cursor.fetchall()
    linesfixed = list(sum(lines, ()))

    value2 = linesfixed

    dateselect = "SELECT date FROM maindata ORDER BY date"
    Dcursor = mySQLconnection.cursor()
    Dcursor.execute(dateselect)
    datelines = Dcursor.fetchall()
    datelinesfixed = list(sum(datelines, ()))


    k = [
    {
        'id': 1,
        'data': lines3fixed,
        'datagraph' : value1,
        'date': datelinesfixed, 
        'done': False
	},
	{
		'id': 2,
		'data': linesfixed,
        'datagraph': value2,
        'date': datelinesfixed, 
		'done': False
	}
    ]
    return k

def topusers(l):
    selecttop = "SELECT user FROM maindata ORDER BY date DESC"
    topcursor = mySQLconnection.cursor()
    topcursor.execute(selecttop)
    users = topcursor.fetchall()
    usersfixed = list(sum(users, ()))

    topPay1 = "SELECT payment1 FROM maindata ORDER BY date DESC"
    paycursor1 = mySQLconnection.cursor()
    paycursor1.execute(topPay1)
    pay1users = paycursor1.fetchall()
    pay1fixed = list(sum(pay1users, ()))

    topPay2 = "SELECT payment2 FROM maindata ORDER BY date DESC"
    paycursor2 = mySQLconnection.cursor()
    paycursor2.execute(topPay2)
    pay2users = paycursor2.fetchall()
    pay2fixed = list(sum(pay2users, ()))

    dateselect2 = "SELECT date FROM maindata ORDER BY date DESC"
    Dcursor2 = mySQLconnection.cursor()
    Dcursor2.execute(dateselect2)
    datalines2 = Dcursor2.fetchall()
    datelines2fixed = list(sum(datalines2, ()))

    l = [
        {
        'id': 1,
        'user': usersfixed[0],
        'pay1': pay1fixed[0],
        'pay2': pay2fixed[0],
        'date': datelines2fixed[0], 
        'done': False
	},
    {
        'id': 2,
        'user': usersfixed[1],
        'pay1': pay1fixed[1],
        'pay2': pay2fixed[1],
        'date': datelines2fixed[1], 
        'done': False
	},
    {
        'id': 3,
        'user': usersfixed[2],
        'pay1': pay1fixed[2],
        'pay2': pay2fixed[2],
        'date': datelines2fixed[2], 
        'done': False
	},
    {
        'id': 4,
        'user': usersfixed[3],
        'pay1': pay1fixed[3],
        'pay2': pay2fixed[3],
        'date': datelines2fixed[3], 
        'done': False
	},
    {
        'id': 5,
        'user': usersfixed[4],
        'pay1': pay1fixed[4],
        'pay2': pay2fixed[4],
        'date': datelines2fixed[4], 
        'done': False
	}

    ]
    return l


login = [
        {
            'username': 'username' ,
            'password': 'password'
        }
        ]


app = Flask(__name__)

cors = CORS(app, resources={r"/todo/api/v1.0/stuff": {"origins": "*"}})
cors = CORS(app, resources={r"/todo/api/v1.0/top": {"origins": "*"}})
cors = CORS(app, resources={r"/todo/api/v1.0/login": {"origins": "*"}})

@app.route('/todo/api/v1.0/stuff', methods=['GET'])
def get_stuff():
   
        stuff = []
        sent = sqlpull(stuff)
        return jsonify({'stuff': sent})

@app.route('/todo/api/v1.0/top', methods=['GET'])    
def get_top():

        tops = []
        ret = topusers(tops)
        return jsonify({'top':ret})    

@app.route('/todo/api/v1.0/login', methods=['GET'])
def logininfo():

        return jsonify({'login' : login})

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=5000, passthrough_errors=True)
        