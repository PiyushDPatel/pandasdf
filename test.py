import pandas as pd
import numpy as np
from datetime import date
import datetime
import json



def json_serial(obj):
	"""JSON serializer for objects not serializable by default json code"""
	if isinstance(obj, date):
		serial = obj.isoformat()
		return serial
	raise TypeError ("Type not serializable")


df = pd.read_csv('test.csv', index_col=0)

numdays = 14
base = datetime.datetime.today().date()
date_list = [base - datetime.timedelta(days=x) for x in range(0, numdays)]
dates = pd.DataFrame(date_list)
dates.columns = ['date']

df.date = pd.to_datetime(df.date)
dates.date = pd.to_datetime(dates.date)


#merge the complete dates with the dateframe
df = pd.merge(dates, df, on=['date'], how='left')
#order by dates
df = df.sort_values('date',ascending=True)
#make dates json serializable
df['date'] = df.date.apply(json_serial)

#insert new code here


print df