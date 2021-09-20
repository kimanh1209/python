import os
import re
import sys


def getFilePathSet(path):
    fileContent = open(path, "r").read()
    jpgLineTextList = re.findall("GET (.*\.jpg)",fileContent,re.MULTILINE)
    jpgLineTextSet=set(jpgLineTextList)
    fileName = os.path.basename(path)
    jpgPaths = []
    for jpg in jpgLineTextSet:
        fullPath = get_domain(fileName)+jpg
        jpgPaths.append(fullPath)
    return jpgPaths

def get_domain(filename):
    #regex như này thì đuôi file là google.com.vn vẫn hiểu được
    re_host = re.search("[\.](\w*(\.[a-z]{2,6}){1,2})$", filename) 
    if re_host: domain = "http://"+re_host.groups()[0]
    else: domain = ""
    return domain

def main():
    args = sys.argv[1:]
    if not args:
        print('usage: file_path [file_path ...]')
        sys.exit(1)
    if args[0] == 'file_path':
        for arg in args[1::]:
            print("\n".join(getFilePathSet(arg)))
    
if __name__ == '__main__':
  main()