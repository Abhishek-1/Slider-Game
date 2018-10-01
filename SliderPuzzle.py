##Name - Abhishek Ranjan
##USN - 657657618
##NetId - aranja8

import time
import os
import psutil



graph = [[str([[1, 0, 2, 4],[5, 7, 3, 8], [9, 6, 11, 12],[13, 10, 14, 15]])]]
final = str([[1, 2, 3, 4],[5, 6, 7, 8], [9, 10, 11, 12],[13, 14, 15, 0]])

 

def findSolution(dir):
    soln = []
    for i in range(len(dir)-1):
        first = eval(dir[i])
        second = eval(dir[i+1])
        i = 0
        j = 0
        k = 0
        l = 0
        while 0 not in first[i]:
            i += 1
        while 0 not in second[k]:
            k += 1
        j = first[i].index(0)
        l = second[k].index(0)
        if k > i:
            soln.append("D")
        elif i > k:
            soln.append("U")
        elif i == k:
            if j < l:
                soln.append("R")
            elif j > l:
                soln.append("L")
    return soln


def traversal(mat): 
   
    tree = [] 
    matrix = eval(mat)
    i = 0
    while 0 not in matrix[i]: i += 1
    j = matrix[i].index(0);
    
   
      #LEFT
    if j > 0:                                                      
      matrix[i][j], matrix[i][j-1] = matrix[i][j-1], matrix[i][j]
      tree.append(str(matrix))
      matrix[i][j], matrix[i][j-1] = matrix[i][j-1], matrix[i][j]

    if j < 3:                                   
      matrix[i][j], matrix[i][j+1] = matrix[i][j+1], matrix[i][j]
      tree.append(str(matrix))
      matrix[i][j], matrix[i][j+1] = matrix[i][j+1], matrix[i][j]
      
    #UP  
    if i > 0:                                   
      matrix[i][j], matrix[i-1][j] = matrix[i-1][j], matrix[i][j] 
      tree.append(str(matrix))
      matrix[i][j], matrix[i-1][j] = matrix[i-1][j], matrix[i][j]
      
    #DOWN  
    if i < 3:                                   
      matrix[i][j], matrix[i+1][j] = matrix[i+1][j], matrix[i][j]
      tree.append(str(matrix))
      matrix[i][j], matrix[i+1][j] = matrix[i+1][j], matrix[i][j]

    return tree

process = psutil.Process(os.getpid())
start_time = time.time()

def mainFunc(graph, final):
    problem = str(graph)
    visitednodes = []
    visted_nodes=0
    while graph:
        dir = graph[0]
        graph = graph[1:]
        node = dir[-1]
        if node in visitednodes: continue
        for posn in traversal(node):
            if posn in visitednodes: continue
            graph.append(dir + [posn])
        visitednodes.append(node)
        visted_nodes += 1
        if node == final: break
    
    print ("Output for Sequence :", problem)
    soln = findSolution(dir)
    print(soln)
    print("Number of Nodes expanded: ", visted_nodes)
    print("TIme Taken" , ((time.time() - start_time)*60), "ms")
    print(((process.memory_info().rss)/1024),"kb")


mainFunc(graph, final)

while True:
    newSeq = input('Enter a new Sequence: ')
    if(newSeq == ''):
        break
    numlist = [int(s) for s in newSeq.split() if s.isdigit()]
    if(len(numlist) != len(set(numlist)) or len(numlist) != 16):
        print("Solution does not exist")
        break
    for s in range(len(numlist)):
        if(numlist[s] > 15 or numlist[s] < 0):
             print("Solution does not exist")
             break
    
        
    w, h = 4, 4
    k = 0
    Matrix = [[0 for x in range(w)] for y in range(h)] 
    for i in range (4):
        for j in range(4):
            Matrix[i][j] = numlist[k]
            k += 1
        
    inpStr = str(Matrix)
    
    graph = [[inpStr]]
    
    mainFunc(graph, final)
    



