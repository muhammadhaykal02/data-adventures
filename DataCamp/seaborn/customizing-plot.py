# preset white (default), dark, whitegrid, darkgrid, ticks
sns.set_style("the preset")

# changing the palette, theres a preset
# diverging: RdBu, PRGn, RdBu_r, PRGn_r
# sequential: Greys, Blues, PuRd, GnBu

sns.set_palette("the preset")

# you can create custom color palette using a list.
custom_palette = ['#xxx', '#xxx', '#xxx', ]

# changing scale: paper (default), notebook, talk (bigger), poster
sns.set_context()

# adding title and labels
# first determine the objects we are working on, is it FacetGrid or AxesSubplot

g = sns.scatterplot(x="height", y="weight", data=df)
type(g)

# FacetGrid = 1++ AxesSubplot (relplot and catplot)
# AxesSubplot = only create singleplot (scatterplot, countplot)

### ADDING TITLE TO FacetGrid ###
# first assign the plot into a variable
g = sns.catplot(x="Region", y="Birthrate", data=gdp_data, kind="box")
g.fig.suptitle("New Title", 
               y=1.03) # adjust the height, default 1
plt.show()

### ADDING TITLE TO AxesSubplot ###
g = sns.catplot(x="Region", y="Birthrate", data=gdp_data)
g.set_title("New Title", 
               y=1.03) # adjust the height, default 1
plt.show()

### ADDING LABELS ###

g.set(xlabel="New X Label",
      ylabel="New Y Label")
plt.show()

### ROTATING TICKS ###
plt.xticks(rotation=90)
plt.show()
