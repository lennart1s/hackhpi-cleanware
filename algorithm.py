import random

#
Clusters = []
#Array with all given racks from all clusters
Racks = []
#All existing Tasks at the current time
Tasks = []

def initializeAssignment():
    for task in Tasks:
        task.rack = random.randint(0, len(Racks))
    return

#Algorithm optimizes total area overflow in energy-over-time graph
def algorithm(weatherInput):
    while True:
        totalOverflow = 0
        for cluster in Clusters:
            energy = cluster.weatherInput["kwh"]
            totalOverflow += overflowPower(energy, cluster)
    return

#Calculates area overflow for a single cluster
def overflowPower(energy, cluster):
    powerOverflow = 0
    powerUsed = 0
    for rack in cluster:
        powerUsed += rack.cpuCost * calcRackCpuUsage(rack)
    for powerAvailable in energy:
        if powerUsed > powerAvailable:
            powerOverflow += powerAvailable
    return powerOverflow

def calcRackCpuUsage(rack):
    cpuUsage = 0
    for task in rack.assignedTasks:
        cpuUsage += task.cpu
    return cpuUsage



def calcClusterPowerAvailable():
    powerAvailable = cluster.powerAvailable[0]
    for taskMoved in cluster.getMovedTasks():
        powerAvailable -= taskMoved.distanceEnergy * taskMoved.dataSize / 2
        if taskMoved.movedIn() and taskMoved.rack.wasOff():
            powerAvailable -= taskMoved.rack.bootCost
            