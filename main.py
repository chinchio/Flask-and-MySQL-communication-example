from flask import Flask,request
import pymysql
import datetime
app = Flask(__name__)
app.config["DEBUG"] = True
db = pymysql.connect("192.168.1.22", "root", "password", "dev")
cursor = db.cursor()

def getDatetime():
    return datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

@app.route('/', methods=['GET'])
def home():
    return "<h1>Index</h1>"

@app.route("/store/item/add", methods=['GET'])
def addItem():
    seller = request.args.get("seller")
    create_time = getDatetime()
    image = request.args.get("image")
    names = request.args.get("names")
    price = int(request.args.get("price"))
    sql = "INSERT INTO `products` (`seller`, `create_time`, `image`, `names`, `price`)\n"\
            "VALUES ({}, '{}', '{}', '{}', {});".format(seller, create_time, image, names, price)
    cursor.execute(sql)
    db.commit()
    return sql
    #return str(cursor.fetchall())
    #return {"param":request.args}

@app.route("/store/item/delete", methods=['GET'])
def deleteItem():
    id = int(request.args.get("id"))
    sql = "DELETE FROM products\n"\
            "WHERE id = {};".format(id)
    cursor.execute(sql)
    db.commit()
    return sql
    #return {"param":request.args}

app.run(host= '0.0.0.0')
