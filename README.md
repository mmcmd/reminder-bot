# reminder-bot
Short little script to remind me on the first of every month to post in a channel.
Uses crontab (0 0 1 * *) to call the script

## Installing dependencies

The project dependencies are listed in a Pipfile. Use pipenv to trigger python virtual environment:

	cd reminder-bot
	pipenv install

Pipenv uses virtualenv to create a python environment with all the dependencies listed in the Pipfile. Before running the reminder.py script, you must first activate the environment:

	pipenv shell

If you wish to deactivate the environment use the command

	exit

## Config file
A /config/config.json file need to be created in the same directory with reminderstat.py
Below is an example of the config.json file.<br/>
<pre>
{
	"token":"your-token",
	"channel":"your-channel-id",
	"message":"your-message"
}
</pre>

## Script arguments
The following arguments can be passed to the script

| Short | Long             | Type   | Description |
|-------|------------------|--------|-------------|
| -c    | --config         | string | config file path, default is set to "./config/config.json" |

## Running the script using cron

We can use cron to automatically run the script periodically in order to keep it up-to-date. You will need either a macOS computer or Linux server to use cron.

1. Set up config file with specified template in `Config file` section
2. Run `crontab -e` to open the cron editor
3. Use the following format to create a line for your cron
    ```
    * * * * * command to be executed
    - - - - -
    | | | | |
    | | | | ----- Day of week (0 - 7) (Sunday=0 or 7)
    | | | ------- Month (1 - 12)
    | | --------- Day of month (1 - 31)
    | ----------- Hour (0 - 23)
    ------------- Minute (0 - 59)
    ```
    For example, to run the script with default config file at 9 AM everyday, insert the following line

    ```
    0 9 * * * cd /home/tduong/remider-bot && /usr/local/bin/pipenv run python reminder.py
    ```

    Note: run `which pipenv` to identify your pipenv path. Mine is "/usr/local/bin/pipenv"

	  To trigger the script with `your-config.json` at 9 AM everyday, run the below
    ```
    0 9 * * * cd /home/tduong/remider-bot && /usr/local/bin/pipenv run python reminder.py -c ./config/your-config.json
    ```
	  To run schedule the script with pipenv run, the follwing line
	  ```
    0 9 * * * cd /home/tduong/remider-bot && /usr/local/bin/pipenv run python reminder.py -c ./config/your-config.json
    ```
## To-do

See projects tab
