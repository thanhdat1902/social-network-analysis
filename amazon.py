from helper import NetworkHelper
from DataLoader import DataLoader
import sys
import logging
TEST_NAME = "Amazon"
sys.stdout = logging.Logger("./" + TEST_NAME + "_log.txt")


networkHelper = NetworkHelper()
originalNetworkData = DataLoader("data/com-amazon.ungraph.txt", "Amazon").buildNetworkXGraph()
GccNetwork = networkHelper.largestConnectedComponent(originalNetworkData)
avgDegreeOrg = None
averageClusteringCoefficientOrg = None

def original():
    global avgDegreeOrg,averageClusteringCoefficientOrg
    print("========================================= Original Network ======================================")
    avgDegreeOrg = networkHelper.averageDegrees(GccNetwork)
    averageClusteringCoefficientOrg = networkHelper.averageClusteringCoefficient(GccNetwork)
    print("Size: ", networkHelper.getSize(GccNetwork))
    print("Average Degree: ", avgDegreeOrg)
    print("Average Path Length By Taking 10% Nodes In Original:" , networkHelper.averagePathLengthByPercentage(GccNetwork))
    print("Average Path Length By Taking 20% Nodes In Original:" , networkHelper.averagePathLengthByPercentage(GccNetwork, 0.2))
    print("Average Path Length By Using Random Walk Algorithm:" , networkHelper.averagePathLengthRandomWalk(GccNetwork))
    print("Clustering Coefficient: ", averageClusteringCoefficientOrg)


def watts():
    global avgDegreeOrg, averageClusteringCoefficientOrg
    if avgDegreeOrg != None and averageClusteringCoefficientOrg != None:
        d = int(avgDegreeOrg)
        c0 = 3 * (d - 2) / (4 * (d - 1))
        p = (1 - (averageClusteringCoefficientOrg / c0)) ** (1 / 3)
        wattsModel = networkHelper.watts_strogatz_graph(len(GccNetwork), d, p)
        print("========================================= Watts-Strogatz ======================================")
        print("Probability p:", p)
        print("Average Path Length By Taking 10% Nodes In Original:" , networkHelper.averagePathLengthByPercentage(wattsModel))
        print("Average Path Length By Taking 20% Nodes In Original:" , networkHelper.averagePathLengthByPercentage(wattsModel, 0.2))
        print("Average Path Length By Using Random Walk Algorithm:" , networkHelper.averagePathLengthRandomWalk(wattsModel))
        print("Clustering Coefficient: " , networkHelper.averageClusteringCoefficient(wattsModel))
    else:
        print("Error with original network")

def barabasi():
    global avgDegreeOrg
    barabasiModel = networkHelper.barabasi_albert_graph(len(GccNetwork), (int(avgDegreeOrg) // 2))
    print("========================================= Barabasi-Albert ======================================")
    print("Average Path Length By Taking 10% Nodes In Original:" , networkHelper.averagePathLengthByPercentage(barabasiModel))
    print("Average Path Length By Taking 20% Nodes In Original:" , networkHelper.averagePathLengthByPercentage(barabasiModel, 0.2))
    print("Average Path Length By Using Random Walk Algorithm:" , networkHelper.averagePathLengthRandomWalk(barabasiModel))
    print("Clustering Coefficient: ", networkHelper.averageClusteringCoefficient(barabasiModel))


print("========================================= Amazon ======================================")
original()
barabasi()
watts()


