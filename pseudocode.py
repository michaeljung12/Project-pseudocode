# greatwhiteshark = species that I want
# sharktree = shark phylogeny tree in newick format

#Finding the closest relatives of Carcharodon carcharias
#first start python
import dendropy #program used to edit phylogeny trees
#puts the tree into a newick format that is readable on python
tt = dendropy.Tree.get_from_path("shark.tree", schema="newick")
print(tt)
#now you must set the labels for the tips of the phylogeny tree
tt.taxon_set.labels()
#To find Carcharodon carcharias closest relatives, I found all species belonging to Lamnidae from the tree
#Make a set of species to find the most recent common ancestor
mrcaset = ["Carcharodon carcharias", "Lamna nasus"]
#Define a new subtree with the most recent common ancestor
subtree = tt.mrca(taxon_labels = mrcaset)
subtree.as_newick_string() #prints at a newick string
#Now you must write the newick string into a new .tree file to save the new tree that was pruned from the original
out = open("pruned_sharks.tree", "w")
outtree = subtree.as_newick_string()
out.write(outtree)
out.close #close the file after you have written the tree

#from here I need to make a request to get the spatial coordinate datas from OBIS/GBIF
#I wasn't sure how I could use the 5 species in the subtree string and loop the request info 
#and connect it together

# finding all the latitude and longitude points of the GWS locations from OBIS



# plot the data points using matplotlib
# diff color for each species
# script not finished yet
# need to add script for using diff color for each species
# also need to finish looping the request from OBIS/GBIF to plot all points for all species




# calc and plot speciation rates
