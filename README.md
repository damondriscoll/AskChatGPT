## AskChatGPT
Responds to /r/AskReddit posts using OpenAI's GPT-3 model trained on the top 1000 most upvoted posts and their top comments.

[Reddit account using this script](https://www.reddit.com/u/OrganRobber)

## How to train the model and run the script
1. Create an API key on [OpenAI's site](https://platform.openai.com/account/api-keys)
2. Create a [Reddit app](https://www.reddit.com/prefs/apps)
3. Clone the repository, then navigate to its directory and run the following commands:
```
  $ pip install -r requirements.txt
  $ openai api fine_tunes.create -t data.jsonl -m text-davinci-003
```
4. Wait until the fine tune is completed, you can check with:
```
  $ openai api fine_tunes.follow -i <YOUR_FINE_TUNE_JOB_ID>
```
5. After the fine tune is done, run this command and obtain the name from the latest response's 'fine_tuned_model' field:
```
  $ openai api fine_tunes.list
```
6. Set the variables at the top of AskChatGPT.py

You can then run the file, if you want it to run every so often set up a schedule (I used Heroku Schedule)
