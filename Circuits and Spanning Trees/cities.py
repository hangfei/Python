import random
import math
import copy

global storage
storage = {}

global storage_spanning
storage_spanning = {}

def create_cities(how_many):
    if(how_many < 1 or how_many > 26):
        return "Error"
    directory = {}
    for i in range(97, (97 + how_many)):
        directory[chr(i)] = set([float("%.2f" %(1000 * random.random())),
                                 float("%.2f" %(1000 * random.random()))])    
    return directory

def print_cities(directory):
    for i in directory.keys():
        print "City", i, ": has coordinates", list(directory[i])[0],",", list(directory[i])[1]

def create_cycle(directory):
    road_map = {}
    conn_list = directory.keys()
    return cycle_from_list(conn_list)
    
def cycle_from_list(conn_list):
    l = len(conn_list)
    road_map = {}
    for i in range(0, len(conn_list)):
        road_map[conn_list[i]] = set([conn_list[(i - 1) % l], conn_list[(i + 1) % l]])
    return road_map

def create_spanning_tree(directory):
    s_road_map = {}
    conn_list = directory.keys()
    s_road_map[conn_list[0]] = set([conn_list[1]])
    s_road_map[conn_list[-1]] = set([conn_list[-2]])
    for i in range(1, len(conn_list) - 1):
        #print i, conn_list[i]
        s_road_map[conn_list[i]] = set([conn_list[(i - 1)], conn_list[(i + 1)]])
    return s_road_map
    print s_road_map

def compute_cost(road_map, directory):
    sum_dist = 0
    for element in road_map.keys():
        i = 0
        for connected in road_map[element]:
            city = list(road_map[element])[i]
            x2 = list(directory[city])[0]
            x1 = list(directory[element])[0]
            y2 = list(directory[city])[1]
            y1 = list(directory[element])[1]
            sum_dist += (math.sqrt((x2 - x1)**2 + (y2 - y1)**2))/2
            i += 1
    #s = "%.2f" %(sum_dist)
    return sum_dist

def improve_cycle(road_map, directory):
    #print "Old road map", road_map
    d = copy.deepcopy(road_map.keys())
    d.remove('a')    
    l = len(d)
    n1 = int((random.random() * 1000) % l)
    n2 = n1
    while(n2 == n1):
        n2 = int((random.random() * 1000) % l)
    temp = d[n1]
    d[n1] = d[n2]
    d[n2] = temp
    d.insert(0, 'a')
    new_road_map = cycle_from_list(d)
    #print "New road map", new_road_map
    if(compute_cost(new_road_map, directory) <= compute_cost(road_map, directory)):
        store(new_road_map)
        return True
    else:
        return False

def improve_spanning_tree(s_road_map, directory):
    s_road_list = s_road_map.keys()
    length_roadmap = len(s_road_list)
    random_num = int((random.random() * 100000) % length_roadmap)
    random_city = s_road_list[random_num]
    another_num = 0
    #find common city: in the sets. if it's not in the sets, it's the key, there would be some problems
    #find a common city in two sets, and the two key cities is the ends, and the common city in the sets is the node
    #diff_cities[0] is a key, and diff_cities[1] is another key, but node_city is an common element in this two values
    cities_num = len(list(s_road_map[s_road_list[random_num]]))
    if cities_num > 1:
        random_con_num1 = random_num = int((random.random() * 100000) % cities_num)
        random_con_num2 = random_con_num1
        while random_con_num2 == random_con_num1:
            random_con_num2 = (random_con_num1 + 1) % cities_num
        #node_city
        node_city = random_city
        #diff_cities
        con_cities = list(s_road_map[random_city])
        diff_cities =con_cities[random_con_num1] + con_cities[random_con_num2]
    else:
        return False
    #made a modification
    dis_line_node1 = distance(node_city, diff_cities[0],directory)
    dis_line_node2 = distance(node_city, diff_cities[1],directory)
    dis_line_diff = distance(diff_cities[0], diff_cities[1], directory)
    comb_zero = dis_line_node1 + dis_line_node2
    comb_one = dis_line_node1 + dis_line_diff
    comb_two = dis_line_node2 + dis_line_diff
    comb_min = min(comb_zero, comb_one, comb_two)
    if comb_zero == comb_min:
        pass
    if comb_one == comb_min:
        s_road_map[diff_cities[1]].remove(node_city)
        s_road_map[diff_cities[1]].add(diff_cities[0])
        s_road_map[node_city].remove(diff_cities[1])        
        s_road_map[diff_cities[0]].add(diff_cities[1])
        return True
    elif comb_two == comb_min:
        s_road_map[diff_cities[0]].remove(node_city)
        s_road_map[diff_cities[0]].add(diff_cities[1])
        s_road_map[node_city].remove(diff_cities[0])
        s_road_map[diff_cities[1]].add(diff_cities[0])
        return True
        
    else:
        return False

def store(road_map):
    global storage
    storage = road_map

def fetch():
    global storage
    return storage


def store_spanning(road_map):
    global storage_spanning
    storage_spanning = road_map

def fetch_spanning():
    global storage_spanning
    return storage_spanning

def find_best_cycle(road_map, directory):
    count = 0
    for i in range(0, 1000):
        #print count
        ret = improve_cycle(road_map, directory)
        #print ret
        if(ret == True):
            road_map = fetch()
            #print fetch()
            count = 0
        elif(ret == False):
            count += 1
        if(count == 10):
            return fetch()
    print fetch()

def find_best_spanning_tree(s_road_map, directory):
    i = 0
    count = 0
    while i < 50:
        i += 1
        count += 1
        if improve_spanning_tree(s_road_map, directory):
            i = 0
    store_spanning(s_road_map)
    return s_road_map
    
def create_spanning_tree(directory):
    s_road_map = {}
    conn_list = directory.keys()
    s_road_map[conn_list[0]] = set([conn_list[1]])
    s_road_map[conn_list[-1]] = set([conn_list[-2]])
    for i in range(1, len(conn_list) - 1):
        s_road_map[conn_list[i]] = set([conn_list[(i - 1)], conn_list[(i + 1)]])
    return s_road_map

def print_map(road_map, directory):
    
    for element in road_map.keys():
        comp_road_map = {element:road_map[element]}
        print_cities = ""
        for cities in road_map[element]:
            print_cities += cities + " "
        print "City:",element
        print "Connected cities:", print_cities,"  Connection Cost:", compute_cost(comp_road_map, directory)
    print "Total cost:", compute_cost(road_map, directory)

def distance(city_one, city_two, directory):
    x1, x2 = (float(list(directory[city_one])[0]), float(list(directory[city_two])[0]))
    y1, y2 = (float(list(directory[city_one])[1]), float(list(directory[city_two])[1]))
    dist = 0
    dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return dist

def main():
    d = create_cities(15)
    rm = create_cycle(d)
    c = compute_cost(rm, d)
    f = find_best_cycle(rm, d)
    print "For Travelling Sales Man Problem:"
    print_map(f,d)
    print 
    
    s_road_map = create_spanning_tree(d)
    find_best_spanning_tree(s_road_map, d)
    t = fetch_spanning()
    print "For Minimum Spanning Tree Problem:"
    print_map(t, d)
    

main()
