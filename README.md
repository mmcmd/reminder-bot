# reminder-bot
Short little script to remind me on the first of every month to post in a channel.
Uses crontab (0 0 1 * *) to call the script

## Config file
A config.json file need to be created in the same directory with remiderstat.py
Below is an example of the config.json file.<br/>
<pre>
{
	"token":"your-token",
	"channel":"your-channel-id",
	"message":"your-message"
}
</pre>
## To-do

Error handling

Logging
