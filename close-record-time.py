import json, datetime
from dateutil.parser import parse
from os.path import expanduser

# build your home directory
homedir = expanduser("~")

# calculate the date for the day
date_today =  datetime.date.today()
date_today = date_today.isoformat()

# test with a new date?
#date_today = "2018-01-16"

# calculate the time for today
time_today = datetime.datetime.now()
time_today = time_today.isoformat()

# opening the dictionary stored from when the Application was opened from the temp file created in open-record-time.py
temp_filename = 'temp-starttime.json'
with open ('%s/Documents/Own/laptop-usage-stats/%s'%(homedir,temp_filename)) as temp_json_file:
    temp_dict = json.load(temp_json_file)


# adding End Time to temp_dict
temp_dict['End Time'] = time_today

# calculating date difference
d1 = parse(temp_dict['End Time'])
d0 = parse(temp_dict['Start Time'])

diff = d1 - d0 # this represents the difference since the things done
diff = str(diff)

# write the diff to the temp dict
temp_dict['Total Time'] = diff

# read the current and main disc 
#temp_dict = json.dumps(temp_dict)
main_filename = 'usage_statistics.json'

# This is the main file where all the data will be stored, you may choose to upload it to a repository of your choosing. 
# This path may be different from the path of the temp file, but needs to exist with appropriate permissions
# Also ensure that this file ^ exists with the appropriate permissions and contains this   {"Statistics": {}}
# See also README


with open ('%s/Documents/Own/time-stats/%s'%(homedir,main_filename)) as json_fila:
    main_dict = json.load(json_fila)

# append the temporary calculated dict to the main disc, write and finish

main_dict['Statistics'][date_today] = temp_dict

# write the main dict to the file and finish!
with open ('%s/Documents/Own/time-stats/%s'%(homedir,main_filename), 'w') as outfile:
    json.dump(main_dict, outfile, indent=4, sort_keys=True)
