# -*- coding: utf-8 -*-
import subprocess
import matplotlib.pyplot as plt
import os.path

N = 10 # Maximum number of webpages downloaded if no merging is encounterd
webpages = "./webpages/"
seed = "JWD1Fpdd4Pc"
urlList = [seed]

class video():
    def __init__(props):
        url = props[0]
        title = props[1]
        next = None


def downloadWebpage(url):
    subprocess.call("wget  'youtube.com/watch?v=" + url + "'", shell=True)
def shrinkWebpage(url):
    file = "watch?v=" + url
    getNextResult = getNext(file)
    nextUrl = getNextResult[1]
    with open(file,"r") as infile:
        with open(webpages + url ,"wb") as outfile:
            outfile.write("nextUrl " + nextUrl + "\n")
            for line in infile:
                if "itemprop" in line:
                    s = line.split('"')
                    outfile.write(s[1] + " " + s[3] + "\n")
    subprocess.call("rm " + "'watch?v=" + url + "'", shell=True)
    return getNextResult[0] #True #returns if nextUrl is not already in UrlList i.e. "merging of branches"

def getNext(infile):
    href = "href"
    h4 = "</h4>"
    nexttList = ['Up next', 'Nächstes Video', 'À suivre', 'Siguiente']
    hot = False
    nextbool = False
    global urlList
    with open(infile) as f:
        for line in f:
            if (nextbool and h4 in line):
                hot = True
                continue
            nextbool = False
            for nextt in nexttList:
                if nextt in line:
                    nextbool = True
                    break
            if (hot and href in line):
                hot = False
                start = line.rfind(href)
                s = line[start:]
                s1 = line.split('"')
                s1[1] = s1[1][1:]
                s1 = s1[1].split("=")
                if s1[1] in urlList:
                    print "Url already in UrlList"
                    inList = False
                else:
                    urlList.append(s1[1])
                    inList = True
                return [inList,s1[1]]
                #return s1[1]

def getAttr(url, attr):
    with open(webpages + url ,"r") as infile:
        for line in infile:
            if attr in line:
                s = line.split(" ")
                s = s[1][:-1] #strip away \n at end of line
                infile.close()
                return s

def views():
    views = []
    for url in urlList:
        views.append(int(getAttr(url,"interactionCount")))
    print views
    plt.plot(views)
    plt.show()



# main function

for i in range(N):
    if os.path.isfile(webpages + urlList[i]):  #
        nextUrl = getAttr(urlList[i],"nextUrl")# here should not be urlList in order to function with multiple seeds
        if nextUrl in urlList:
            print "Url already in UrlList"
            break
        else:
            urlList.append(nextUrl)
    else:
        downloadWebpage(urlList[i])           #
        if not shrinkWebpage(urlList[i]):     # also here
            break
views()

