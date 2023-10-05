# Introduction to Python

This repository contains the files, libraries and applications for a Python development environment.

You'll set up this environment and use it to create a simple project of your choice. Here are a few
suggestions:
- Mad Libs
- Calculator
- Hangman
- Tic Tac Toe
- Blackjack

The goal of this project is to learn basic programming and get more comfortable working in an 
environment that's not visual. Building a website lets a developer see the results in a web 
browser and the kinds of applications we use every day have things like buttons to interact with,
but often these are powered by programs that can only be interacted with by text. Pressing that
button might send a text command to a different program running on a server, and an important
part of thinking like a developer is being able to understand a program's code without actually
seeing the results or have a visual way to interact with it.

After completing this project, you'll have an understanding of writing code in Python but also
ideas that apply to other programming languages. We'll use that and combine it with what you've
learned so far to create a web app using HTML, CSS, and Javascript.

First, though, you'll start by learning the basics of Python.

## Technical Introduction ## 
With this project, you'll be creating a new virtual environment in Docker. This will be the
workspace that you'll run your Python programs, since not every computer has Python installed.
This virtual environment will have Python preinstalled and everything set up to run Python
programs, but can only be interacted with using the terminal.

## Setting Up the Environment ##

You'll need 3 things first: a code editor, Docker Desktop, and the Github application. Keep track
of any questions as you go. There's going to be a lot of stuff here, which is easier to explain
once the environment is built. Really, all you need to know is that this will install and set up
everything you need to work on software projects.

### 1. Fork this Repository ###

Right now, this project isn't owned by you, so you'll need to create a copy of it that you own. Scroll back to
the top of this page (or go to https://github.com/passthefist/ dev_container) if you're not on it. Click the "Fork"
button to create a copy of this project for your Github account (forking just means creating a copy of a project).
It will take you to a prompt, where you can choose your user in the "Owner" dropdown and just keep the defaults for
the rest. Clicking the "Create Fork" button will create your own version  of this project owned by your account.
You can follow this video as an example.

https://github.com/passthefist/dev_container/assets/279303/49af98d3-ad88-4518-ba97-e96030523aec

### 2. Clone this repository locally ###

Right now, the code for the project only exists on the GitHub website, but you'll need it to be
on your computer to work on. First, open the GitHub Desktop app on your computer, then click the
"Clone a Repository From the Internet" button. A [code repository](docs/Glossary.md#code-repository)
is where all the code for a software project is stored, and cloning is a term Git uses for downloading
the code in a repository and creating a copy on your computer.

In the upper left corner of the Github Desktop app, you can search for your projcets, which are called
[repositories](docs/Glossary.md#code-repository) by Git and GitHub. Choose this one (it should be called "dev_container")
to create a copy of the repository to work with on your computer. This is called "cloning", a term you'll see
while in the Github Desktop App or Github Website. Once you do, it will download the code for this project
so you can work with it and use the Github Desktop app to upload your code changes to be backed up on the
GitHub website so the code is shown as part of a portfolio of projects and your website is published on
the internet.

https://github.com/passthefist/dev_container/assets/279303/99ec12f5-b2a5-4763-bc85-d99a23aabf25

You should then see this screen once it's done, and you can open the files in your code editor by clicking 
this button. Once the full environment is set up, you'll be able to use Git to save your changes. 

![opening code repo](docs/img/first-repo.png)

### 3. Start the Python Workspace Container ###

The easiest way to do this is using the command line in Visual Studio Code. The [command line](docs/Glossary.md#command-line-console)
is a more powerful way developers, hackers, and really anyone doing I.T. work interact with computers. Typically, we interact
with computers graphically with a mouse and all that, but the command line is more primitive. It only takes text based commands and
only shows text based output. A user types a command on the prompt line and hits enter to run it, which is why it's called
the command line interface. The results of the command are shown on the next line as the output. 

Another name for the command line is the terminal, and this video shows how to open it in Visual Studio Code. It also
shows a sample command to run. The command is called `echo`, which takes some text and echoes what was typed as output
on the next line after it's run when the user presses enter.

https://github.com/passthefist/dev_container/assets/279303/5c6051e5-3922-4e1b-8459-95320c8f74eb

Here, we'll be using it to build and run our server with the `docker-compose` command. It has 
options such as `build`, `up`, and `down` to build, start, and stop containers respectively.

First, create and build the server by typing `docker-compose build` in the prompt and hitting enter.
Then type `docker-compose up` and hit enter to run it. It should look similar to this video.

https://github.com/passthefist/dev_container/assets/279303/c61818f3-e1e3-4535-8c2b-32a416766767

**If you see an error message like this, make sure that the Docker Desktop app is running.**

```
error during connect: this error may indicate that the docker daemon is not running: Get "http://%2F%2F.%2Fpipe%2Fdocker_engine/_ping": open //./pipe/docker_engine: The system cannot find the file specified.
```

Once built, the container can be ran and managed from the Docker Desktop app. You can also use the 
`docker-compose up` and `docker-compose down` commands in a terminal to start and stop it respectively.
This video shows how to start it in the Docker Desktop app. If you're following this setup, it should
already be running and you can see that in the app, too.

https://github.com/passthefist/dev_container/assets/279303/0c0ca9e8-6498-49ed-afd2-31ccca4c77fe

### 4. Run the first example program ###

Connect to your Python workspace by typing the command `docker attach python_workspace` into a
terminal. This tells the `docker` program to run the `attach` command to attach your terminal to
a docker container. Here, the command will find the container named `python_workspace` (the one
you just created) and connect your terminal there. Importantly, this is a *different* terminal
than the one you initially opened which was running on your computer. Now, this terminal is
actually running on your virtual Python workspace.

Once there, you can run the `ls` command to get a list of all the files and folders in this
project. Refer to [this cheatsheet](docs/Commands-Cheatsheet.md) for common commands to navigate a 
terminal environment and an explanation of them.

Next, you can use the `cd` command to open the `examples` folder. Whenever you attach to your
python workspace to run the examples, you'll need to `cd` into the directory.

Try using `ls` to see what's in this folder. You'll see a bunch of files that end in `.py`,
which means they are Python program files. Open `hello_world.py` in your editor and run it
in your workspace with `python 1_hello_world.py`. This command tells Python to run the `1_hello_world.py`
program. Read through the code in the file and try to match it to the output.

## Next Steps ##

You've now set up everything you need to write and run Python programs. Before starting on your project,
work through some of the other programs in the examples folder to get a feel for Python.

Refer to [this cheatsheet](docs/Commands-Cheatsheet.md) for common commands to navigate a 
terminal environment and an explanation of them.

Start with opening `1_hello_world.py` in your code editor, then move through the rest in order. You can
run a program with the `python` command by typing the name of the file you want to run after the command.
For example, to run the `1_hello_world.py` program you'd use the command `python 1_hello_world.py`, which
tells Python to read the contents of the `1_hello_world.py` file and run it as a Python program. You can
run the other files in the same way, like `python 2_hello_world.py`

Think of these examples as little puzzles, and try to have fun understanding what they are doing,
changing any of the code if you feel like it's helpful.

### Starting an Interactive Python Session ###

You can also start an interactive Python session with just the `python` command and no file after it. It
will open a console that lets you try out some Python code line by line instead of running a given 
program file. Initially, it should look like this:

```
Python 3.8.3 (default, Jun  9 2020, 17:39:39) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

If you type a simple bit of code such as adding some numbers together and hit enter, it will run that
code and print the result on the next line.

```
Python 3.8.3 (default, Jun  9 2020, 17:39:39) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 1 + 2
3  
```

The interactive session is a real Python environment, so you can define functions and variables, and
they will be kept even for other lines of code (see the `3_intro_variables.py` and `9_function.py` files for more on variables and functions).

```
Python 3.8.3 (default, Jun  9 2020, 17:39:39) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> a = 4
>>> b = 5
>>> a + b
9   
>>> def add_3(num):
...     return num + 3
...
>>> add_3(7)
10
```