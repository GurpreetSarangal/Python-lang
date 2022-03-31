import random
class card:
    def __shuffle(self):
        temp_list1 = [x for x in range(0, self.no_of_colors)]
        temp_list2 = [x for x in range(0, self.depth)]

        # loop will also iterate for random range
        for i in range(0, random.randrange(0, self.depth + self.no_of_colors) ):
            # select random bead to swap
            first_x = random.choice(temp_list1)  
            first_y = random.choice(temp_list2)

            # select random bead to swap
            second_x = random.choice(temp_list1)  
            second_y = random.choice(temp_list2) 

            # swap random beads
            self.beads[second_x][second_y], self.beads[first_x][first_y] = self.beads[first_x][first_y], self.beads[second_x][second_y]
            
    def __init__(self, no_of_colors, depth):
        self.beads=[]
        self.no_of_colors = no_of_colors
        self.depth = depth
        for i in range(0, no_of_colors):
            temp=[]
            for j in range(0, depth):
                temp.append(chr(65+i))
            self.beads.append(temp)
        self.__shuffle()
    
    def test(self):
        print(self.beads)

test = card(3,3)
test.test()