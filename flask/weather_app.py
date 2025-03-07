import sqlite3
from flask import Flask, jsonify, render_template
from flask_swagger_ui import get_swaggerui_blueprint
import json
import pandas as pd


app = Flask(__name__)

# Configure Swagger UI
SWAGGER_URL = '/swagger'
API_URL = 'http://localhost:5000/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Sample API"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/swagger.json')
def swagger():
    with open('/app/flask/swagger.json', 'r') as f:
        return jsonify(json.load(f))


@app.route("/")
def landing():
    return render_template("home.html")

    
@app.route("/get_data", methods=['GET'])
def get_data():
    
    con = sqlite3.connect("/app/sqlite/weather.db")

    cursor = con.cursor()

    results = cursor.execute("SELECT * FROM WEATHER LIMIT 10")
    results = results.fetchall()
    
    results_dict = []
    for row in results:
        results_dict.append(
            {
                "date": row[0],
                "max_temp": row[1],
                "min_temp": row[2],
                "percipitation": row[3]
            }
        )
    
    # print({"Results": results_dict})
    
    return {"Results": results_dict}

if __name__ == '__main__':  
   app.run(debug=False, host="0.0.0.0", port=5000)