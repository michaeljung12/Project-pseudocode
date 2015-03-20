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

#Now I will plot the latitude and longitude points onto a world map for the 5 species 
#Still using R Studio for this, and these are the packages I used to plot the points
library (maps)
library (mapdata)

sharkmap <- map('worldHires') #makes an empty and basic worldmap
#this next part plots the cleaned Latitude and Longitude points from the 5 species above onto the map, with different colors for each
points(cleaned$decimalLongitude, cleaned$decimalLatitude, col = "red", cex = .3)
points(cleaned4$decimalLongitude, cleaned4$decimalLatitude, col = "blue", cex = .3)
points(cleaned3$decimalLongitude, cleaned3$decimalLatitude, col = "green", cex = .3)
points(cleaned2$decimalLongitude, cleaned2$decimalLatitude, col = "orange", cex = .3)
points(cleaned1$decimalLongitude, cleaned1$decimalLatitude, col = "yellow", cex = .3)

#This next part calculates and plots the speciation rates
#I used BAMM (Bayesian Analysis of Macoevolutionary Mixtures) to analyze the phylogenetic tree and calculate and plot speciation rates
#You must first download BAMM and set up your control file
#Set the working directory to where you downloaded BAMM
setwd("~/tree_stuff/bamm/build")
sharktree <- read.tree("shark.tree") #read the tree
#set the BAMMpriors for the control file that is specific to your phylogenetic tree to run it with the optimal settings
setBAMMpriors(sharktree) 

#Now, you cannot run BAMM on vagrant and have to run it on your local directory in your terminal
setwd(/usr/local/bin/tempsharks) #set working directory to local bin in a folder with your control file and all the info
bamm -c myControlfile.txt #this runs BAMM onto your control file; you specify your tree file in the control file

#After you run bamm, you can use the BAMMtools package on R Studio to calculate and plot speciation rates
library(BAMMtools)
#set working directory to where all your files are
setwd("~/tree_stuff/shark_bamm")
tree <- read.tree("shark.tree")
#this defines the BAMMdata object using event_data.txt
edata <- getEventData(tree, eventdata = "event_data.txt", burnin=0.1) #event_data.txt file should be automatically made after you run BAMM
edata2 <- subsetEventData(edata, index = 1:20) #subsets the eventdata
#This allows you to calculate the speciation rate for each Tip of your phylogenetic tree
meanlam <- getTipRates(edata, returnNetDiv = FALSE, statistic = 'mean')$lambda.avg
meanlam #prints all the speciation rates for each tip

#To Plot speciation rate
#This calculates the Mean Branch Length speciation rate for your tree file
ratetree <- getMeanBranchLengthTree(edata2, rate='speciation')
#Plots a phylogenetic tree, topologically identical to the model tree 
#but with branch lengths replaced by the mean (marginal) rates on each branch as estimated from the posterior samples in the bammdata object.
plot(ratetree$phy, show.tip.label=FALSE)
#This makes a phylorate plot showing speciation rates along each branch of the shark phylogenetic tree
#cool colors = slow, warm = fast
plot.bammdata(edata, lwd=2, method="polar", pal="temperature")
#Each unique color section of a branch represents the mean of the marginal posterior density of speciation rates on a localized segment of your phylogenetic tree
