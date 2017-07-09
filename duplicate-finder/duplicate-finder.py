'''**************************************** LIBRARIES ******************************************'''
import os
from argparse import ArgumentParser
from Queue import Queue
from sys import argv,setrecursionlimit

'''*************************************** GLOBAL VARIABLES ************************************'''
setrecursionlimit(3000) #if you get "maximum recursion depth exceeded" error enable this and set value > 1000 default value is 1000
q=Queue()
file_dict={}

'''*************************************** FUNCTIONS *******************************************'''
# returns a list of files in given location
def files(pat):
    files=[x for x in os.listdir(pat) if not x.startswith(".") and os.path.isfile(os.path.join(pat,x))]
    return files

# returns a list of directories in given location
def directories(pat):
    dirs=[x for x in os.listdir(pat) if not x.startswith(".") and os.path.isdir(os.path.join(pat,x))]
    return dirs

# returns a list of hidden files in given location
def hid_fil(pat):
    hidden_files=[x for x in os.listdir(pat) if x.startswith(".") and os.path.isdir(os.path.join(pat,x))]
    return len(hidden_files)

# returns a list of hidden directories in given location
def hid_dir(pat):
    hidden_dirs=[x for x in os.listdir(pat) if x.startswith(".") and os.path.isfile(os.path.join(pat,x))]
    return len(hidden_dirs)

# main function to get files,dirs,hidden files,hidden dirs
def main(location):
    #global file_dict
    b=directories(location)
    for item in b:
        q.put(os.path.join(location,item))
    for fil in files(location):
        if fil not in file_dict.keys():
            file_dict.update({fil:os.path.join(location,fil)})
        elif type(file_dict[fil]).__name__ == "str":
            fi=[file_dict[fil]]
            fi.append(os.path.join(location,fil))
            file_dict.update({fil:set(fi)})
        else:
            fi=list(file_dict[fil])
            fi.append(os.path.join(location,fil))
            file_dict.update({fil:set(fi)})
    while not q.empty():
        main(q.get())

# MAIN FUNCTION
if __name__=="__main__":
    parser = ArgumentParser()
    parser.add_argument('-s','--search',help="File name to search for duplication",required=False)
    parser.add_argument('-p','--path',help="Path to search for files defaults to PWD",required=False,default=".")
    args=parser.parse_args()
    path=args.path
    if path == ".":
        path=os.path.abspath(".")
    if path[0] =="/" or path[0:2] == "./" or path[0:3]=="../" or path[0].isalpha():
        main(path)
    if args.search:
        print args.search
        for i in file_dict[args.search]:
            print "\t",i
        exit(0)
    for i in file_dict.keys():
        if type(file_dict[i]).__name__ == "set":
            print i
            for j in file_dict[i]:
                print "\t",j
            exit(0)
    print "Congrats no duplicate files found"
