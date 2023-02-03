import openai
import praw
import os

reddit = praw.Reddit(
    client_id = os.getenv("MY_CLIENT_ID"),
    client_secret = os.getenv("MY_CLIENT_SECRET"),
    password = os.getenv("MY_PASSWORD"),
    user_agent = "Fetches a random rising post on /r/AskReddit (by u/Enodma) https://github.com/damondriscoll/AskChatGPT",
    username = os.getenv("MY_USERNAME")
)

my_submission = ""
for submission in reddit.subreddit("AskReddit").random_rising():
    if "[Serious]" not in submission.title: # Ignores [Serious] posts because I don't want to piss anyone off with an incoherent/inappropriate response
        my_submission = submission
        break

print(my_submission.title)

completions = openai.Completion.create(
    engine = os.getenv("MY_OPEN_AI_MODEL"),
    prompt = str(my_submission.title).encode("ascii", errors="ignore").decode() + "\n\n###\n\n",
    max_tokens = 1024,
    n = 1,
    stop = [" END OF THE COMMENT"]
)

print(completions.choices[0].text[1:])

my_submission.reply(completions.choices[0].text[1:])