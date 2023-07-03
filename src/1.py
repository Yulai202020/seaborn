from data import *
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

plt.plot(x,x_multby2)

sns.lineplot(x="var",y="x_multby2")

plt.grid(True)
plt.tight_layout()

plt.savefig("mygraph.png")