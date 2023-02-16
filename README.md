# Pr Closer

Tool to automate the process of closing all of the open pull requests on a gh organization

## Getting Started

* run `python3 -m venv venv` to create a virtual enviroment
* run  `. ./venv/bin/activate` to enter the virutal enviroment
* run `pip3 -r requirements.txt` to install the required packages
* `touch .env`, add a [classic github token](https://github.com/settings/tokens/new) with all auth scopes to the `.env` file like so:
```sh
GH_TOKEN=< your github token >
```
* run `python3 main.py < org name >` to run the script and close all open prs

example usage: 
```sh
$ python3 main.py WDI-SEA

Closing pull requests on command-line-murder-mystery, repo 1 of 463
Closing pull requests on google-shopping-conditionals-loops, repo 2 of 463
Closing pull requests on google-shopping-functions, repo 3 of 463
Closing pull requests on tic-tac-toe, repo 4 of 463
Closing pull requests on iterators-reddit, repo 5 of 463
Closing pull requests on jquery-todo-list, repo 6 of 463
	Closing pulls for https://api.github.com/repos/WDI-SEA/jquery-todo-list/pulls/175
Closing pull requests on ajax-reddit-slideshow, repo 7 of 463
	Closing pulls for https://api.github.com/repos/WDI-SEA/ajax-reddit-slideshow/pulls/208
Closing pull requests on bootstrap-mockups, repo 8 of 463
	Closing pulls for https://api.github.com/repos/WDI-SEA/bootstrap-mockups/pulls/71
	Closing pulls for https://api.github.com/repos/WDI-SEA/bootstrap-mockups/pulls/70
	Closing pulls for https://api.github.com/repos/WDI-SEA/bootstrap-mockups/pulls/69
...
```
