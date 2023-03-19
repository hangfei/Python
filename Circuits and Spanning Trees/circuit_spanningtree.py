import random
import itertools
import math

def create_cities(how_many):
    if(how_many < 1 or how_many > 26):
        return "Error"
    directory = {}
    for i in range(97, (97 + how_many)):
        directory[chr(i)] = (1000 * random.random(), 1000 * random.random())
        #print "City", chr(i), ": has coordinates",directory[chr(i)]
    return directory

def print_cities(directory):
    for i in directory.keys():
        print "City", i, ": has coordinates", "(%.2f," % directory[i][0], "%.2f)" % directory[i][1]

def create_cycle(directory):
    #del directory['a']
    road_map = list(itertools.permutations(directory.keys()))[0]
    print road_map
    return road_map

def improve_cycle(road_map, directory):
    print "In improve ", road_map, directory
    sum_dist = 0
    length = len(road_map)
    for i in range(0, len(road_map)):
        print "second element: ", directory[road_map[(i + 1) % length]] ,"first ele: ", directory[road_map[(i) % length]] 
        sum_dist += math.sqrt(((directory[road_map[(i + 1) % length]][0] - directory[road_map[i]][0]) ** 2)
                            + ((directory[road_map[(i + 1) % length]][1] - directory[road_map[i]][1]) ** 2 ))                
        print sum_dist
        if(sum_dist < 10000000):
            retur

            
                   

        
def main():
    d = create_cities(5)
    print_cities(d)
    rm = create_cycle(d)
    improve_cycle(rm, d)

main()


##sum_dist = 0
##current_x = directory['a'][0]
##current_y = directory['a'][1]
##print "current", current_x, current_y
##del directory['a']
##for coord in itertools.permutations (directory.values()):
##    print coord
##    for i in coord:    
##        sum_dist += math.sqrt(((current_x - i[0]) ** 2) + ((current_y - i[1]) ** 2 ))
##        print sum_dist
