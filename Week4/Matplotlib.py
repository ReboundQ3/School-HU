#%%

import matplotlib.pyplot as mpl
import numpy as np

labels = ['Win7', 'Vista', 'NT*', 'WinXP', 'Linux', 'Mac', 'Mobile']
Sizes = [56.8, 3.0, 1.8, 22.1, 4.8, 9.2, 1.8]

fig, ax = mpl.subplots()
ax.pie(Sizes, labels=labels)

# %%
