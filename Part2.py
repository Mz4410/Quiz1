import pandas as pd
import datetime
from os import listdir
from os.path import isfile, join
import glob
import re

df = pd.read_csv("https://raw.githubusercontent.com/marwagaser/Quiz1-CSEN1095/main/CSVs/salesMinimized%20-%20salesMinimized.csv?token=AGGO3KVVFYGJFHNYW7N726S7WPBBY")
df
 
id_vars = ['d_1',d_2,d_3,d_4,d_5,d_6,d_7,d_8,d_9,d_10,d_11,d_12,d_13,d_14,d_15,d_16,d_17,d_18,d_19,d_20,d_21,d_22,d_23,d_24,d_25,d_26,d_27,d_28,d_29,d_30,d_31,d_32,d_33,d_34,d_35,d_36,d_37,d_38,d_39,d_40,d_41,d_42,d_43,d_44,d_45,d_46,d_47,d_48,d_49,d_50,d_51,d_52,d_53,d_54,d_55,d_56,d_57,d_58,d_59,d_60,d_61,d_62,d_63,d_64,d_65,d_66,d_67,d_68,d_69,d_70]

df = pd.melt(frame=df,id_vars=id_vars, var_name="dNumber", value_name="occurence")


df["dNumber"] = df['dNumber'].str.extract('(\d+)', expand=False).astype(int)
df["occurence"] = df["occurence"].astype(int)

df = df.dropna()


billboard = df

df.head(10)