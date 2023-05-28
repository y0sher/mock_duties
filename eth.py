from flask import Flask, render_template
from flask_sock import Sock
import time
import random
import json


app = Flask(__name__)
sock = Sock(app)

duty_list = ['PROPOSER', 'ATTESTER', 'AGGREGATOR', 'SYNC_COMMITTEE']
validators = ['1', '2', '3', '4', '5', '6']
validator_index = {}

def generate_duty():
    height = 0
    duty = ""
    validator = validators[random.randint(0, len(validators)-1)]
    if validator not in validator_index:
        height = 0
        duty = duty_list[0]
        validator_index[validator] = { 'last_height': height, 'heights': { height: 0 } }
        
    else:
        height = validator_index[validator]['last_height']
        lduty = validator_index[validator]['heights'][height]
        if lduty is len(duty_list)-1:
            height = height+1
            duty = duty_list[0]
            validator_index[validator]['last_height'] = height
            validator_index[validator]['heights'][height] = 0
        else:
            duty = duty_list[validator_index[validator]['heights'][height]+1]
            validator_index[validator]['heights'][height] = validator_index[validator]['heights'][height]+1
            
    return {'validator': validator, 'duty': duty, 'height': height}
        

@sock.route('/ws')
def duties(ws):
    while True:
        time.sleep(3)
        ws.send(json.dumps(generate_duty()))
        

if __name__ == "__main__":
    app.run()