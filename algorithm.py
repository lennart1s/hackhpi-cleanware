from asyncio import tasks
import random
from xml.dom import NoModificationAllowedErr

#
clusters = []

class Cluster:
    powerOverflow = 0
    tasks = []
    energy = []
    minEnergy = 0
    overflowTasks = []
    def __init__(self) -> None:
        for i in range(3):
            self.tasks.append(random.randint(1,30))
        for j in range(48):
            self.energy.append(random.randint(2,8))
        
    
    def overflowPower(self, additional = 0):
        powerOverflow = 0
        powerUsed = (sum(self.tasks) + additional) * 0.2
        for powerAvailable in self.energy:
            if powerUsed > powerAvailable:
                powerOverflow += powerUsed - powerAvailable
        return powerOverflow
    
    def calcMinEnergy(self):
        self.minEnergy = min(self.energy)
    
    def calcOverflowTasks(self):
        sumTasks = 0
        for i in range(len(self.tasks)):
            if sumTasks + self.tasks[i] > self.minEnergy:
                self.overflowTasks = self.tasks[i:]
                self.tasks = self.tasks[:i]
    
    def getMaxOverflowTask(self):
        maxOverflowTask = -1
        


#Algorithm optimizes total area overflow in energy-over-time graph

def algorithm():
    
    
        


        #totalOverflow += overflowPower(energy, cluster)
    cluster.tasks.sort()
    minData = cluster.energy[0]
    for dataPoint in cluster.energy:
        if dataPoint < minData:
            minData = dataPoint
    sum = 0
    for i in range(len(cluster.tasks) - 1):
        if sum + cluster.tasks[i] < minData:
            sum += cluster.tasks[i]
        else:
            tasksToMove += cluster.tasks[i:]
            break
                
    #Move around            
    for task in tasksToMove:
        for cluster in clusters:
            cluster.tasks.append(task)
            if overflowPower(cluster) > cluster.overflow:
                cluster.tasks.remove(task)
                cluster.overflow = overflowPower(cluster)
                print(cluster.overflow)
                break
            else:
                tasksToMove.remove(task)

        
    return

def findMaxOverflowTask():
    maxOverflowTask = -1
    for i in range(len(clusters) - 1):
        

def get_power(task):
    return task.get('Name')

#Calculates area overflow for a single cluster
def overflowPower(cluster):
    powerOverflow = 0
    powerUsed = sum(cluster.tasks) * 0.2
    for powerAvailable in cluster.energy:
        if powerUsed > powerAvailable:
            powerOverflow += powerUsed - powerAvailable
    return powerOverflow


def main():
    for i in range(3):
        clusters.append(Cluster())
    algorithm()

main()