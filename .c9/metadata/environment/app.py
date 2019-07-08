{"changed":true,"filter":false,"title":"app.py","tooltip":"/app.py","value":"import os\nfrom flask import Flask, render_template, redirect, request, url_for\nfrom flask_pymongo import PyMongo\nfrom bson.objectid import ObjectId\n\napp = Flask(__name__)\n\napp.config[\"MONGO_DBNAME\"] = 'recipe_db'\napp.config[\"MONGO_URI\"] = 'mongodb+srv://root2019:RooT20i9@myfirstcluster-2yjug.mongodb.net/recipe_db?retryWrites=true&w=majority'\n\nmongo = PyMongo(app)\n\n@app.route('/')\n@app.route('/')\n\n\n\n@app.route('/get_recipes')\ndef get_recipes():\n    return render_template(\"recipes.html\", recipes=mongo.db.recipes.find())\n    \nif __name__ == '__main__' :\n    app.run(host=os.environ.get('IP'),\n            port=int(os.environ.get('PORT')),\n            debug=True)\n\n    ","undoManager":{"mark":94,"position":100,"stack":[[{"start":{"row":3,"column":31},"end":{"row":3,"column":32},"action":"insert","lines":["t"],"id":106},{"start":{"row":3,"column":32},"end":{"row":3,"column":33},"action":"insert","lines":["I"]},{"start":{"row":3,"column":33},"end":{"row":3,"column":34},"action":"insert","lines":["d"]}],[{"start":{"row":5,"column":21},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":107},{"start":{"row":6,"column":0},"end":{"row":7,"column":0},"action":"insert","lines":["",""]},{"start":{"row":7,"column":0},"end":{"row":7,"column":1},"action":"insert","lines":["a"]}],[{"start":{"row":7,"column":1},"end":{"row":7,"column":2},"action":"insert","lines":["p"],"id":108},{"start":{"row":7,"column":2},"end":{"row":7,"column":3},"action":"insert","lines":["p"]},{"start":{"row":7,"column":3},"end":{"row":7,"column":4},"action":"insert","lines":["."]},{"start":{"row":7,"column":4},"end":{"row":7,"column":5},"action":"insert","lines":["c"]},{"start":{"row":7,"column":5},"end":{"row":7,"column":6},"action":"insert","lines":["o"]}],[{"start":{"row":7,"column":6},"end":{"row":7,"column":7},"action":"insert","lines":["n"],"id":109},{"start":{"row":7,"column":7},"end":{"row":7,"column":8},"action":"insert","lines":["f"]},{"start":{"row":7,"column":8},"end":{"row":7,"column":9},"action":"insert","lines":["i"]},{"start":{"row":7,"column":9},"end":{"row":7,"column":10},"action":"insert","lines":["g"]}],[{"start":{"row":7,"column":10},"end":{"row":7,"column":12},"action":"insert","lines":["[]"],"id":110}],[{"start":{"row":7,"column":11},"end":{"row":7,"column":13},"action":"insert","lines":["\"\""],"id":111}],[{"start":{"row":7,"column":12},"end":{"row":7,"column":13},"action":"insert","lines":["M"],"id":112},{"start":{"row":7,"column":13},"end":{"row":7,"column":14},"action":"insert","lines":["O"]},{"start":{"row":7,"column":14},"end":{"row":7,"column":15},"action":"insert","lines":["N"]},{"start":{"row":7,"column":15},"end":{"row":7,"column":16},"action":"insert","lines":["G"]},{"start":{"row":7,"column":16},"end":{"row":7,"column":17},"action":"insert","lines":["O"]},{"start":{"row":7,"column":17},"end":{"row":7,"column":18},"action":"insert","lines":["_"]}],[{"start":{"row":7,"column":18},"end":{"row":7,"column":19},"action":"insert","lines":["D"],"id":113},{"start":{"row":7,"column":19},"end":{"row":7,"column":20},"action":"insert","lines":["B"]},{"start":{"row":7,"column":20},"end":{"row":7,"column":21},"action":"insert","lines":["N"]},{"start":{"row":7,"column":21},"end":{"row":7,"column":22},"action":"insert","lines":["A"]},{"start":{"row":7,"column":22},"end":{"row":7,"column":23},"action":"insert","lines":["M"]},{"start":{"row":7,"column":23},"end":{"row":7,"column":24},"action":"insert","lines":["E"]}],[{"start":{"row":7,"column":26},"end":{"row":7,"column":27},"action":"insert","lines":[" "],"id":114},{"start":{"row":7,"column":27},"end":{"row":7,"column":28},"action":"insert","lines":["="]}],[{"start":{"row":7,"column":28},"end":{"row":7,"column":29},"action":"insert","lines":[" "],"id":115}],[{"start":{"row":7,"column":29},"end":{"row":7,"column":31},"action":"insert","lines":["''"],"id":116}],[{"start":{"row":7,"column":30},"end":{"row":7,"column":31},"action":"insert","lines":["r"],"id":117},{"start":{"row":7,"column":31},"end":{"row":7,"column":32},"action":"insert","lines":["e"]},{"start":{"row":7,"column":32},"end":{"row":7,"column":33},"action":"insert","lines":["c"]},{"start":{"row":7,"column":33},"end":{"row":7,"column":34},"action":"insert","lines":["i"]},{"start":{"row":7,"column":34},"end":{"row":7,"column":35},"action":"insert","lines":["p"]},{"start":{"row":7,"column":35},"end":{"row":7,"column":36},"action":"insert","lines":["e"]},{"start":{"row":7,"column":36},"end":{"row":7,"column":37},"action":"insert","lines":["_"]}],[{"start":{"row":7,"column":37},"end":{"row":7,"column":38},"action":"insert","lines":["d"],"id":118},{"start":{"row":7,"column":38},"end":{"row":7,"column":39},"action":"insert","lines":["b"]}],[{"start":{"row":7,"column":40},"end":{"row":8,"column":0},"action":"insert","lines":["",""],"id":119},{"start":{"row":8,"column":0},"end":{"row":8,"column":1},"action":"insert","lines":["a"]},{"start":{"row":8,"column":1},"end":{"row":8,"column":2},"action":"insert","lines":["p"]},{"start":{"row":8,"column":2},"end":{"row":8,"column":3},"action":"insert","lines":["p"]},{"start":{"row":8,"column":3},"end":{"row":8,"column":4},"action":"insert","lines":["."]},{"start":{"row":8,"column":4},"end":{"row":8,"column":5},"action":"insert","lines":["c"]},{"start":{"row":8,"column":5},"end":{"row":8,"column":6},"action":"insert","lines":["o"]}],[{"start":{"row":8,"column":6},"end":{"row":8,"column":7},"action":"insert","lines":["n"],"id":120},{"start":{"row":8,"column":7},"end":{"row":8,"column":8},"action":"insert","lines":["f"]},{"start":{"row":8,"column":8},"end":{"row":8,"column":9},"action":"insert","lines":["i"]},{"start":{"row":8,"column":9},"end":{"row":8,"column":10},"action":"insert","lines":["g"]}],[{"start":{"row":8,"column":10},"end":{"row":8,"column":12},"action":"insert","lines":["[]"],"id":121}],[{"start":{"row":8,"column":11},"end":{"row":8,"column":13},"action":"insert","lines":["\"\""],"id":122}],[{"start":{"row":8,"column":12},"end":{"row":8,"column":13},"action":"insert","lines":["M"],"id":123},{"start":{"row":8,"column":13},"end":{"row":8,"column":14},"action":"insert","lines":["O"]},{"start":{"row":8,"column":14},"end":{"row":8,"column":15},"action":"insert","lines":["N"]},{"start":{"row":8,"column":15},"end":{"row":8,"column":16},"action":"insert","lines":["G"]},{"start":{"row":8,"column":16},"end":{"row":8,"column":17},"action":"insert","lines":["O"]},{"start":{"row":8,"column":17},"end":{"row":8,"column":18},"action":"insert","lines":["_"]}],[{"start":{"row":8,"column":18},"end":{"row":8,"column":19},"action":"insert","lines":["U"],"id":124},{"start":{"row":8,"column":19},"end":{"row":8,"column":20},"action":"insert","lines":["R"]},{"start":{"row":8,"column":20},"end":{"row":8,"column":21},"action":"insert","lines":["I"]}],[{"start":{"row":8,"column":23},"end":{"row":8,"column":24},"action":"insert","lines":[" "],"id":125},{"start":{"row":8,"column":24},"end":{"row":8,"column":25},"action":"insert","lines":["="]}],[{"start":{"row":8,"column":25},"end":{"row":8,"column":26},"action":"insert","lines":[" "],"id":126}],[{"start":{"row":8,"column":26},"end":{"row":8,"column":28},"action":"insert","lines":["''"],"id":127}],[{"start":{"row":8,"column":27},"end":{"row":8,"column":126},"action":"insert","lines":["mongodb+srv://root2019:<password>@myfirstcluster-2yjug.mongodb.net/test?retryWrites=true&w=majority"],"id":128}],[{"start":{"row":8,"column":97},"end":{"row":8,"column":98},"action":"remove","lines":["t"],"id":129},{"start":{"row":8,"column":96},"end":{"row":8,"column":97},"action":"remove","lines":["s"]},{"start":{"row":8,"column":95},"end":{"row":8,"column":96},"action":"remove","lines":["e"]},{"start":{"row":8,"column":94},"end":{"row":8,"column":95},"action":"remove","lines":["t"]}],[{"start":{"row":8,"column":94},"end":{"row":8,"column":95},"action":"insert","lines":["r"],"id":130},{"start":{"row":8,"column":95},"end":{"row":8,"column":96},"action":"insert","lines":["e"]},{"start":{"row":8,"column":96},"end":{"row":8,"column":97},"action":"insert","lines":["c"]},{"start":{"row":8,"column":97},"end":{"row":8,"column":98},"action":"insert","lines":["i"]},{"start":{"row":8,"column":98},"end":{"row":8,"column":99},"action":"insert","lines":["p"]},{"start":{"row":8,"column":99},"end":{"row":8,"column":100},"action":"insert","lines":["e"]}],[{"start":{"row":8,"column":100},"end":{"row":8,"column":101},"action":"insert","lines":["_"],"id":131},{"start":{"row":8,"column":101},"end":{"row":8,"column":102},"action":"insert","lines":["d"]},{"start":{"row":8,"column":102},"end":{"row":8,"column":103},"action":"insert","lines":["b"]}],[{"start":{"row":8,"column":50},"end":{"row":8,"column":60},"action":"remove","lines":["<password>"],"id":132},{"start":{"row":8,"column":50},"end":{"row":8,"column":51},"action":"insert","lines":["R"]},{"start":{"row":8,"column":51},"end":{"row":8,"column":52},"action":"insert","lines":["o"]},{"start":{"row":8,"column":52},"end":{"row":8,"column":53},"action":"insert","lines":["o"]}],[{"start":{"row":8,"column":53},"end":{"row":8,"column":54},"action":"insert","lines":["T"],"id":133}],[{"start":{"row":8,"column":54},"end":{"row":8,"column":55},"action":"insert","lines":["2"],"id":134},{"start":{"row":8,"column":55},"end":{"row":8,"column":56},"action":"insert","lines":["0"]},{"start":{"row":8,"column":56},"end":{"row":8,"column":57},"action":"insert","lines":["i"]},{"start":{"row":8,"column":57},"end":{"row":8,"column":58},"action":"insert","lines":["9"]}],[{"start":{"row":9,"column":0},"end":{"row":10,"column":0},"action":"insert","lines":["",""],"id":135},{"start":{"row":10,"column":0},"end":{"row":11,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":1},"action":"insert","lines":["m"],"id":136},{"start":{"row":10,"column":1},"end":{"row":10,"column":2},"action":"insert","lines":["o"]},{"start":{"row":10,"column":2},"end":{"row":10,"column":3},"action":"insert","lines":["n"]},{"start":{"row":10,"column":3},"end":{"row":10,"column":4},"action":"insert","lines":["g"]},{"start":{"row":10,"column":4},"end":{"row":10,"column":5},"action":"insert","lines":["o"]}],[{"start":{"row":10,"column":5},"end":{"row":10,"column":6},"action":"insert","lines":[" "],"id":137},{"start":{"row":10,"column":6},"end":{"row":10,"column":7},"action":"insert","lines":["="]}],[{"start":{"row":10,"column":7},"end":{"row":10,"column":8},"action":"insert","lines":[" "],"id":138},{"start":{"row":10,"column":8},"end":{"row":10,"column":9},"action":"insert","lines":["P"]},{"start":{"row":10,"column":9},"end":{"row":10,"column":10},"action":"insert","lines":["y"]}],[{"start":{"row":10,"column":10},"end":{"row":10,"column":11},"action":"insert","lines":["M"],"id":139},{"start":{"row":10,"column":11},"end":{"row":10,"column":12},"action":"insert","lines":["o"]},{"start":{"row":10,"column":12},"end":{"row":10,"column":13},"action":"insert","lines":["n"]},{"start":{"row":10,"column":13},"end":{"row":10,"column":14},"action":"insert","lines":["g"]},{"start":{"row":10,"column":14},"end":{"row":10,"column":15},"action":"insert","lines":["o"]}],[{"start":{"row":10,"column":15},"end":{"row":10,"column":17},"action":"insert","lines":["()"],"id":140}],[{"start":{"row":10,"column":16},"end":{"row":10,"column":17},"action":"insert","lines":["a"],"id":141},{"start":{"row":10,"column":17},"end":{"row":10,"column":18},"action":"insert","lines":["p"]},{"start":{"row":10,"column":18},"end":{"row":10,"column":19},"action":"insert","lines":["p"]}],[{"start":{"row":1,"column":23},"end":{"row":1,"column":24},"action":"insert","lines":[","],"id":143}],[{"start":{"row":1,"column":24},"end":{"row":1,"column":25},"action":"insert","lines":[" "],"id":144},{"start":{"row":1,"column":25},"end":{"row":1,"column":26},"action":"insert","lines":["r"]},{"start":{"row":1,"column":26},"end":{"row":1,"column":27},"action":"insert","lines":["e"]},{"start":{"row":1,"column":27},"end":{"row":1,"column":28},"action":"insert","lines":["n"]},{"start":{"row":1,"column":28},"end":{"row":1,"column":29},"action":"insert","lines":["d"]},{"start":{"row":1,"column":29},"end":{"row":1,"column":30},"action":"insert","lines":["e"]}],[{"start":{"row":1,"column":30},"end":{"row":1,"column":31},"action":"insert","lines":["r"],"id":145},{"start":{"row":1,"column":31},"end":{"row":1,"column":32},"action":"insert","lines":["_"]},{"start":{"row":1,"column":32},"end":{"row":1,"column":33},"action":"insert","lines":["t"]},{"start":{"row":1,"column":33},"end":{"row":1,"column":34},"action":"insert","lines":["e"]},{"start":{"row":1,"column":34},"end":{"row":1,"column":35},"action":"insert","lines":["m"]}],[{"start":{"row":1,"column":35},"end":{"row":1,"column":36},"action":"insert","lines":["p"],"id":146},{"start":{"row":1,"column":36},"end":{"row":1,"column":37},"action":"insert","lines":["l"]},{"start":{"row":1,"column":37},"end":{"row":1,"column":38},"action":"insert","lines":["a"]},{"start":{"row":1,"column":38},"end":{"row":1,"column":39},"action":"insert","lines":["t"]},{"start":{"row":1,"column":39},"end":{"row":1,"column":40},"action":"insert","lines":["e"]}],[{"start":{"row":1,"column":40},"end":{"row":1,"column":41},"action":"insert","lines":[","],"id":147}],[{"start":{"row":1,"column":41},"end":{"row":1,"column":42},"action":"insert","lines":[" "],"id":148},{"start":{"row":1,"column":42},"end":{"row":1,"column":43},"action":"insert","lines":["r"]},{"start":{"row":1,"column":43},"end":{"row":1,"column":44},"action":"insert","lines":["e"]},{"start":{"row":1,"column":44},"end":{"row":1,"column":45},"action":"insert","lines":["d"]},{"start":{"row":1,"column":45},"end":{"row":1,"column":46},"action":"insert","lines":["i"]},{"start":{"row":1,"column":46},"end":{"row":1,"column":47},"action":"insert","lines":["r"]},{"start":{"row":1,"column":47},"end":{"row":1,"column":48},"action":"insert","lines":["e"]},{"start":{"row":1,"column":48},"end":{"row":1,"column":49},"action":"insert","lines":["c"]},{"start":{"row":1,"column":49},"end":{"row":1,"column":50},"action":"insert","lines":["t"]}],[{"start":{"row":1,"column":50},"end":{"row":1,"column":51},"action":"insert","lines":[","],"id":149}],[{"start":{"row":1,"column":51},"end":{"row":1,"column":52},"action":"insert","lines":[" "],"id":150},{"start":{"row":1,"column":52},"end":{"row":1,"column":53},"action":"insert","lines":["r"]},{"start":{"row":1,"column":53},"end":{"row":1,"column":54},"action":"insert","lines":["e"]},{"start":{"row":1,"column":54},"end":{"row":1,"column":55},"action":"insert","lines":["q"]},{"start":{"row":1,"column":55},"end":{"row":1,"column":56},"action":"insert","lines":["u"]},{"start":{"row":1,"column":56},"end":{"row":1,"column":57},"action":"insert","lines":["e"]},{"start":{"row":1,"column":57},"end":{"row":1,"column":58},"action":"insert","lines":["r"]}],[{"start":{"row":1,"column":57},"end":{"row":1,"column":58},"action":"remove","lines":["r"],"id":151}],[{"start":{"row":1,"column":57},"end":{"row":1,"column":58},"action":"insert","lines":["s"],"id":152},{"start":{"row":1,"column":58},"end":{"row":1,"column":59},"action":"insert","lines":["t"]},{"start":{"row":1,"column":59},"end":{"row":1,"column":60},"action":"insert","lines":[","]}],[{"start":{"row":1,"column":60},"end":{"row":1,"column":61},"action":"insert","lines":[" "],"id":153},{"start":{"row":1,"column":61},"end":{"row":1,"column":62},"action":"insert","lines":["u"]},{"start":{"row":1,"column":62},"end":{"row":1,"column":63},"action":"insert","lines":["r"]},{"start":{"row":1,"column":63},"end":{"row":1,"column":64},"action":"insert","lines":["l"]}],[{"start":{"row":1,"column":64},"end":{"row":1,"column":65},"action":"insert","lines":["_"],"id":154},{"start":{"row":1,"column":65},"end":{"row":1,"column":66},"action":"insert","lines":["f"]},{"start":{"row":1,"column":66},"end":{"row":1,"column":67},"action":"insert","lines":["o"]},{"start":{"row":1,"column":67},"end":{"row":1,"column":68},"action":"insert","lines":["r"]}],[{"start":{"row":12,"column":15},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":155}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":2},"action":"insert","lines":["''"],"id":156}],[{"start":{"row":13,"column":1},"end":{"row":13,"column":2},"action":"insert","lines":["a"],"id":157}],[{"start":{"row":13,"column":1},"end":{"row":13,"column":2},"action":"remove","lines":["a"],"id":158},{"start":{"row":13,"column":0},"end":{"row":13,"column":2},"action":"remove","lines":["''"]}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":1},"action":"insert","lines":["@"],"id":159},{"start":{"row":13,"column":1},"end":{"row":13,"column":2},"action":"insert","lines":["a"]},{"start":{"row":13,"column":2},"end":{"row":13,"column":3},"action":"insert","lines":["p"]},{"start":{"row":13,"column":3},"end":{"row":13,"column":4},"action":"insert","lines":["p"]}],[{"start":{"row":13,"column":4},"end":{"row":13,"column":5},"action":"insert","lines":["."],"id":160},{"start":{"row":13,"column":5},"end":{"row":13,"column":6},"action":"insert","lines":["r"]},{"start":{"row":13,"column":6},"end":{"row":13,"column":7},"action":"insert","lines":["o"]},{"start":{"row":13,"column":7},"end":{"row":13,"column":8},"action":"insert","lines":["u"]},{"start":{"row":13,"column":8},"end":{"row":13,"column":9},"action":"insert","lines":["t"]},{"start":{"row":13,"column":9},"end":{"row":13,"column":10},"action":"insert","lines":["e"]}],[{"start":{"row":13,"column":10},"end":{"row":13,"column":11},"action":"insert","lines":["9"],"id":161}],[{"start":{"row":13,"column":10},"end":{"row":13,"column":11},"action":"remove","lines":["9"],"id":162}],[{"start":{"row":13,"column":10},"end":{"row":13,"column":12},"action":"insert","lines":["()"],"id":163}],[{"start":{"row":13,"column":11},"end":{"row":13,"column":13},"action":"insert","lines":["''"],"id":164}],[{"start":{"row":13,"column":12},"end":{"row":13,"column":13},"action":"insert","lines":["/"],"id":165}],[{"start":{"row":13,"column":13},"end":{"row":13,"column":14},"action":"insert","lines":["g"],"id":166},{"start":{"row":13,"column":14},"end":{"row":13,"column":15},"action":"insert","lines":["e"]},{"start":{"row":13,"column":15},"end":{"row":13,"column":16},"action":"insert","lines":["t"]},{"start":{"row":13,"column":16},"end":{"row":13,"column":17},"action":"insert","lines":["_"]}],[{"start":{"row":13,"column":17},"end":{"row":13,"column":18},"action":"insert","lines":["r"],"id":167},{"start":{"row":13,"column":18},"end":{"row":13,"column":19},"action":"insert","lines":["e"]},{"start":{"row":13,"column":19},"end":{"row":13,"column":20},"action":"insert","lines":["c"]},{"start":{"row":13,"column":20},"end":{"row":13,"column":21},"action":"insert","lines":["e"]}],[{"start":{"row":13,"column":20},"end":{"row":13,"column":21},"action":"remove","lines":["e"],"id":168}],[{"start":{"row":13,"column":20},"end":{"row":13,"column":21},"action":"insert","lines":["i"],"id":169},{"start":{"row":13,"column":21},"end":{"row":13,"column":22},"action":"insert","lines":["p"]},{"start":{"row":13,"column":22},"end":{"row":13,"column":23},"action":"insert","lines":["e"]},{"start":{"row":13,"column":23},"end":{"row":13,"column":24},"action":"insert","lines":["s"]}],[{"start":{"row":14,"column":11},"end":{"row":14,"column":12},"action":"remove","lines":[":"],"id":170},{"start":{"row":14,"column":10},"end":{"row":14,"column":11},"action":"remove","lines":[")"]},{"start":{"row":14,"column":9},"end":{"row":14,"column":10},"action":"remove","lines":["("]},{"start":{"row":14,"column":8},"end":{"row":14,"column":9},"action":"remove","lines":["o"]},{"start":{"row":14,"column":7},"end":{"row":14,"column":8},"action":"remove","lines":["l"]},{"start":{"row":14,"column":6},"end":{"row":14,"column":7},"action":"remove","lines":["l"]},{"start":{"row":14,"column":5},"end":{"row":14,"column":6},"action":"remove","lines":["e"]},{"start":{"row":14,"column":4},"end":{"row":14,"column":5},"action":"remove","lines":["h"]}],[{"start":{"row":14,"column":4},"end":{"row":14,"column":5},"action":"insert","lines":["d"],"id":171},{"start":{"row":14,"column":5},"end":{"row":14,"column":6},"action":"insert","lines":["e"]}],[{"start":{"row":14,"column":5},"end":{"row":14,"column":6},"action":"remove","lines":["e"],"id":172},{"start":{"row":14,"column":4},"end":{"row":14,"column":5},"action":"remove","lines":["d"]}],[{"start":{"row":14,"column":4},"end":{"row":14,"column":5},"action":"insert","lines":["g"],"id":173},{"start":{"row":14,"column":5},"end":{"row":14,"column":6},"action":"insert","lines":["e"]},{"start":{"row":14,"column":6},"end":{"row":14,"column":7},"action":"insert","lines":["t"]},{"start":{"row":14,"column":7},"end":{"row":14,"column":8},"action":"insert","lines":["_"]},{"start":{"row":14,"column":8},"end":{"row":14,"column":9},"action":"insert","lines":["r"]},{"start":{"row":14,"column":9},"end":{"row":14,"column":10},"action":"insert","lines":["e"]}],[{"start":{"row":14,"column":10},"end":{"row":14,"column":11},"action":"insert","lines":["c"],"id":174},{"start":{"row":14,"column":11},"end":{"row":14,"column":12},"action":"insert","lines":["e"]}],[{"start":{"row":14,"column":11},"end":{"row":14,"column":12},"action":"remove","lines":["e"],"id":175}],[{"start":{"row":14,"column":11},"end":{"row":14,"column":12},"action":"insert","lines":["i"],"id":176},{"start":{"row":14,"column":12},"end":{"row":14,"column":13},"action":"insert","lines":["p"]},{"start":{"row":14,"column":13},"end":{"row":14,"column":14},"action":"insert","lines":["e"]}],[{"start":{"row":14,"column":14},"end":{"row":14,"column":15},"action":"insert","lines":["s"],"id":177}],[{"start":{"row":14,"column":15},"end":{"row":14,"column":17},"action":"insert","lines":["()"],"id":178}],[{"start":{"row":15,"column":18},"end":{"row":15,"column":19},"action":"remove","lines":["\""],"id":179},{"start":{"row":15,"column":17},"end":{"row":15,"column":18},"action":"remove","lines":["#"]},{"start":{"row":15,"column":16},"end":{"row":15,"column":17},"action":"remove","lines":["o"]},{"start":{"row":15,"column":15},"end":{"row":15,"column":16},"action":"remove","lines":["l"]},{"start":{"row":15,"column":14},"end":{"row":15,"column":15},"action":"remove","lines":["l"]},{"start":{"row":15,"column":13},"end":{"row":15,"column":14},"action":"remove","lines":["e"]},{"start":{"row":15,"column":12},"end":{"row":15,"column":13},"action":"remove","lines":["H"]},{"start":{"row":15,"column":11},"end":{"row":15,"column":12},"action":"remove","lines":["\""]},{"start":{"row":15,"column":10},"end":{"row":15,"column":11},"action":"remove","lines":[" "]},{"start":{"row":15,"column":9},"end":{"row":15,"column":10},"action":"remove","lines":["n"]},{"start":{"row":15,"column":8},"end":{"row":15,"column":9},"action":"remove","lines":["r"]},{"start":{"row":15,"column":7},"end":{"row":15,"column":8},"action":"remove","lines":["u"]},{"start":{"row":15,"column":6},"end":{"row":15,"column":7},"action":"remove","lines":["t"]},{"start":{"row":15,"column":5},"end":{"row":15,"column":6},"action":"remove","lines":["e"]},{"start":{"row":15,"column":4},"end":{"row":15,"column":5},"action":"remove","lines":["r"]}],[{"start":{"row":15,"column":4},"end":{"row":15,"column":5},"action":"insert","lines":["r"],"id":180},{"start":{"row":15,"column":5},"end":{"row":15,"column":6},"action":"insert","lines":["e"]},{"start":{"row":15,"column":6},"end":{"row":15,"column":7},"action":"insert","lines":["t"]},{"start":{"row":15,"column":7},"end":{"row":15,"column":8},"action":"insert","lines":["u"]},{"start":{"row":15,"column":8},"end":{"row":15,"column":9},"action":"insert","lines":["r"]},{"start":{"row":15,"column":9},"end":{"row":15,"column":10},"action":"insert","lines":["n"]}],[{"start":{"row":15,"column":10},"end":{"row":15,"column":11},"action":"insert","lines":[" "],"id":181},{"start":{"row":15,"column":11},"end":{"row":15,"column":12},"action":"insert","lines":["r"]},{"start":{"row":15,"column":12},"end":{"row":15,"column":13},"action":"insert","lines":["e"]},{"start":{"row":15,"column":13},"end":{"row":15,"column":14},"action":"insert","lines":["n"]},{"start":{"row":15,"column":14},"end":{"row":15,"column":15},"action":"insert","lines":["d"]},{"start":{"row":15,"column":15},"end":{"row":15,"column":16},"action":"insert","lines":["e"]},{"start":{"row":15,"column":16},"end":{"row":15,"column":17},"action":"insert","lines":["r"]}],[{"start":{"row":15,"column":11},"end":{"row":15,"column":17},"action":"remove","lines":["render"],"id":182},{"start":{"row":15,"column":11},"end":{"row":15,"column":26},"action":"insert","lines":["render_template"]}],[{"start":{"row":15,"column":26},"end":{"row":15,"column":28},"action":"insert","lines":["()"],"id":183}],[{"start":{"row":15,"column":27},"end":{"row":15,"column":29},"action":"insert","lines":["\"\""],"id":184}],[{"start":{"row":15,"column":28},"end":{"row":15,"column":29},"action":"insert","lines":["r"],"id":185},{"start":{"row":15,"column":29},"end":{"row":15,"column":30},"action":"insert","lines":["e"]},{"start":{"row":15,"column":30},"end":{"row":15,"column":31},"action":"insert","lines":["e"]},{"start":{"row":15,"column":31},"end":{"row":15,"column":32},"action":"insert","lines":["c"]}],[{"start":{"row":15,"column":31},"end":{"row":15,"column":32},"action":"remove","lines":["c"],"id":186},{"start":{"row":15,"column":30},"end":{"row":15,"column":31},"action":"remove","lines":["e"]}],[{"start":{"row":15,"column":30},"end":{"row":15,"column":31},"action":"insert","lines":["c"],"id":187},{"start":{"row":15,"column":31},"end":{"row":15,"column":32},"action":"insert","lines":["i"]},{"start":{"row":15,"column":32},"end":{"row":15,"column":33},"action":"insert","lines":["p"]},{"start":{"row":15,"column":33},"end":{"row":15,"column":34},"action":"insert","lines":["e"]},{"start":{"row":15,"column":34},"end":{"row":15,"column":35},"action":"insert","lines":["s"]}],[{"start":{"row":15,"column":35},"end":{"row":15,"column":36},"action":"insert","lines":["."],"id":188},{"start":{"row":15,"column":36},"end":{"row":15,"column":37},"action":"insert","lines":["h"]},{"start":{"row":15,"column":37},"end":{"row":15,"column":38},"action":"insert","lines":["t"]},{"start":{"row":15,"column":38},"end":{"row":15,"column":39},"action":"insert","lines":["m"]},{"start":{"row":15,"column":39},"end":{"row":15,"column":40},"action":"insert","lines":["l"]}],[{"start":{"row":15,"column":41},"end":{"row":15,"column":42},"action":"insert","lines":[","],"id":189}],[{"start":{"row":15,"column":42},"end":{"row":15,"column":43},"action":"insert","lines":[" "],"id":190},{"start":{"row":15,"column":43},"end":{"row":15,"column":44},"action":"insert","lines":["r"]},{"start":{"row":15,"column":44},"end":{"row":15,"column":45},"action":"insert","lines":["e"]},{"start":{"row":15,"column":45},"end":{"row":15,"column":46},"action":"insert","lines":["c"]},{"start":{"row":15,"column":46},"end":{"row":15,"column":47},"action":"insert","lines":["e"]}],[{"start":{"row":15,"column":46},"end":{"row":15,"column":47},"action":"remove","lines":["e"],"id":191}],[{"start":{"row":15,"column":46},"end":{"row":15,"column":47},"action":"insert","lines":["i"],"id":192},{"start":{"row":15,"column":47},"end":{"row":15,"column":48},"action":"insert","lines":["p"]},{"start":{"row":15,"column":48},"end":{"row":15,"column":49},"action":"insert","lines":["e"]},{"start":{"row":15,"column":49},"end":{"row":15,"column":50},"action":"insert","lines":["s"]}],[{"start":{"row":15,"column":50},"end":{"row":15,"column":51},"action":"insert","lines":["="],"id":193}],[{"start":{"row":15,"column":51},"end":{"row":15,"column":52},"action":"insert","lines":["m"],"id":194},{"start":{"row":15,"column":52},"end":{"row":15,"column":53},"action":"insert","lines":["o"]},{"start":{"row":15,"column":53},"end":{"row":15,"column":54},"action":"insert","lines":["n"]},{"start":{"row":15,"column":54},"end":{"row":15,"column":55},"action":"insert","lines":["g"]},{"start":{"row":15,"column":55},"end":{"row":15,"column":56},"action":"insert","lines":["o"]}],[{"start":{"row":15,"column":55},"end":{"row":15,"column":56},"action":"remove","lines":["o"],"id":195}],[{"start":{"row":15,"column":55},"end":{"row":15,"column":56},"action":"insert","lines":["o"],"id":196},{"start":{"row":15,"column":56},"end":{"row":15,"column":57},"action":"insert","lines":["."]},{"start":{"row":15,"column":57},"end":{"row":15,"column":58},"action":"insert","lines":["d"]},{"start":{"row":15,"column":58},"end":{"row":15,"column":59},"action":"insert","lines":["b"]}],[{"start":{"row":15,"column":59},"end":{"row":15,"column":60},"action":"insert","lines":["."],"id":197}],[{"start":{"row":15,"column":60},"end":{"row":15,"column":61},"action":"insert","lines":["r"],"id":198},{"start":{"row":15,"column":61},"end":{"row":15,"column":62},"action":"insert","lines":["e"]},{"start":{"row":15,"column":62},"end":{"row":15,"column":63},"action":"insert","lines":["c"]},{"start":{"row":15,"column":63},"end":{"row":15,"column":64},"action":"insert","lines":["i"]},{"start":{"row":15,"column":64},"end":{"row":15,"column":65},"action":"insert","lines":["p"]},{"start":{"row":15,"column":65},"end":{"row":15,"column":66},"action":"insert","lines":["e"]},{"start":{"row":15,"column":66},"end":{"row":15,"column":67},"action":"insert","lines":["s"]}],[{"start":{"row":15,"column":67},"end":{"row":15,"column":68},"action":"insert","lines":["."],"id":199},{"start":{"row":15,"column":68},"end":{"row":15,"column":69},"action":"insert","lines":["f"]},{"start":{"row":15,"column":69},"end":{"row":15,"column":70},"action":"insert","lines":["i"]},{"start":{"row":15,"column":70},"end":{"row":15,"column":71},"action":"insert","lines":["n"]},{"start":{"row":15,"column":71},"end":{"row":15,"column":72},"action":"insert","lines":["d"]}],[{"start":{"row":15,"column":72},"end":{"row":15,"column":74},"action":"insert","lines":["()"],"id":200}],[{"start":{"row":14,"column":17},"end":{"row":14,"column":18},"action":"insert","lines":[":"],"id":201}],[{"start":{"row":12,"column":15},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":202},{"start":{"row":13,"column":0},"end":{"row":14,"column":0},"action":"insert","lines":["",""]},{"start":{"row":14,"column":0},"end":{"row":15,"column":0},"action":"insert","lines":["",""]},{"start":{"row":15,"column":0},"end":{"row":16,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":1},"action":"insert","lines":["@"],"id":203},{"start":{"row":13,"column":1},"end":{"row":13,"column":2},"action":"insert","lines":["a"]},{"start":{"row":13,"column":2},"end":{"row":13,"column":3},"action":"insert","lines":["p"]},{"start":{"row":13,"column":3},"end":{"row":13,"column":4},"action":"insert","lines":["p"]},{"start":{"row":13,"column":4},"end":{"row":13,"column":5},"action":"insert","lines":["."]}],[{"start":{"row":13,"column":5},"end":{"row":13,"column":6},"action":"insert","lines":["r"],"id":204},{"start":{"row":13,"column":6},"end":{"row":13,"column":7},"action":"insert","lines":["o"]},{"start":{"row":13,"column":7},"end":{"row":13,"column":8},"action":"insert","lines":["u"]},{"start":{"row":13,"column":8},"end":{"row":13,"column":9},"action":"insert","lines":["t"]},{"start":{"row":13,"column":9},"end":{"row":13,"column":10},"action":"insert","lines":["e"]}],[{"start":{"row":13,"column":10},"end":{"row":13,"column":12},"action":"insert","lines":["()"],"id":205}],[{"start":{"row":13,"column":11},"end":{"row":13,"column":13},"action":"insert","lines":["''"],"id":206}],[{"start":{"row":13,"column":12},"end":{"row":13,"column":13},"action":"insert","lines":["/"],"id":207}]]},"ace":{"folds":[],"scrolltop":75,"scrollleft":0,"selection":{"start":{"row":13,"column":13},"end":{"row":13,"column":13},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":4,"state":"start","mode":"ace/mode/python"}},"timestamp":1562424710353}