import random
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd
import csv

# dice1 = random.randint(1,6)
# dice2 = random.randint(1,6)
# print(dice1, dice2)

# count = []
# dice_result = []
# for i in range(0,100):
#     dice1 = random.randint(1,6)
#     dice2 = random.randint(1,6)
#     dice_result.append(dice1 + dice2)
#     count.append(i)

# fig = px.bar(x = dice_result, y = count)
# fig.show()    

# fig = ff.create_distplot([dice_result],["Result"])
# fig.show() 

df = pd.read_csv("data.csv")

fig1 = ff.create_distplot([df["Height(Inches)"].tolist()], ["Height"], show_hist= False )
fig2 = ff.create_distplot([df["Weight(Pounds)"].tolist()], ["Weight"], show_hist= False)
fig1.show() 
fig2.show()
