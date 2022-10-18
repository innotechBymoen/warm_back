from flask import request, Flask, make_response
import json
from dbhelpers import run_statement
from apihelpers import check_endpoint_info
import dbcreds

app = Flask(__name__)

@app.get('/api/gifs')
def get_restaurant():
    results = run_statement('CALL get_gifs()')
    if(type(results) == list):
        res_json = json.dumps(results, default=str)
        return make_response(res_json, 200)
    else:
        return make_response("Sorry, there was an error getting the gifs", 500)

# FIX ME WITH PROPER RUNNING!
if(dbcreds.production_mode == True):
    print("Running in Production Mode")
    import bjoern # type: ignore
    bjoern.run(app, "0.0.0.0", 5063)
else:
    from flask_cors import CORS
    CORS(app)
    print("Running in Testing Mode!")
    app.run(debug=True)
