# Flask-and-MySQL-communication-example

## 簡介
這個只是用作展示 `flask` 與 `MySQL server` 通訊的簡單例子
code寫得很差 請多多包涵

## code 基本簡介

### 需要的library
```python
from flask import Flask,request
import pymysql #用python實現與MySQL通訊的library
import datetime #用來生成現在時間的library
```

### 基本設定
```python
app = Flask(__name__)
app.config["DEBUG"] = True #把debug選項打開
db = pymysql.connect("192.168.1.22", "root", "password", "dev") #與MySQL的必要設定設定好
cursor = db.cursor()
```

### function 簡介

#### getDatetime()
因為`MySQL`裏有一種資料型態叫做`datetime`，專門是用來儲存時間
故此本人並不考慮利用`unix time`(在`MySQL`對應的資料型態應該是`timestamp`)儲存時間
而`datetime`的format為```YYYY-MM-DD hh:mm:ss```
```python
def getDatetime():
    return datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
```

#### 路由
它的format基本上是
```python
@app.route('/', methods=['GET'])
```
第一個參數是host address之後的路徑如 localhost:5000/**test**
而第二個參數則是`http method` 最常用的是get及post

```python
@app.route('/', methods=['GET'])
def home():
    return "<h1>Index</h1>"
```
在上述code的例子中 只要連接到 http://localhost/ 時，在取得的網頁source code就會有一行
```html
<h1>Index</h1>
```

下面這段code是將這個flask的application可以讓其他的電腦連接
因為flask default好像是只允許執行程式的機器連接到該application
```python
app.run(host= '0.0.0.0')
```

