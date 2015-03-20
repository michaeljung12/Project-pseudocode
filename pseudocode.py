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

#From here I need download the spatial coordinate data from GBIF for the 5 species in the pruned tree
#Will use R studio for this part
#these are the packages used to directly download the spatial data from GBIF 
library(sp)
library(raster)
library(dismo)

#this is the code that grabs the data from GBIF directly
greatwhite <- occ_search("Carcharodon carcharias", limit = 500) #limits the amount of data to 500 points for whichever species you want
#Now you have to extract the latitude and longitude from the downloaded occurrence data
setwd("/home/vagrant/tree_stuff/whitesharkoccurence") #sets the current working directory on R to where the downloaded info is
#Defines a function that allows you to extract only the Latitude and Longitude from occurrence.txt file
whiteshark_func <- function(filename) {
    ws_occurrence <- read.table(filename, header= TRUE, sep= "\t", na.strings= "NA", quote= "", fill= TRUE)  
    whiteshark_new_occurrence <- ws_occurrence[,c("decimalLongitude", "decimalLatitude", "species")] #pulls out lat/lon into new object
    return(whiteshark_new_occurrence)    
}
#Applied the function to all the downloaded occurrence text files for the 5 species
coor = whiteshark_func('occurrence.txt')
cleaned <- na.omit(coor) #removes all NA from occurrence data
coor1 = whiteshark_func('occurrence1.txt')
cleaned1 <- na.omit(coor1)
coor2 = whiteshark_func('occurrence2.txt')
cleaned2 <- na.omit(coor2)
coor3 = whiteshark_func('occurrence3.txt')
cleaned3 <- na.omit(coor3)
coor4 = whiteshark_func('occurrence4.txt')
cleaned4 <- na.omit(coor4)

# finding all the latitude and longitude points of the GWS locations from OBIS



# plot the data points using matplotlib
# diff color for each species
# script not finished yet
# need to add script for using diff color for each species
# also need to finish looping the request from OBIS/GBIF to plot all points for all species




# calc and plot speciation rates
