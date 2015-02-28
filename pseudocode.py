# greatwhiteshark = species that I want
# sharktree = shark phylogeny tree in newick format

# def treePrune (greatwhiteshark, sharktree):
    #return prunedtree = pruned version of shark tree with great white sharks only
import dendropy

tt = dendropy.Tree.get_from_path("shark.tree", schema="newick")

print(tt)

tt.taxon_set.labels()

mrcaset = ["Carcharodon carcharias", "Lamna nasus"]

subtree = tt.mrca(taxon_labels = mrcaset)

subtree.as_newick_string()

out = open("pruned_sharks.tree", "w")

outtree = subtree.as_newick_string()

out.write(outtree)

out.close

#from here I need to make a request to get the spatial coordinate datas from OBIS/GBIF
#I wasn't sure how I could use the 5 species in the subtree string and loop the request info 
#and connect it together

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
# diff color for each species
# script not finished yet
# need to add script for using diff color for each species
# also need to finish looping the request from OBIS/GBIF to plot all points for all species

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
 
map = Basemap(projection='robin', resolution = 'l', area_thresh = 1000.0,
              lat_0=0, lon_0=-130)
map.drawcoastlines()
map.drawcountries()
map.fillcontinents(color = 'gray')
map.drawmapboundary()
map.drawmeridians(np.arange(0, 360, 30))
map.drawparallels(np.arange(-90, 90, 30))
 
x,y = map(lons, lats)
map.plot(x, y, 'ro', markersize=6)
 
plt.show()


# calc and plot speciation rates
