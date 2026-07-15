class Solution(object):
    def numRabbits(self, answers):
        available_slots = {}
        total_rabbits = 0
        
        for x in answers:
            if x in available_slots and available_slots[x] > 0:
                available_slots[x] -= 1
            else:
                total_rabbits += x + 1
                available_slots[x] = x
                
        return total_rabbits

        