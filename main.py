from flask import Flask, request, jsonify, abort
from flask_cors import CORS
import traceback
import litellm

from litellm import completion 
import os, dotenv
dotenv.load_dotenv()

######### LOGGING ###################
# log your data to slack, supabase
litellm.success_callback=["slack", "supabase"] # set .env SLACK_API_TOKEN, SLACK_API_SECRET, SLACK_API_CHANNEL, SUPABASE 

######### ERROR MONITORING ##########
# log errors to slack, sentry, supabase
litellm.failure_callback=["slack", "sentry", "supabase"] # .env SENTRY_API_URL

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'received!', 200

@app.route('/chat/completions', methods=["POST"])
def api_completion():
    data = request.json
    try:
        # pass in data to completion function, unpack data
        response = completion(**data) 
    except Exception as e:
        # call handle_error function
        return handle_error(data)
    return response, 200

@app.route('/get_models', methods=["POST"])
def get_models():
    try:
        return litellm.model_list
    except Exception as e:
        traceback.print_exc()
        response = {"error": str(e)}
    return response, 200

if __name__ == "__main__":
  from waitress import serve
  serve(app, host="0.0.0.0", port=5000, threads=500)

############### Advanced ##########################

################ ERROR HANDLING #####################
# implement model fallbacks, cooldowns, and retries
# if a model fails assume it was rate limited and let it cooldown for 60s
def handle_error(data):
    import time
    # retry completion() request with fallback models
    response = None
    start_time = time.time()
    rate_limited_models = set()
    model_expiration_times = {}
    fallback_strategy=['gpt-3.5-turbo', 'command-nightly', 'claude-2']
    while response == None and time.time() - start_time < 45: # retry for 45s
      for model in fallback_strategy:
        try:
            if model in rate_limited_models: # check if model is currently cooling down
              if model_expiration_times.get(model) and time.time() >= model_expiration_times[model]:
                  rate_limited_models.remove(model) # check if it's been 60s of cool down and remove model
              else:
                  continue # skip model
            print(f"calling model {model}")
            response = completion(**data)
            if response != None:
              return response
        except Exception as e:
          rate_limited_models.add(model)
          model_expiration_times[model] = time.time() + 60 # cool down this selected model
          pass
    return response


########### Pricing is tracked in Supabase ############