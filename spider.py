import database

_date_ = "2019/2/8 12:05"
_author_ = "xing"
from flask_sqlalchemy import SQLAlchemy

from flask import Flask, request
from app import creat_app
from flask import jsonify

app = creat_app()

@app.route("/api/search")
def search():
    """"""
    keyword = request.args.get("keyword")
    limit = request.args.get("limit")
    start = request.args.get("start")
    if limit and start and keyword:
        return_list = database.search_content(keyword, start, limit)
        print(return_list)
        print(len(return_list))
        number = database.search_content_number(keyword)
        print("number = " + str(number))

        return jsonify({"result_list": return_list, "total_number":number})
    else:
        return "hello world"

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=app.config["DEBUG"], threaded=True, port=5001)
