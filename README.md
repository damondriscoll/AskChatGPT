## AskChatGPT
Responds to /r/AskReddit posts using OpenAI's GPT-3 model trained on the top 1000 most upvoted posts.

[Reddit account using this script](https://www.reddit.com/u/OrganRobber)

## How to train the model
1. Create an API key on [OpenAI's site](https://platform.openai.com/account/api-keys)
2. Create a [Reddit app](https://www.reddit.com/prefs/apps)
3. Set the variables for the OpenAI key, the
4. Clone the repository, then navigate to its directory and run the following commands
```
$ pip install -r requirements.txt
$ openai api fine_tunes.create -t data.jsonl -m text-davinci-003
$ openai api fine_tunes.list
```
5. The last command will list all fine tunes; the latest one should be our fine tuned model.
6.
