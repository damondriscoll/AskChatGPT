import openai
import praw
import os

# Either set the environmental variables for these or replace them as strings
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
APP_CLIENT_ID = os.getenv("APP_CLIENT_ID")
APP_CLIENT_SECRET = os.getenv("APP_CLIENT_SECRET")
MY_REDDIT_PASSWORD = os.getenv("MY_REDDIT_PASSWORD")
MY_REDDIT_USERNAME = os.getenv("MY_REDDIT_USERNAME")
FINE_TUNED_MODEL = os.getenv("FINE_TUNED_MODEL")


reddit = praw.Reddit(
    client_id = APP_CLIENT_ID,
    client_secret = APP_CLIENT_SECRET,
    password = MY_REDDIT_PASSWORD,
    user_agent = "Fetches a random rising post on /r/AskReddit (by u/Enodma) https://github.com/damondriscoll/AskChatGPT",
    username = MY_REDDIT_USERNAME
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
