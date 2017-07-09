***"""Script to find duplicate files in present working directory or custom path"""***

#Description:
This script tries to list down the duplicate files in given path.

By default Present Working Directory is Taken.

You can also search for custom files in the path.

#Requirements:
Python 2.6+

#Instructions:
* Run as python duplicate-finder.py to list all the duplicate files in Present Working Directory.
* Script without additional arguments outputs results from current directory.
* Script with additional options give respective results.

#Usage:
* python duplicate-finder.py [OPTION]
* -s,--search - specific file name to search for.
* -p,--path - custom path to scan and print.
* -h,--help - Display help message.

#Note:
If you get "maximum recursion depth exceeded" error enable setrecursionlimit in duplicate_finderer.py and set value > 1000 default value is 1000.
