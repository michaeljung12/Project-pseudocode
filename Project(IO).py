
# coding: utf-8

# In[1]:

import dendropy


# In[2]:

tt = dendropy.Tree.get_from_path("shark.tree", schema="newick")


# In[3]:

tt.taxon_set.labels()


# In[4]:

mrcaset = ["Carcharodon carcharias", "Lamna nasus"]


# In[5]:

tt.mrca(taxon_labels=mrcaset)


# In[6]:

subtree = tt.mrca(taxon_labels=mrcaset)


# In[8]:

subtree.as_newick_string()


# In[9]:

out = open("pruned_sharks.tree", "w")


# In[10]:

outtree = subtree.as_newick_string()


# In[11]:

out.write(outtree)


# In[12]:

out.close


# In[13]:

#from here I need to make a request to get the spatial coordinate datas from OBIS/GBIF
#I wasn't sure how I could use the 5 species in the subtree string and loop the request info and connect it together


# In[14]:

#the next script is manually getting the latitude and longitude values from the downloaded csv file from OBIS


# In[15]:

import csv


# In[16]:

f = open("carcharodon.csv")


# In[17]:

csv_f = csv.reader(f)


# In[18]:

latitudes = []
longitudes = []


# In[20]:

for column in csv_f:
    latitudes.append(column[6])
    longitudes.append(column[7]) 


# In[21]:

print str(latitudes)


# In[22]:

print str(longitudes)


# In[ ]:

#Next need to plot the latitude and longitude points onto a map

