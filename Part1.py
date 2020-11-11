import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm


dat = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv")
dat_bill=dat.loc[:,'bill_length_mm':'bill_depth_mm']
df = dat[['bill_length_mm','bill_depth_mm']]

sns.pairplot(df, kind="scatter")
plt.show()
plt.scatter(dat['bill_length_mm'], dat['bill_depth_mm'])
plt.show()
np.corrcoef(dat['bill_length_mm'], dat['bill_depth_mm'])

dat_bill1=dat.loc[:,'body_mass_g']
df1 = dat[['body_mass_g']]
df1.mean()


