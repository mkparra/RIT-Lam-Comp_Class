# -*- coding: utf-8 -*-
"""
Created on Mon Oct 7 16:40:57 2020

@author: Mike Ortiz
"""

# Testing the Barnes-Hut algorithm by simulating galaxy clusters 
# into the future. Then use your fav intergrating method 
#
#

import numpy as np

Gal_1 = np.load('galaxies0.npy')
Gal_2 = np.load('galaxies1.npy')
# print(np.shape(Gal_1))

def BuildTree(node, node0, thetamax=0.7, G=1.0): 
    
    # Buidling the tree with the theta and Gravity as variables 
    # Calling this with the topnode as node will walk the tree to calculate the total field at node0.
    dx = node.COM - node0.COM    # vector between nodes' centres of mass
    r = np.sqrt(np.sum(dx**2))   # distance between them
    if r>0:
        # if the node only has one particle or theta is small enough,
        #  add the field contribution to value stored in node.g
        if (len(node.children)==0) or (node.size/r < thetamax):
            node0.g += G * node.mass * dx/r**3
        else:
            # otherwise split up the node and repeat
            for c in node.children: BuildTree(c, node0, thetamax, G)
                        
            
class Nodes:
    # stores the data for a node, and births its children if possible
    def __init__(self, center, size, masses, points, ids, leaves=[]):
        self.center = [5,5,0]                    # center of the node's box
        self.size = size                        # maximum side length of the box
        self.children = []                      # start out assuming that the node has no children
 
        Npoints = len(points)
 
        if Npoints == 1:
            # if we're down to one point, we need to store stuff in the node
            leaves.append(self)
            self.COM = points[0]
            self.mass = masses[0]
            self.id = ids[0]
            self.g = np.zeros(3)        # at each point, we will want the gravitational field for potentional
        else:
            self.MakingChildren(points, masses, ids, leaves)# if we have at least 2 points in the node, birth its children
 
            # now we can sum the total mass and center of mass hierarchically
            com_total = np.zeros(3) # running total for mass moments to get center of mass
            m_total = 0.            # running total for masses
            for c in self.children:
                m, com = c.mass, c.COM
                m_total += m
                com_total += com * m   # add the moments of each child
            self.mass = m_total
            self.COM = com_total / self.mass  
 
    def MakingChildren(self, points, masses, ids, leaves):
        """Generates the node's children"""
        octant_index = (points > self.center) 
        print(octant_index) #does all comparisons needed to determine points' octants
        for i in range(2): #looping over the octant
            for j in range(2):
                for k in range(2):
                    in_octant = np.all(octant_index == np.bool_([i,j,k]), axis=1)
                    print(in_octant)
                    print(type(size))
                    if not np.any(in_octant): continue           # if no particles, don't make another node
                    dx = .5*self.size*(np.array([i,j,k])-0.5)   # difference between parents and children centers
                    self.children.append(Nodes(self.center+dx,
                                                 self.size/2,
                                                 masses[in_octant],
                                                 points[in_octant],
                                                 ids[in_octant],
                                                 leaves))
                    
                    
                    
    def Force_Softning(points, masses, thetamax=0.7, G=1.):
        center = (np.max(points,axis=0)+np.min(points,axis=0))/2       #center of bounding box
        topsize = np.max(np.max(points,axis=0)-np.min(points,axis=0))  #size of bounding box
        leaves = []  # want to keep track of leaf nodes
        topnode = Nodes(center, topsize, masses, points, np.arange(len(masses)), leaves) #build the tree with force softening
     
        accel = np.empty_like(points)
        for i,leaf in enumerate(leaves):
            BuildTree(topnode, leaf, thetamax, G)  # do field summation
            accel[leaf.id] = leaf.g  # get the stored acceleration
     
        return accel                    
center = (5,5,0)
size = int(1)
ids = np.arange(1,656,1)
points = Gal_1
z = np.zeros(len(points))
z_new = z.reshape(655,1)
# print(np.shape(points))
positions = np.column_stack((points,z_new))
print(len(positions))
# print(type(points))
Po = np.empty(len(points))
# print(len(Po))
Mass = np.array(([10**12])*len(Po)) #Solar Masses
print((Mass))
# print(points)    
leaves = [] 

Tree = Nodes(center,size,Mass,positions,ids,leaves)
# print(Tree)                 
                  
                    
                    
                    
            