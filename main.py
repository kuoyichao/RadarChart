import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import pi


df = pd.DataFrame({'client_id': ['Current Prosthesis', 'CyberLimb'],
                   'comfort': [8, 4],
                   'function': [7, 9],
                   'durability': [5, 5],
                   'appearance': [9, 6],
                   'cost': [3, 8]},
                   columns=['client_id','comfort', 'function', 'durability', 'appearance', 'cost'])
categories = list(df)[1:]

values = df.mean().values.flatten().tolist()
values += values[:1] # repeat the first value to close the circular graph

angles = [n / float(len(categories)) * 2 * pi for n in range(len(categories))]
angles += angles[:1]

#############
#fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8, 8),
#                       subplot_kw=dict(polar=True))

#plt.xticks(angles[:-1], categories, color='grey', size=12)
#plt.yticks(np.arange(1, 11), ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
#           color='black', size=12)
#plt.ylim(0, 10)
#ax.set_rlabel_position(30)

#ax.plot(angles, values, linewidth=1, linestyle='solid')
#ax.fill(angles, values, 'skyblue', alpha=0.4)

#plt.show()
###############
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8, 8), subplot_kw=dict(polar=True))

plt.xticks(angles[:-1], categories, color='grey', size=20)
plt.yticks(np.arange(1, 11), ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
           color='black', size=12)
plt.ylim(0, 10)
ax.set_rlabel_position(30)

# part 1
val_c1 = df.loc[0].drop('client_id').values.flatten().tolist()
val_c1 += val_c1[:1]
ax.plot(angles, val_c1, linewidth=1, linestyle='solid', label='Current Prosthesis')
ax.fill(angles, val_c1, 'skyblue', alpha=0.4)

# part 2
val_c2 = df.loc[1].drop('client_id').values.flatten().tolist()
val_c2 += val_c2[:1]
ax.plot(angles, val_c2, linewidth=1, linestyle='solid', label='CyberLimb')
ax.fill(angles, val_c2, 'lightpink', alpha=0.4)

plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

plt.show()
