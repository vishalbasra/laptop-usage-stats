# laptop-usage-stats
Usage statistics of a laptop(running osx/macos) based on the run-time of an Application

## Example of how to start the counter
`osascript -e 'tell app "Microsoft Outlook" to launch' ; python ~/Documents/Own/laptop-usage-stats/open-record-time.py`

## Example of how to end the counter
`osascript -e 'quit app "Microsoft Outlook"' ; python ~/Documents/Own/laptop-usage-stats/close-record-time.py`
