import read
import collections

df=read.load_data();

headlines=df['headline'].tolist();
headline_long="";
for headline in headlines:
    headline_long+=str(headline).lower();
    headline_long+=" ";

headline_split=headline_long.split(' ');
#print(headline_split);
c=collections.Counter(headline_split);
print(c.most_common(10));