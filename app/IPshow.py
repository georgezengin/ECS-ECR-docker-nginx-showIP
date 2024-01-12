#import redis
from flask import Flask, request, render_template
import pytz
import socket
from datetime import datetime as dt

app = Flask(__name__)
#cache = redis.Redis(host='redis', port=6379)

#@app.route('/')
#def index():
#    return render_template('index.html')


#@app.route('/current_time', methods=['POST'])
#def current_time():
#    data = request.get_json()
#    timezone = data['timezone']
#    user_timezone = pytz.timezone(timezone)
#    current_time = dt.now(user_timezone).strftime("%d %B %Y, %H:%M:%S")
#    return current_time


hostname = socket.gethostname()   
IPAddr   = socket.gethostbyname(hostname) 

@app.route('/')
def ip():
    ip = IPAddr
    tm = dt.now().strftime("%d %B %Y, %H:%M:%S")
    #return f'<HTML><BODY><br><br><br><br><H1><center>Current date and time: [{tm}]<br><br>Host Name: [{hostname}] <br><br>IP Address: [{ip}]</center></H1></BODY></HTML>' #.format(ip)
    return f'''
        <!DOCTYPE html>
        <html>
        <head>
        </head>
        <body>
            <br><br><br><br><center>
            <h1>Current host date and time: [{tm}]</h1>
            <br><br>
            <h1>
            Host Name: [{hostname}]
            <br><br>
            IP Address: [{ip}]
            </h1>
            </center>
        </body>
        </html>
        '''


if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True,threaded=True) #,port=5000
