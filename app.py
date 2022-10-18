from flask import request, Flask
import json
from dbhelpers import run_statement
from apihelpers import check_endpoint_info

app = Flask(__name__)

@app.get('/api/gifs')
def get_restaurant():
    results = run_statement('CALL get_gifs()')
    if(type(results) == list):
        res_json = json.dumps(results, default=str)
        return res_json
    else:
        return "Sorry, there was an error getting the gifs"

# FIX ME WITH PROPER RUNNING!
app.run(debug=True)