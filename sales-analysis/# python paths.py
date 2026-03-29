# python paths 

Python paths
Understanding how Python finds files

​
The most confusing part of Python
Understanding paths is probably the most confusing part when starting with Python. You’ll make mistakes with file paths and imports, and that’s totally fine. That’s how everyone learns.
This page gives you a quick introduction. Some parts might not be completely clear right now, but as you practice, it will click. Come back to this page when you run into path issues - it happens to everyone!
​
The mental model
When working with multiple files, always think about two things:
Where am I? - What folder is my Python script in?
Where do I want to go? - What file or module do I need?
Then navigate:
Going down into subfolders: Use / for files, . for imports
Going up to parent folders: Use ../ for files, add to sys.path for imports
Same folder: Just use the filename
# From script.py, accessing different locations:
"data/sales.csv"        # Down into data folder
"../config.json"        # Up one level
"helper.py"             # Same folder

# For imports:
import helper           # Same folder - no path needed!
import data.processor   # Down into data folder

# Parent folder imports need sys.path:
import sys
sys.path.append("..")   # Add parent to path
import parent_module    # Now you can import
​
The simple rule
When Python runs, it has a “current working directory” - the folder it’s currently in. All file paths start from there.
import os

# See where Python is right now
print(os.getcwd())
Try this - it shows you exactly where Python is looking for files.
​
Finding your files
Let’s say you have this structure:
my-project/
├── script.py
├── data.txt
└── folder/
    └── other.txt
If you run script.py:
# Python can find these:
open("data.txt")           # Same folder
open("folder/other.txt")   # Subfolder

# Python CAN'T find these (they don't exist from here):
open("other.txt")          # Wrong! It's in a subfolder
open("../parent.txt")      # Looking in parent folder
​
Files vs modules - key difference
Python handles regular files and Python modules differently:
Regular files (CSV, TXT, JSON):
Use open() or file-reading functions
Need the exact path from your current directory
Use forward slashes: data/sales.csv
# Reading a CSV file - needs exact path
with open("data/sales.csv", "r") as file:
    content = file.read()
Python modules (importing code):
Use import statements
Python searches in multiple locations (sys.path)
Use dots instead of slashes: folder.module
# Importing a module - Python searches for it
import mymodule                    # Looks for mymodule.py
from folder.utils import helper    # Looks for folder/utils.py
​
How Python finds modules
Python looks for modules (other .py files) in specific places. You can see these places:
import sys
print(sys.path)  # List of folders Python checks
The list includes:
The folder containing your script
Python’s built-in library folders
Installed packages
​
Adding your own folders
Sometimes you need Python to look in additional places:
import sys

# Add a folder to Python's search path
sys.path.append("/path/to/my/folder")

# Now you can import from that folder
import mymodule
Common example - importing from a parent folder:
import sys
import os

# Go up one level from current script
parent = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parent)
​
Common mistakes
FileNotFoundError: No such file or directory

ModuleNotFoundError: No module named 'X'

Mixing up files and modules

Running from the wrong folder

Using backslashes on Mac/Linux

​
Keep it simple
Remember, everyone struggles with paths at first. For now:
Keep related files in the same folder
Use the VS Code play button (it’s predictable)
When confused, print os.getcwd() to see where you are
Come back to this page when you hit path errors
The mental model: Know where you are, know where you want to go, then navigate with / for files. For imports, same folder needs no path, subfolders use ., parent folders need sys.path.