import sys
import markdown
inp = open("AMS 301-02-transcript.vtt").read()
# print(inp[0:200])

data = [x.strip() for x in inp.split("\n")[:-1]]
x=len(data)
info = []
for i in range(1,x,5):
    times = data[i+1].split(" --> ")
    words = data[i+2].split(">")[1]
    info.append([times,words])              

def eval(x):
    curr = [float(x) for x in x.split(":")]
    return curr[0]*3600+curr[1]*60+curr[2]
def stuff(x):
    x = x.split(":")
    val = ""
    if int(x[0])!=0: val += x[0]+":"
    val+=x[1]+":"
    val+=x[2][:x[2].index(".")]
    return val
i = 0

while i < len(info):
    start = info[i][0][0]
    end = info[i][0][1]
    curr = ""
    while i < len(info) and eval(end)-eval(start)<300:
        curr+=info[i][1]
        i+=1
        if i!=len(info): 
            curr+=" "
            end = info[i][0][1]
    print("# "+stuff(start)+"-"+stuff(end)+"\n")
    print(eval(start),eval(end),start,end)

"""
import sys
sys.stdin = open("AMS 301-02-transcript.vtt")
with open("AMS 301-02-transcript.vtt") as fp:
    x = len(fp.readlines())
_ = input()
info = []
for i in range(1,x,5):
    _ = input()
    times = input().split(" --> ")
    words = input().split(">")[1]
    _ = input()
    _=input()
    info.append([times,words])
def eval(x):
    curr = [float(x) for x in x.split(":")]
    return curr[0]*3600+curr[1]*60+curr[2]
i = 0
while i < len(info):
    start = info[i][0][0]
    end = info[i][0][1]
    curr = info[i][1]
    while i < len(info) and eval(end)-eval(start)<300:
        i+=1
        if i!=len(info): 
            if curr[-1] in "?.": curr+=" "
            curr+=info[i][1]
            end = info[i][0][1]
    print(eval(start),eval(end))
    print(curr)


"""
