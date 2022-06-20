
# chat-channel

###  Requirements
- Python ( 3.9 + )
---
### Setup
- Create and Activate virtual environment
	> ### Windows
	>> `python -m venv venv`
	>> Creates a virtual environment.
	>> `venv\Scripts\activate`
	> ### Linux
	>> `pip install virtualenv`
	>> `virtualenv venv`
	>> Creates a virtual environment.
	>> `source venv\bin/activate`
- Install Dependencies
	> `pip install python-dotenv`
---
### How to Start
- Without any modification, this project will start locally(127.0.0.1) at PORT(33000)
1. Terminal 1
	> `python Server.py`
2. Terminal 2
	> `python Client.py`
	A new window will pop up and insert the name.

- To make multiple Clients Repeat Step 2 
- To exit after chatting : Type `{quit}` and send
---
### Issues
- Program will throw error if GUI stopped before giving `Name`
- Instead of GUI Horizontal bar, need a Text Wrap
> If you know the solution to the known bugs, create a PR with the solution.
---
### New Bugs
- Create a New issue in the Issues Page.
---

### Enjoy ...
