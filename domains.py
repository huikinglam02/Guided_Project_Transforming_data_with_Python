import read
import pandas as pd
import numpy as np
import tldextract

#def trim_domain_names(df):
    #domain_occurances=df_cleaned['url'].str.split('.');
# Reading of the data
df=read.load_data();
# Cleaning of NaN rows
df_cleaned=df.dropna();

urls=df_cleaned['url'].tolist();
for url in urls:
    ext = tldextract.extract(url);
    url=ext.registered_domain;

se = pd.Series(urls)
df_cleaned=df_cleaned.reset_index(drop=False);
#print(df_cleaned);
#print(se)
df_cleaned['clean_url']=se;
#print(df_cleaned)

# Count number of occurances
domains=df_cleaned['clean_url'].value_counts();
# Print out the number of occurances
for name, row in domains.items():
    print("{0}: {1}".format(name, row));