from flask import Flask
from flask import request
from strgen import StringGenerator as SG
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/jobs', methods=['POST'])
def jobs():
    jobRequest = request.json
    print jobRequest['jobId']
    print jobRequest['scriptId']
    scriptContent = jobRequest['scriptContent']
    print jobRequest['scriptRole']

    filename = SG("[\l\d]{10}").render()

    with open('/tmp/'+filename,'w') as f:
        f.write(scriptContent)

    
    return str(jobRequest)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='20523')
