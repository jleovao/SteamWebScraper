# SteamWebScraper
This is a personal project I developed while learning Python. When executed, this Python script will extract data from [Steam](http://store.steampowered.com/), which is a digital distribution platform developed by Valve Corporation. I use this data from the Steam market to display the current top selling games that support macOS (since I'm using a Macbook), its tags (e.g Action, Strategy, Multiplayer), the current price of the game, and a link to the game provided by Steam. The extracted data is then parsed and saved into a csv file and can be viewed through many apps. My preference is Microsoft Excel or the Numbers spreadsheet app. 

## Getting Started
Download the project to any directory and make sure you have the software neccessary to run this project.

### Prerequisites
This project requires Python. Check if it is already installed on your computer. If it isn't, download Python:

* [Python](https://www.python.org/downloads/) - The programming language used

For Windows users, install Anaconda instead of Python

* [Anaconda](https://www.anaconda.com/download/#wi) - Data Science platform for Windows users

Optional: Install the Sublime Text text editor

* [Sublime Text](https://www.sublimetext.com/3) - Pretty neat text editor

### Install dependencies
Open the terminal and install the Python package Beautiful Soup with this command:

```
pip install bs4
```

Beautiful Soup is a Python package that parses HTML and XML documents and will enable us to web scrape.

## Running the script
This python script can be run through the terminal, or through Sublime Text.

### Linux Terminal
Open the linux terminal and 'cd' into the project directory containing the project files. Run the project by entering this command:

```
python steam_specials_web_scrape.py
```

Optional: You can make the project an executable first, then run the project using a shorter command. To do this, make the project executable:

```
chmod +x steam_specials_web_scrape.py
```

Then run the project:

```
./steam_specials_web_scrape.py
```

### Sublime Text
Open the python file through any Sublime Text editor. Make sure the syntax is set to Python. You can make sure with this command:

```
⌘ + ⇧ + P  (Command + shift + P)
```

and then enter this command in the text field:

```
Set Syntax: Python
```

If the Syntax is already in Python, just enter this command to run the script:

```
⌘ + B  (Command + B)
```

## Author
Joseph Leovao
