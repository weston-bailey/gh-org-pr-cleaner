from dotenv import load_dotenv
import os
import sys
from lib.PullCloser import PullCloser

def main():
    load_dotenv()
    GH_TOKEN = os.environ["GH_TOKEN"]
    if len(sys.argv) < 2:
        print("script requires a valid github organization as an argument")
        return
    ORG = sys.argv[1]

    pr_bot = PullCloser(GH_TOKEN, ORG)
    pr_bot.run()


if __name__ == "__main__":
    main()
