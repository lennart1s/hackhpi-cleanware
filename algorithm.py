import random
from xml.dom import NoModificationAllowedErr

#
clusters = []

moveCost = 10
taskFactor = 1

class Cluster:

    def __init__(self, clusterId, tasks = None):
        if tasks:
            self.tasks = tasks
        else:
            self.tasks = []
            for i in range(5):
                self.tasks.append(random.randint(1,20))
        self.energy = []
        for j in range(12):
            self.energy.append(random.randint(50,80))
        self.clusterId = clusterId
        self.minEnergy = min(self.energy)
        self.tasks.sort()
        print(self.tasks)
        
    
    def overflowPower(self, additional = 0):
        powerOverflow = 0
        powerUsed = (sum(self.tasks) + additional) * taskFactor
        for powerAvailable in self.energy:
            if powerUsed > powerAvailable:
                powerOverflow += powerUsed - powerAvailable
        return powerOverflow


    
    def extractOverflowTasks(self):
        sumTasks = 0
        res = []
        lastUsed = -1
        for i in range(len(self.tasks)):
            if (sumTasks + self.tasks[i]) * taskFactor > self.minEnergy:
                res.append((self.tasks[i], self.clusterId))
            else:
                lastUsed = i
            sumTasks += self.tasks[i]
        self.tasks = self.tasks[:lastUsed + 1]
        return res
        


#Algorithm optimizes total area overflow in energy-over-time graph

def algorithm():
    overflowTasks = []
    for cluster in clusters:
        overflowTasks += cluster.extractOverflowTasks()
    
    overflowTasks.sort(key = lambda tup: tup[0], reverse=True)
    print(overflowTasks)
    for overflowTask in overflowTasks:
        findBestFittingCluster(overflowTask)
    
    for cluster in clusters:
        print(cluster.tasks)
        

     

def findBestFittingCluster(task):
    bestFittingCluster = -1
    overflowAddition = 99999999999
    for i in range(len(clusters)):
        print(task[1])
        print(i)
        if clusters[i].clusterId == task[1]:
            additional = 0
        else:
            additional = moveCost
        if overflowAddition - additional > clusters[i].overflowPower(task[0]) - clusters[i].overflowPower():
            overflowAddition = clusters[i].overflowPower(task[0]) - clusters[i].overflowPower()
            bestFittingCluster = i
            if additional == 0:
                print('movefree')
    clusters[bestFittingCluster].tasks.append(task[0])
    print(clusters[bestFittingCluster].tasks)
        

def main():
    s = 0
    clusters.append(Cluster(0))
    s += clusters[0].overflowPower()
    clusters.append(Cluster(1))
    s += clusters[1].overflowPower()
    clusters.append(Cluster(2))
    s += clusters[2].overflowPower()
    print(s)
    algorithm()
    s2 = 0
    for i in range(3):
        s2 += clusters[i].overflowPower()
    print(s2)
    if s2 != 0:
        print(s/s2)
    else:
        print('perfect')

main()