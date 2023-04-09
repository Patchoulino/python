import argparse
from flask import Flask, render_template
import datetime

app = Flask(__name__)

parser = argparse.ArgumentParser()
parser.add_argument('--port', type=int, default=5001, help='port number')
parser.add_argument('--countdown-file', type=str, default='countdown.txt', help='path to countdown file')
args = parser.parse_args()

@app.route('/')
def countdown():
    with open(args.countdown_file, 'r') as f:
        lines = f.readlines()
    events = []
    for line in lines:
        date_str, name = line.strip().split('|')
        date_str = str(datetime.datetime.now().year) + "-" + date_str
        date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
        if date_obj > datetime.datetime.now():
            events.append((date_obj, name))
    events.sort()
    if not events:
        date_str, name = "", "No upcoming events"
    else:
        date_obj, name = events[0]
        date_str = date_obj.strftime('%b %d, %Y %H:%M:%S')
    return render_template('countdown.html', date=date_str, name=name)

if __name__ == '__main__':
    app.run(debug=True, port=args.port, host='0.0.0.0')
