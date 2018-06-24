import json, requests, time

runs = int(input("Laeufe = "))


def ch4():
    geturl = "https://cc.the-morpheus.de/challenges/4/"
    posturl = "https://cc.the-morpheus.de/solutions/4/"

    param = dict()
    resp = requests.get(url = geturl, params = param)
    data = resp.json()

    getK = data["k"]
    getArr = data["list"]
    # print(getK)
    # print(getArr)

    def rotate(array, k):
        for i in range(0, k, 1):
                new = [0]
                for j in range(0, len(array), 1):
                        new.append(array[j])
                new[0] = new[len(new) - 1]
                del new[len(new) - 1]
                array = new
        loesung = {"token":array}
        #print(loesung)
        # print(loesung)
        result = requests.post(posturl, json.dumps(loesung))
        if a < 10:
            print("Run Nummer  %s = %s" % (a, result.text))
        else:
            print("Run Nummer %s = %s" % (a, result.text))
        # print(result.text)
        # print(result.text)

    rotate(getArr, getK)

start = time.time()
for a in range(0, runs, 1):
    ch4()
dauer = time.time() - start
durchschn = dauer / runs
print("Insgesamte Dauer: %s Sekunden" % dauer)
print("Dauer pro Run: %s Sekunden" % durchschn)
