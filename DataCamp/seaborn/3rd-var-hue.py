# adding third variable with hue
# load dataset function in Seaborn

import pandas as pd
import seaborn as sns
tips = sns.load_dataset("tips")
tips.head()

# creating a basic scatter plot
import matplotlib.pyplot as plt
import seaborn as sns
sns.scatterplot(x="total_bill", y="tip", data=tips)
plt.show()

# in case you want to know which customers that pay a huge bill and give big tip is a smoker or not
# which is a third variable, add hue = "column you wanna add"
# another one, if you wanna order the color of the third variable, add hue_order=["yes","no"]
import matplotlib.pyplot as plt
import seaborn as sns
sns.scatterplot(x="total_bill", y="tip", data=tips, hue="smoker", hue_order=["yes","no"])
plt.show()

# changing the hue colors
# requires a dictionary with key-value pairs.
import matplotlib.pyplot as plt
import seaborn as sns
hue_colors = {"Yes":"black",
              "No":"red"}
sns.scatterplot(x="total_bill", y="tip", data=tips, hue="smoker", palette=hue_colors)
plt.show()

# you can use html color code (hex) for the colors, just replace the "black"/"red" with the hex #
