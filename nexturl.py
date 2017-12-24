import subprocess
import matplotlib.pyplot as plt
import os.path

N = 10
webpages = "./webpages/"
seed = "JWD1Fpdd4Pc"
urlList = [seed]

class video():
    def __init__(props):
        url = props[0]
        title = props[1]
        next = None


def downloadWebpage(url):
    subprocess.call("wget -q 'youtube.com/watch?v=" + url + "'", shell=True)
def shrinkWebpage(url):
    file = "watch?v=" + url
    if getNext(file):
        nextUrl = urlList[-1]
        with open(file,"r") as infile:
            with open(webpages + url ,"wb") as outfile:
                outfile.write("nextUrl " + nextUrl + "\n")
                for line in infile:
                    if "itemprop" in line:
                        s = line.split('"')
                        outfile.write(s[1] + " " + s[3] + "\n")
        subprocess.call("rm " + "'watch?v=" + url + "'", shell=True)
        return True
    else:
        return False
def getNext(infile):
    href = "href"
    h4 = "</h4>"
    nextt = "chstes Video"
    hot = False
    nextbool = False
    global urlList
    with open(infile) as f:
        for line in f:
            if (nextbool and h4 in line):
                hot = True
                continue
            nextbool = False
            if nextt in line:
                nextbool = True
                continue
            if (hot and href in line):
                hot = False
                start = line.rfind(href)
                s = line[start:]
                s1 = line.split('"')
                s1[1] = s1[1][1:]
                s1 = s1[1].split("=")
                if s1[1] in urlList:
                    print "Url already in UrlList"
                    return False
                else:
                    urlList.append(s1[1])
                    return True
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
    if os.path.isfile(webpages + urlList[i]):
        nextUrl = getAttr(urlList[i],"nextUrl")
        if nextUrl in urlList:
            print "Url already in UrlList"
            break
        else:
            urlList.append(nextUrl)
    else:
        downloadWebpage(urlList[i])
        if not shrinkWebpage(urlList[i]):
            break
views()

