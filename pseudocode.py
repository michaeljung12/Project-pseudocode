#this script finds all great white shark species in a phylogeny and prunes the tree 
#then downlaods occurrence data from obis and put onto a map

# greatwhiteshark = species that I want
# sharktree = shark phylogeny tree in newick format

# def treePrune (greatwhiteshark, sharktree):
    #return prunedtree = pruned version of shark tree with great white sharks only

#once I get the subtree

# finding all the latitude and longitude points of the GWS locations from OBIS
import csv

f = open('carcharodon.csv')

csv_f = csv.reader(f)

latitudes = []
longitudes = []

for column in csv_f:
    latitudes.append(column[6])
    longitudes.append(column[7])

print str(latitudes)
print str(longitudes)  


# plot the data points using matplotlib
#diff color for each species

# calc and plot speciation rates



