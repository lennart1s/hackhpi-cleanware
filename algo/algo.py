from typing import List, Any

moveCost = 10
taskFactor = 0.27


class Algo:
    clusters = []

    def __init__(self) -> None:
        pass

    def add_task(self, datacenter: str, value: int) -> bool:
        for cluster in self.clusters:
            if cluster.clusterId == datacenter:
                return cluster.addTask(value)

    def delete_task(self, datacenter: str, value: int) -> bool:
        for cluster in self.clusters:
            if cluster.clusterId == datacenter:
                return cluster.delTask(value)
        return False

    def add_datacenter(self,
                       datacenter: str,
                       kilowats: List[float],
                       racks: int,
                       ) -> bool:

        self.clusters.append(Cluster(datacenter, kilowats, racks))

    def status(self) -> List[Any]:
        overflowTasks = []
        for cluster in self.clusters:
            overflowTasks += cluster.extractOverflowTasks()

        overflowTasks.sort(key=lambda tup: tup[0], reverse=True)
        for overflowTask in overflowTasks:
            self.findBestFittingCluster(overflowTask)

        result = []
        for cluster in self.clusters:
            result.append({'name': str(cluster.clusterId),
                           'tasks': cluster.tasks,
                           'racks': int(cluster.racks),
                           'rewgen': cluster.energy[0],
                           'rewused': sum(cluster.tasks)*taskFactor,
                           'overflow': cluster.overflowPower(),
                           'moved': cluster.movedTasks
                           })

        return result

    def findBestFittingCluster(self, task):
        bestFittingCluster = -1
        overflowAddition = 99999999999
        for i in range(len(self.clusters)):
            if self.clusters[i].clusterId == task[1]:
                additional = 0
            else:
                additional = moveCost
            if overflowAddition - additional > self.clusters[i].overflowPower(task[0]) - self.clusters[i].overflowPower() and self.clusters[i].possibleUsage(task[0]):
                overflowAddition = self.clusters[i].overflowPower(
                    task[0]) - self.clusters[i].overflowPower()
                bestFittingCluster = i
        self.clusters[bestFittingCluster].tasks.append(task[0])
        if self.clusters[bestFittingCluster].clusterId != task[1]:
            self.clusters[bestFittingCluster].movedTasks += 1


class Cluster:

    def __init__(self, clusterId, kilowats, racks):
        self.movedTasks = 0
        self.tasks = []
        self.racks = racks
        self.energy = kilowats
        self.clusterId = clusterId
        self.minEnergy = min(self.energy)

    def addTask(self, value):
        self.tasks.append(value)
        self.tasks.sort()
        return True

    def delTask(self, value):
        try:
            self.tasks.remove(value)
            self.tasks.sort()
            return True
        except:
            return False

    def overflowPower(self, additional=0):
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

    def possibleUsage(self, task=0):
        return sum(self.tasks) + task <= self.racks * 100
