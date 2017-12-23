import subprocess
import matplotlib.pyplot as plt

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
    subprocess.call("wget 'youtube.com/watch?v=" + url + "'", shell=True)
def shrinkWebpage(url):
    file = "watch?v=" + url
    print file
    nextUrl = getNext(file)
    with open(file,"r") as infile:
        with open(webpages + url ,"wb") as outfile:
            outfile.write("nextUrl " + nextUrl + "\n")
            for line in infile:
                if "itemprop" in line:
                    s = line.split('"')
                    outfile.write(s[1] + " " + s[3] + "\n")
    subprocess.call("rm " + "'watch?v=" + url + "'", shell=True)
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
                print s1[1]
                urlList.append(s1[1])
                return s1[1]


def views():
    views = []
    for i in range(N):
        with open(webpages + urlList[i] ,"r") as infile:
            for line in infile:
                if "interactionCount" in line:
                    s = line.split(" ")
                    print s[1]
                    s = s[1][:-1] #strip away \n at end of line
                    views.append(int(s))
    print views
    plt.plot(views)
    plt.show()


# main function

for i in range(N):
    downloadWebpage(urlList[i])
    shrinkWebpage(urlList[i])
views()

