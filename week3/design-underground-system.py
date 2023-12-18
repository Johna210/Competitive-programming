class UndergroundSystem:

    def __init__(self):
        self.diff = {}
        self.traveler = {}        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.traveler[id] = (stationName,t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        val = t - self.traveler[id][1]
        origin = self.traveler[id][0]

        if f"{origin}--{stationName}" in self.diff:
            self.diff[f"{origin}--{stationName}"].append(val)
        else:
            self.diff[f"{origin}--{stationName}"] = [val]


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        value = self.diff[f"{startStation}--{endStation}"]
        average = sum(value) / len(value)
        return average


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)