import read
import matplotlib.pyplot as plt
import read
import time_dq


df=read.load_data();
# Find length of each string
df['headline_length']=df['headline'].str.len()

# Headline length vs. # of upvotes
fig = plt.figure()
ax = plt.subplot(2,2,1)
ax.scatter(df["headline_length"], df["upvotes"]);
ax.set_yscale('log')
ax.set_ylabel('# of upvotes')
ax.set_xlabel('Headline length');
print('Finished first graph');

# Get time from time stamp
df['hours']=df['submission_time'].apply(time_dq.hours);
ax = plt.subplot(2,2,2)
ax.scatter(df["hours"], df["upvotes"]);
ax.set_yscale('log')
ax.set_xlabel('submission hour')
ax.set_ylabel('# of upvotes')
print('Finished second graph');

df['years']=df['submission_time'].apply(time_dq.years);
ax = plt.subplot(2,2,3)
ax.scatter(df["years"], df["upvotes"]);
ax.set_yscale('log')
ax.set_xlabel('submission year')
ax.set_ylabel('# of upvotes');
print('Finished Third graph');

df['weekday']=df['submission_time'].apply(time_dq.weekdays);
ax = plt.subplot(2,2,4)
ax.scatter(df["weekday"], df["upvotes"]);
ax.set_yscale('log')
ax.set_xlabel('submission weekday')
ax.set_ylabel('# of upvotes')
print('You are done!');

plt.show()