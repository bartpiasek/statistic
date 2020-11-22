from statistics import mean

class Average():
    """
    Count avg of pkt or cgl
    """
    def avgPkt(numList):
        AvgDataPkt = statistics.mean(numList)
        return AvgDataPkt
    
    def avgPkt(final_list):
        AvgDataCgl = statistics.mean(final_list)
        return AvgDataCgl