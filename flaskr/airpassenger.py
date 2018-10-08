from flask import Flask, render_template, request, jsonify
import pymysql

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config["JSON_SORT_KEYS"] = False

#Mysql接続情報
def getConnection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='human92',
        db='air_passenger',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor,
    )

@app.route('/')
def count_passenger():
    with app.app_context():
        db = getConnection()
        cur = db.cursor()
        sql = "select * from airpassenger"
        cur.execute(sql)
        passengers = cur.fetchall()
        cur.close()
        db.close()
        result = jsonify({'passengers':passengers})
    return render_template('index.html', result=result)
    # return jsonify({'passengers':passengers})

# おまじない
if __name__ == "__main__":
    app.run(debug=True)