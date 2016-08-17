from flask import Flask
from flask import request
from strgen import StringGenerator as SG
import json
import os
import subprocess

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

    os.chmod('/tmp/'+filename, 0o777)

    result = subprocess.check_output('/tmp/'+filename, shell=True)

    os.remove('/tmp/'+filename)
    
    #return str(jobRequest)
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='20523')
