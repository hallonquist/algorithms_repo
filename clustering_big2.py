import numpy as np
import heapq
import copy
import time

file = open('clustering_big.txt','r')
line = file.readline()
x = line.split()
n = int(x[0])
num_bits = int(x[1])
print(n,num_bits)

V = np.zeros( (n,num_bits), dtype='int')

for i in range(0,n):
    line = file.readline()
    x = line.split()
    for j in range(0,num_bits):
        V[i,j] = int(x[j])
    
print(V[0:10,:])
file.close()

def vertex_distance(v1,v2,num_bits):

    dist = np.sum(v1!=v2)
        
    return dist

if 0:
    edges=[]
    vertex_near_another = np.zeros((n,1))
    for i in range(0,1000):

        if i%100==0:
            print(i)
        
        for j in range(i+1,n):
            if vertex_distance(V[i,:],V[j,:],num_bits)<=2:
                edges.append([i,j])
                vertex_near_another[i]=1
                vertex_near_another[j]=1

    print(np.sum(vertex_near_another))
    print(len(edges))
    # 4497.0
    # 3568





l=12
clusters = {}
for i in range(0,n):
    bits = V[i,0:l].tolist()
    s = ''.join(str(x) for x in bits)
    clusters[s] = []
    
for i in range(0,n):
    bits = V[i,0:l].tolist()
    s = ''.join(str(x) for x in bits)
    x = clusters[s]
    x.append(i)
    clusters[s] = x

base = V[i,0:l].tolist()
count=0
for stuff in clusters.keys():

    y = [int(i) for i in stuff]
    #print(base, y)
    #print(vertex_distance(base,np.array(stuff),l))
    dist=0
    for j in range(0,l):
        if int(base[j]) != int(stuff[j]):
            dist+=1
    #print( dist )
    if dist <= 2:
        count+=1

print(count)
print(len( clusters.keys() ))

tic = time.perf_counter()
edges=[]
vertex_near_another = np.zeros((n,1))
for i in range(0,1000):

    if i%100==0:
        print(i)

    base = V[i,0:l].tolist()

    # for each cluster:
    for stuff in clusters.keys():
        y = [int(j) for j in stuff]

        # calculate projection distance:
        proj_dist=0
        for j in range(0,l):
            if int(base[j]) != int(stuff[j]):
                proj_dist+=1

        # if the projection distance is close enough:
        if proj_dist <= 2:

            # calculate full distance for each vertex in this cluster:
            vertex_list = clusters[stuff]
            for j in vertex_list:
            
                if vertex_distance(V[i,:],V[j,:],num_bits)<=2 and i<j:
                    edges.append([i,j])
                    vertex_near_another[i]=1
                    vertex_near_another[j]=1


    #for j in range(i+1,n):
    #    if vertex_distance(V[i,:],V[j,:],num_bits)<=2:
    #        edges.append([i,j])
    #        vertex_near_another[i]=1
    #        vertex_near_another[j]=1

print(np.sum(vertex_near_another))
print(len(edges))
toc = time.perf_counter()
print(f"{toc - tic:0.4f} seconds")


    # old version:
    # 4497.0
    # 3568f

    # timing: l=14, time=139.6066 (sec)
            # l=13, time=70.8954 (sec)
            # l=12, time=47.0208 (sec)
            # l=11, time=51.2576 (sec)
            # l=10, time=69.0672 (sec)

git 