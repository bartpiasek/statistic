import statistics
from statistics import stdev


def avgPkt(pktList):
    AvgDataPkt = statistics.mean(pktList)
    print(AvgDataPkt)
    return AvgDataPkt


def avgCgl(cglList):
    AvgDataCgl = statistics.mean(cglList)
    print(AvgDataCgl)
    return AvgDataCgl


def standardDevPkt(pktList):
    stdDataPkt = stdev(pktList)
    return stdDataPkt


def standardDevCgl(cglList):
    stdDataCgl = stdev(cglList)
    return stdDataCgl
