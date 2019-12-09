import json
import datetime, time

FILENAME = 'data.json'
with open(FILENAME, 'r') as f:
	data = json.loads(f.read())

META = data['Meta Data']
WEEKLY = data['Weekly Adjusted Time Series']

DATES  = [time.mktime(datetime.datetime.strptime(s, "%Y-%m-%d").timetuple()) for s in WEEKLY.keys()][::-1]
OPEN   = [float(WEEKLY[i]['open']) for i in WEEKLY]
HIGH   = [float(WEEKLY[i]['high']) for i in WEEKLY]
LOW    = [float(WEEKLY[i]['low']) for i in WEEKLY]
CLOSE  = [float(WEEKLY[i]['close']) for i in WEEKLY]
VOLUME = [int(WEEKLY[i]['volume']) for i in WEEKLY]
DIV    = [float(WEEKLY[i]['dividend amount']) for i in WEEKLY]
