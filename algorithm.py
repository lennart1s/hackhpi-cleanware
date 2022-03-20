import random
import json




#
clusters = []

moveCost = 10
taskFactor = 0.27

class Cluster:

    def __init__(self, clusterId, tasks, racks):
        self.movedTasks = 0
        self.tasks = tasks
        self.racks = racks
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
    
    def possibleUsage(self, task = 0):
        return sum(self.tasks) + task <= self.racks * 100
        


#Algorithm optimizes total area overflow in energy-over-time graph

def algorithm():
    overflowTasks = []
    for cluster in clusters:
        overflowTasks += cluster.extractOverflowTasks()
    
    overflowTasks.sort(key = lambda tup: tup[0], reverse=True)
    print(overflowTasks)
    for overflowTask in overflowTasks:
        findBestFittingCluster(overflowTask)

     

def findBestFittingCluster(task):
    bestFittingCluster = -1
    overflowAddition = 99999999999
    for i in range(len(clusters)):
        if clusters[i].clusterId == task[1]:
            additional = 0
        else:
            additional = moveCost
        if overflowAddition - additional > clusters[i].overflowPower(task[0]) - clusters[i].overflowPower() and clusters[i].possibleUsage(task[0]):
            overflowAddition = clusters[i].overflowPower(task[0]) - clusters[i].overflowPower()
            bestFittingCluster = i
    clusters[bestFittingCluster].tasks.append(task[0])
    if clusters[bestFittingCluster].clusterId != task[1]:
        clusters[bestFittingCluster].movedTasks += 1
        

def testing():
    s = 0
    clusters.append(Cluster(0, [9, 10, 12, 19], 1))
    s += clusters[0].overflowPower()
    clusters.append(Cluster(1, [4, 5, 10, 11, 17, 20], 2))
    s += clusters[1].overflowPower()
    clusters.append(Cluster(2, [1, 6, 11, 17, 20], 1))
    s += clusters[2].overflowPower()
    print(s)
    algorithm()
    s2 = 0
    for i in range(3):
        s2 += clusters[i].overflowPower()
        print(clusters[i].tasks)
    print(s2)
    if s2 != 0:
        print(s/s2)
    else:
        print('perfect')


def main():
    with open('data_center.json') as json_file:
        jsonCluster = json.load(json_file)
    for cluster in jsonCluster:
        clusters.append(Cluster(cluster['id'], cluster['tasks'], cluster['racks']))
    algorithm()
    result = []
    for cluster in clusters:
        result.append({'id':cluster.clusterId,
        'tasks':cluster.tasks,
        'racks':cluster.racks,
        'renewableEnergyGenerated':cluster.energy[0],
        'energyUsed':sum(cluster.tasks)*taskFactor,
        'energyOverflowNext12h':cluster.overflowPower(),
        'movedTasks':cluster.movedTasks
        })
    print(result)

main()