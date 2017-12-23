import subprocess

N = 3
webpages = "./webpages/"
seed = "JWD1Fpdd4Pc"
urlList = [seed]

class video():
    def __init__(props):
        url = props[0]
        title = props[1]
        next = None

    def getnext(self):
        href = "href"
        h4 = "</h4>"
        nextt = "chstes Video"
        hot = False
        nextbool = False
        properties = [href,"title"]
        with open(webpages + self.url) as f:
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
                    props = []
                    getProps()
                    for prop in properties:
                        start = line.rfind(prop)
                        s = line[prop:]
                        s1 = line.split('"')
                        props.append(s1[1])
                    self.next=video(props)

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




# main function

for i in range(N):
    downloadWebpage(urlList[i])
    shrinkWebpage(urlList[i])
    print i

