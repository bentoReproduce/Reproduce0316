import matplotlib.pyplot as plt

folderName = "ground_truth_verfier_max6"

ts1 = list()
sizes1 = list()
ts2 = list()
sizes2 = list()
ts3 = list()
sizes3 = list()
ts4 = list()
sizes4 = list()
ts5 = list()
sizes5 = list()
ts6 = list()
sizes6 = list()

with open(folderName+"/client1_output.txt") as f:
    for line in f.readlines():
        t, size, _ = line.split()
        ts1.append(float(t))
        sizes1.append(float(size))


with open(folderName+"/client2_output.txt") as f:
    for line in f.readlines():
        t, size, _ = line.split()
        ts2.append(float(t))
        sizes2.append(float(size))


with open(folderName+"/client3_output.txt") as f:
    for line in f.readlines():
        t, size, _ = line.split()
        ts3.append(float(t))
        sizes3.append(float(size))


with open(folderName+"/client4_output.txt") as f:
    for line in f.readlines():
        t, size, _ = line.split()
        ts4.append(float(t))
        sizes4.append(float(size))

with open(folderName+"/client5_output.txt") as f:
    for line in f.readlines():
        t, size, _ = line.split()
        ts5.append(float(t))
        sizes5.append(float(size))

with open(folderName+"/client6_output.txt") as f:
    for line in f.readlines():
        t, size, _ = line.split()
        ts6.append(float(t))
        sizes6.append(float(size))

plt.figure()
#plt.scatter(ts, sizes)
#plt.savefig("client1")
plt.plot(ts1, sizes1, label="clinet 1")
plt.plot(ts2, sizes2, label="clinet 2")
plt.plot(ts3, sizes3, label="clinet 3")
plt.plot(ts4, sizes4, label="clinet 4")
plt.plot(ts5, sizes5, label="clinet 5")
plt.plot(ts6, sizes6, label="clinet 6")
plt.legend()
plt.title('ground_truth_verfier_max6')
plt.xlabel('time')
plt.ylabel('bandwidth')
plt.ylim(0, 500)
plt.show()
