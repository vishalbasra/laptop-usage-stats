import json, datetime
from os.path import expanduser
# calculate the time
time_today = datetime.datetime.now()
time_today = time_today.isoformat()

# create a statistics dictionary
stat_dict = dict()

# Note the time of writing the application
stat_dict['Start Time'] = time_today

# write the following to a temporary file
homedir = expanduser("~")
filename = 'temp-starttime.json'
with open ('%s/Documents/Own/laptop-usage-stats/%s'%(homedir,filename), 'w') as outfile:
    json.dump(stat_dict, outfile)
