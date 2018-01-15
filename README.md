# laptop-usage-stats
Usage statistics of a laptop(running osx/macos) based on the run-time of an Application

## Example of how to start the counter

You may choose to create a shell script which contains this 


`osascript -e 'tell app "Microsoft Outlook" to launch' ; python ~/Documents/Own/laptop-usage-stats/open-record-time.py`

## Example of how to end the counter

You may choose to create a shell script which contains this 
`osascript -e 'quit app "Microsoft Outlook"' ; python ~/Documents/Own/laptop-usage-stats/close-record-time.py ; cd ~/Documents/Own/time-stats ; git add *.json ; git commit -m "Application usage statistic uploaded at $(date)" ; git push origin master`
