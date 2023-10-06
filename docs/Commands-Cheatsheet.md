# Command Line Overview

The command line is a fairly simple interface, with just a few core concepts needed to get started.

First, it takes a command typed by the user and runs it, showing the output line by line. When
finished, a new input line is shown to prompt another command from the user.

Second, just like a desktop environment, the command line has files and folders. Instead of clicking
on them to open a file, or run an application, or move a file from one folder to another, commands are 
used to do the same things. Folders are commonly called directories in the context of the command line.

Finally, the command line prompt exists in one directory at a time. With a desktop environment, you can
have multiple folders open at once and view what's in them at the same time. In a terminal, you navigate
in one directory at a time. This is called the working directory, and some commands interact with the
current working directory. For example, the `ls` command will show the contents of the current working
directory, like opening and viewing the contents of a folder in the desktop environment.

Directories are organized in a hierachy, where a topmost directory contains some other directories, and
those contain more directories, and so on. This topmost directory is called the root directory, since all
other directories live under this one. In windows, this root directory is usually called "C://" and in
UNIX, Linux, and macOS the root directory is just "/". The path from this root directory to any given 
one is the name of each directory separated by a forward slash. For example, a directory called 'images' 
that's in a directory called 'home', which is in a directory called 'root' would have a path like 'C://
home/images' in windows and "/home/images" in Linux and macOS.

The Python workspace you're working in is a Linux environment, so it uses the "/home/images" style. If
a photo named "sunset.jpg" was stored in the images directory, it would have a path like
"/home/image/sunset.jpg". These are examples of absolute paths, which describe how to navigate from the
root directory to another directory or file. To follow the path, you start at the root, then move to the
next directory, and then the next one, and so on until you get to the file or directory at the 
end of the path.

Another way to specify a file or directory is with a relative path, which starts with the current
working directory instead of the root. For example, for that same "sunset.jpg" file, if the current
working directory is the home directory, then the relative path to the file would be
"./images/sunset.jpg". The dot at the start of the path refers to the current directory. If the
working directory was the "images" directory, then the path to the file would be "./sunset.jpg".
Similar to the dot that means the current directory, two dots means the directory above the current one.

Understanding directories is important for navigating the command line, especially understanding
the concept of a working directory. Some of the common commands are described below, with more examples
to further explain how to navigate the command line.

### Commands
There's many commands to use with the command line. These are the ones that will be needed for your
Python workspace.

cd: **C**hange **d**irectory. Used like `cd ./home/projects`, which will change the current working 
directory to the one specified. It can also be used like `cd ..` which will change to the directory
above the current one. If the currentworking directy 
ls: **L**i**s**t directory contents. Used like `ls`, which will show all the files and directories in the current working directory.
pwd: **P**rint **w**orking directory. Used like `pwd`, which will show the path to the current working directory.
cp: **C**o**p**y file or directory. Used like `cp images/wedding backup/images/wedding`, which will copy the directory on the left to a new directory on the right at the path `where/to/put/it`. There must be a directory with the path `where/to/put` already, and it will create a new directory named `it` in the `put`
mv: **M**o**v**e or rename file or directory.
cat: Display the contents of a file.
echo: Print text to the terminal.
