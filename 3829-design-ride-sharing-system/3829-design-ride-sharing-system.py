class RideSharingSystem(object):

    def __init__(self):

        self.rider = deque()
        self.driver = deque()
        self.cancel = set()

    def addRider(self, riderId):

        if riderId in self.cancel:
            self.cancel.remove(riderId)
        self.rider.append(riderId)

    def addDriver(self, driverId):

        self.driver.append(driverId)
        
    def matchDriverWithRider(self):

        while self.rider and self.rider[0] in self.cancel:
            self.rider.popleft()
        
        if self.rider and self.driver:

            r = self.rider[0]
            d = self.driver[0]

            self.rider.popleft()
            self.driver.popleft()

            return [d, r]

        return [-1,-1]

    def cancelRider(self, riderId):
        
        self.cancel.add(riderId)
        


# Your RideSharingSystem object will be instantiated and called as such:
# obj = RideSharingSystem()
# obj.addRider(riderId)
# obj.addDriver(driverId)
# param_3 = obj.matchDriverWithRider()
# obj.cancelRider(riderId)