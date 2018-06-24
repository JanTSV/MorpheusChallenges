import json, requests, time

runs = int(input("Runs = "))


def ch4():
    geturl = "https://cc.the-morpheus.de/challenges/4/"
    posturl = "https://cc.the-morpheus.de/solutions/4/"

    param = dict()
    resp = requests.get(url = geturl, params = param)
    data = resp.json()

    getK = data["k"]
    getArr = data["list"]

    def rotate(array, k):
        for i in range(0, k, 1):
                new = [0]
                for j in range(0, len(array), 1):
                        new.append(array[j])
                new[0] = new[len(new) - 1]
                del new[len(new) - 1]
                array = new
        result = {"token":array}
        send = requests.post(posturl, json.dumps(result))
        if a < 10:
            print("Run  %s = %s" % (a, send.text))
        else:
            print("Run %s = %s" % (a, send.text))

    rotate(getArr, getK)

start = time.time()
for a in range(0, runs, 1):
    ch4()
timeforallruns = time.time() - start
timeperrun = timeforallruns / runs
print("Time        : %s secs" % timeforallruns)
print("Time per run: %s Sekunden" % timeperrun)
