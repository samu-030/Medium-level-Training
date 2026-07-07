class Solution(object):
    def carFleet(self, target, position, speed):

        fleet = 0
        prev_time = 0

        cars = sorted(zip(position, speed), reverse = True)

        for pos, spd in cars:

            time = float(target - pos) / spd

            if time > prev_time:
                fleet += 1
                prev_time = time

        return fleet
        