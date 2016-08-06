import dateutil
import read

def hours(x):
    y = dateutil.parser.parse(x)
    return y.hour
def days(x):
    y = dateutil.parser.parse(x)
    return y.day
def years(x):
    y = dateutil.parser.parse(x)
    return y.year
def weekdays(x):
    y = dateutil.parser.parse(x)
    return y.weekday()




def get_time():
    # return and print hours
    df['hours']=df['submission_time'].apply(hours);
    df['day']=df['submission_time'].apply(days);
    df['year']=df['submission_time'].apply(years);
    df['weekday']=df['submission_time'].apply(weekdays);

if __name__ == "__main__":
    # Read the csv file
    df = read.load_data();
    df=df.get_time();
    print(df['hours'].value_counts());
    print(df['day'].value_counts());
    print(df['year'].value_counts());
    print(df['weekday'].value_counts());

