## AskGPT
Responds to /r/AskReddit posts using an OpenAI GPT-3 model trained on the top 1000 most upvoted posts and their top comments.

[Reddit account using this model](https://www.reddit.com/u/OrganRobber) - **The account has since been banned since Reddit doesn't allow bots.**



I scraped the Reddit data using [PRAW](https://praw.readthedocs.io/en/stable/). I would have used more than 1000 entries but OpenAI's free trial usage only allows a certain amount of spending and this dataset already uses half of it. On top of that, Reddit's API has a limit on how many submissions you can pull at once, which, you guessed it, is 1000.

## How to train the model and use it
1. Install the [latest version of Python](https://www.python.org/downloads/), make sure to add to PATH
2. Create an API key on [OpenAI's site](https://platform.openai.com/account/api-keys)
3. Create a [Reddit app](https://www.reddit.com/prefs/apps)
4. Clone the repository, then navigate to its directory and run the following commands:
```
  $ pip install -r requirements.txt
  $ openai api fine_tunes.create -t data.jsonl -m text-davinci-003
```
5. Wait until the fine tune is completed, you can check with:
```
  $ openai api fine_tunes.follow -i <YOUR_FINE_TUNE_JOB_ID>
```
6. After the fine tune is done, run this command and obtain the name from the latest response's 'fine_tuned_model' field:
```
  $ openai api fine_tunes.list
```
7. Set the variables at the top of AskGPT.py

You can then run the file. If you want it to run every so often set up a scheduler (I used Heroku Schedule)
