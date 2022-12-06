from time import sleep
k = open("output2.txt", "w")
g = open("output1.txt", "w")
for i in range(10):
    k.write("HE" + str(i) +"\n")
    g.write("Ke"+ str(i) +"\n")
    k.flush()
    g.flush()
    sleep(2)
