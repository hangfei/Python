
import random
import itertools
import math

#if there are n cities, then n-1 lines is enough
#but there may be cases where n or n+1 lines may be better?
#it must be worse. lines added, distance added



def create_cities(how_many):
    if(how_many < 1 or how_many > 26):
        return "Error"
    directory = {}
    for i in range(97, (97 + how_many)):
        directory[chr(i)] = (1000 * random.random(), 1000 * random.random())
        #print "City", chr(i), ": has coordinates",directory[chr(i)]
    return directory

def create_spanning_tree(directory):
    #form a simplest case.put them in a list of tuples
    #the initial case does not matter
    #whe the sequence is so ?
    cities_list = directory.keys()
    road_map = []
    for i in range(0,len(directory.keys())-1):
        road_map.append((cities_list[i], cities_list[i+1]))
    print road_map
    return road_map

        

    

def improve_spanning_tree(s_road_map, directory):
    #every time randomly pick two connected tuples, say (a,b),(b,c), and shuffle
    length_roadmap = len(road_map)
    random_num = int((random.random() * 1000000) % length_roadmap)
    another_num = 0
    #find the connected city with the random_num
    for element in road_map:
        if (road_map[random_num][0] == element[0] or road_map[random_num][0] == element[1]
            or road_map[random_num][1] == element[0] or road_map[random_num][1] == element[1]) and (element != road_map[random_num]):
            break
        another_num += 1
    #two cities form a line
    improve_line1 = ()
    improve_line2 = ()
    #pick
    #find the common city of two lines
    #and change a connection city to make an improvement
    if True:
        #use set to get the node city and the different cities
        set_line1 = set([road_map[random_num][0],road_map[random_num][1]])
        set_line2 = set([road_map[another_num][0],road_map[another_num][1]])
        #?. use list to convert and then do not forget to use index, instead of the whole list
        node_city = list(set_line1.intersection(set_line2))[0]
        #set.difference is different from set.symmetric_difference
        diff_cities = set_line1.symmetric_difference(set_line2)
        city_one = list(diff_cities)[0]
        city_two = list(diff_cities)[1]
        new_node = city_one
        improve_line1 = (new_node, node_city)
        improve_line2 = (new_node, city_two)
        road_map[random_num] = improve_line1
        road_map[another_num] = improve_line2
        print road_map
        #improved road_map finished
        
            

directory = create_cities(9)
road_map = create_spanning_tree(create_cities(9))
improve_spanning_tree(road_map, directory)
