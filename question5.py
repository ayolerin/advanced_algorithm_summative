# Ayo-Fisher Oluwapamilerin 
# Question 5
# This program will allow the user 
# find the  shortest distance to each node from the start node in 
# ascending order of node number
# import the heapq
import heapq

# create the edges variable to store the edges of the graph and its respective weight
edges = [[1, 2, 24], [1, 4, 20], [3, 1, 3], [4, 3, 12]]

# create the graph_create function that takes edges array as an argument 
def graph_create(edges):
    # create the graph variable to store all 
    # the edges as keys and the edges they are connected to as values 
    # and also their weight in a tuple   
    graph = {num:[] for num in range(1,len(edges)+1)}
    
    # for loop to loop through the edges array and remove its variable
    for first,second,third in edges:
        # if statement to check if the first and second variable are not in the graph         
        if first not in graph or second not in graph:
            # store the first variable as a key and 
            # the second and third variable as values 
            graph[first] = (second,third)
            # store the second variable as a key and 
            # the first and third variable as values 
            graph[second] = (first,third)
        # else statement if these edges have been seen 
        else:
            # append the graph with first variable as a key and 
            # the second and third variable as values
            graph[first].append((second,third))
            # append the graph with second variable as a key and 
            # the first and third variable as values
            graph[second].append((first,third))

    # return the graph
    return graph   


# create the shortestReach function that takes the number of edges, 
# array of edges and the start point as arguments  
def shortestReach(number,edges,start):
    
    # create the heap_var variable to store the start node and the weight
    heap_var = [(0, start)]
    
    # update the graph variable with the graph_create(edges)
    graph = graph_create(edges)
    
    # create the result dictionary to store the shortest reach 
    # and set the edges as the key and infinity as the value
    result    = {}
    # for statement to check the range 
    for first in range(1, number + 1):
        # set the result[first] to infinity
        result[first] = float('inf')
        
    # update the result[start] to zero because its the 
    # first node and it does not connect to anything but itself 
    result[start] = 0
    
    # while loop to pop out the first tuple in the heap 
    while heap_var:
        # create the tpl variable to pop the first tuple 
        tpl = heapq.heappop(heap_var)
        # for statement to go through the edge using a bfs method
        for fig in graph[tpl[1]]:
            # if statement if the weight of the connecting edge is greater than
            # the sum of the original weight of the edge and the current weight 
            if result[fig[0]] > result[tpl[1]] + fig[1]:
                # update the original weight to the sum of the original weight 
                # of the edge and the current weight
                result[fig[0]] = result[tpl[1]] + fig[1]
                # if statement to check if the tuple exists in the heap already
                if (fig[1], fig[0]) in heap_var:
                    # remove the tuple 
                    heap.remove((fig[1], fig[0]))
                    # call the heapify() function to sort them 
                    heapq.heapify(heap_var)
                # push the current edge and its weight to the heap 
                heapq.heappush(heap_var, (result[fig[0]], fig[0]))
      
    # create a short_path array to store the result of the shortest path 
    short_path = []
    # for loop to loop through the dictionary 
    for i in result:
        # add the path to the short_path array 
        short_path.append(result[i])

    # return the short_path array with the shortest path 
    return short_path[1:]
# start from one
start = 1

# call the shortestReach function 
print("With the Graph: " + str(edges))
print("The shortest path is " + str(shortestReach(len(edges),edges,start)))
