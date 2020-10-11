%reset -f
# Above clears out everything in memory each time the code is run.
import pandas as pd
# Above pulls in the pandas library for data analysis.
import numpy as np
# Above pulls in the numpy scientific computing library.

################################################################################
########################### Attributions #######################################

# Daniel Chen "Pandas for Everyone"
# Allen Downey "Think Python"
# Yves Hilpisch "Python for Finance"
# Wes McKinney "Python for Data Analysis"
# Theodore Petrou "Pandas Cookbook"
# Jake VanderPlas "Python Data Science Handbook"

################################################################################
################################################################################

# Shift + Enter runs individual lines or code or hi-lited blocks of code in Atom.

# First, let's change the directory to c:\tools\Python\returns and the look at what directory we are operating in. If you have not already created this folder you can type, without the leading "#":
# %mkdir c:\tools\Python\returns

# Next, put the Excel file returns.xlsx into the c:\tools\Python\returns folder regardless of the method you used to create the folder.
# then type:
# %cd c:\tools\Python\returns

# without the '#' to change into that working directory. 

# Below, use pwd to see what directory we are operating within and then "ls" to list the contents of the directory.
%pwd
%ls
# Next, read in the returns.xlsx Excel file as a Python DataFrame named "df"
df= pd.read_excel('returns.xlsx')

# See everything that has been loaded thus far into our interactive space. You can see two modules and one DataFrame. The DataFrame contains the stock market data for several companies.
%whos

# Next, let's take a look at the first five observations in the DataFrame. Note that in Python indices start from 0 rather than 1.
df.head()

# PERMNO, Ticker Symbol, and Company Name are all company identifiers. Names Date is a timestamp formatted as year-month-day (YYYY-MM-DD), Standard Industry Classification is the four-digit SIC code the company operates within. Price or Bid/Ask Average is the stock price, Returns is the monthly return including any dividends i.e., (P1+Div-P0)/P0. Returns without Dividends is (P1-P0)/P0, and the Return on the S&P 500 Index is our proxy for the market return.

# The variables above are sometimes all caps (PERMNO) and sometimes with caps in the first letters (Ticker Symbol) and sometimes a mix (Returns without Dividends). In Python, we will write code referencing variable names (i.e., column headings or fields) so it's a good idea to standardize these by renaming the columns.

# This is how to rename a single column to make it lower case. You can also use this to change the name of any individual column. The "inplace=True" option is telling pandas we want to modify the DataFrame.
df.rename(columns= {'PERMNO': 'permno'}, inplace=True)
df.head()

%whos
# Alternatively, we could look at the index of the column names.
df.columns

# Or even refer to each element of the index by its position in the index. What do you think we will see if we refer to the element 1?
df.columns[1]
# Remember that Python indices start from 0, so [1] is actually the second column in the DataFrame. So above we see "Names Date" rather than "permno"
# We can also refer to the last column by using "-1" as the index we want.
df.columns[-1]
# Or, we can get the length of the index using "len"
len(df.columns)
# Note above that while the number 9 is returned, this starts with 0 so the index position of the last column is 8 and not 9.
df.columns[8]
# Subtracting 1 from the length of the index will give us the proper index number to reference.
len(df.columns)-1
# and we can also feed the above to return the last index.
df.columns[len(df.columns)-1]

# Next, rather than rewriting all of the column names to lower case manually, let's use .str and .lower() to do this automatically.

df.columns= df.columns.str.lower()
df.head()

%whos

# You can see above that each column name is now all in lower case. Let's now rename some of these to make them easier to work with later. Note that we will use the column position rather than writing out the entire name of each column.

df.rename(columns= {df.columns[2]: 'sic'}, inplace=True)
df.head()

# inplace illustration. df has not changd below.
df.rename(columns= {df.columns[2]: 'GOTCHA'})
df

%whos

# We can return a pandas Series object by referring to one column in the dataframe. There are a few ways to do this shown below. First, we pull the series based on its position. 
df[df.columns[2]]
type(df[df.columns[2]])
# Illustration of .loc where we select all rows with : and then the column. 
df.loc[:, df.columns[2]]
# Create the same series using the name of the column. 
df['sic']

# Now let's take care of the rest of them. I am using a mix of column positions and column names for illustrative purposes.
df.rename(columns= {df.columns[1]: 'date', 'ticker symbol': 'ticker', df.columns[4]: 'name', df.columns[5]: 'price', 'returns': 'ret', df.columns[7]: 'retx', df.columns[8]: 'sp' }, inplace=True)

df.head()

# Above you can see that when we were naming something with words, we needed to put '' around the name. This tells Python that we are referring to a string. We also used a dictionary when renaming columns. Let's take a quick detour and look at dictionaries, lists, strings, loops and functions below before we return to analyzing the DataFrame we have.
string= 'a'
# Note that typing: string = a , without the quotes, will return an error since a is not defined.
type(string)
%whos

# But we also used a dictionary which contains key:value pairs.
dict= {'Floyd Mayweather': 'Welterweight', 'James Toney': 'Heavyweight'}
dict
type(dict)
%whos

# Return all keys in the dictionary
dict.keys()
# Return all the values in the dictionary
dict.values()
# Return the value associated with a particular key
dict.get('James Toney')

# Delete the dictionary we created and the string variable.
del dict, string

# Python also has list objects. Let's create two separate lists and then turn them into a dictionary.
keys= ['a', 'b', 'c']
values=[0, 3, 1]

type(keys)
dict= dict(zip(keys, values))
dict
%whos

# We can positionally refer to each element of the list similar to positionally referencing the previous index.
keys[0]
keys[1]
keys[2]

# Below are two examples of loops in Python. The first adds one to each item in the value list.
values

for i in values:
    print(i)


for i in values:
    print(i+1)

# The second uses control flow to do something as long as one condition is met and to do something else if a second condition is met.
for i in values:
    if i != 3:
        print(i+1)
    else:
        print('Excluded')

# We can also define a function in Python to do something. This function takes whatever number we set "input" to be and returns that number divided by two. The input is referred to as a "parameter" of the function and the actual values we pass in are known as "arguments."
def divide_by_two(input):
    return input/2

%whos
divide_by_two(50)
divide_by_two(125)


# typing: divide_by_two('abcd') will return an error since one would be trying to do a mathematical operation to a string.

# The function below is set up to take two parameters: the number to be divided and the divisor.
def divide_by_user_specified(a, b):
    return a/b

divide_by_user_specified(50 ,1)


divide_by_user_specified(50 ,2)
divide_by_user_specified(200 ,30)

# Take a look again at the interactive variables. You will see that our functions are now listed.
%whos

# Let's remove some things we created that we don't need anymore.
del keys, values, dict, i
%whos

# Back to analyzing the DataFrame. First, let's see how many rows and columns there are in df. The number of rows (i.e., observations or records) is first and the number of variables (i.e., columns or fields) is second.
df.shape

# Next, return the data types for each variable in the dataset.
df.dtypes

# permno and date are integers (int64), price, ret, retx, and sp are floats (float64) which means they have numbers to the right of a decimal point. ticker and name are 'object' types, and this means they have been stored as strings.

df.head()

# The date variable is currently stored as an integer so .describe() will treat it as any other numeric variable. The results below are actually meaningless to us.

%whos
df['date'].describe()

# Let's turn off the scientific notation display.
pd.set_option('display.float_format', lambda x: '%.5f' % x)

df['date'].describe()

# You can see from the summary statistics returned above that 'date' is being treated like an integer and not a date. This is expected based on the int64 format. Below, we convert 'date' into 'date_2' which is a datetime variable.

df['date_2']= pd.to_datetime((df['date']), format='%Y%m%d')

list= ['ticker', 'date', 'date_2']
type(list)
df[list].head()

df[['ticker', 'date', 'date_2']].head()
df.dtypes
df['date_2'].describe()
df.head()
# As seen above, there is a time component of the variable (hours, minutes, seconds). You can also see how .describe() is no longer returning the standard deviation 'std' or average 'mean' on the datetime64[ns] object. The earliest date in the dataset is 1/31/2012 and the last date is 12/29/2017. This is for the entire dataset- we don't know yet if we have a balanced panel or not (i.e., we don't know if we have the same time periods for all firms... or even how many firms are in the dataset. We will explore that shortly.)

# Let's create 'date_3' which removes the hours, minutes, and seconds from date_2.
df['date_3']= pd.to_datetime((df['date']), format='%Y%m%d').dt.date
df.dtypes
# Above output makes it look like 'date_3' is an object, but per https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.dt.date.html it is a date object. Below, the describe output is slightly different from that given by 'date_2'
df['date_3'].describe()
df.head()

df[['date', 'date_2', 'date_3']].describe()
# Above only summarizes 'date', since this is the only numeric variable that was given. Below, we use the "include= 'all'" option for the others.
df[['date', 'date_2', 'date_3']].describe(include='all')

# You can see the difference in how 'date_2' and 'date_3' are treated. Let's drop the date variables we don't need and then rename the one we will retain.

df.drop(['date', 'date_3'], axis=1)
df

df.drop(['date', 'date_3'], axis=1, inplace=True)
df
# Above, 'axis=1' tells Python to operate down the column axis.
df.rename(columns= {'date_2': 'date'}, inplace=True)

df.head()
# Before going further, let's look at the summary statistics for the data and see if anything jumps out. Before we run various analyses, we want to get an idea about the data and see if there are things like missing values or values that are clearly erroneous. This step is known as exploratory data analysis, and it is extremely important to the analytics process. It typically includes things like looking at various graphs of variables plotted against each other (e.g., a scatter plot of y and x), graphs of one variable over time, looking at histograms, counts, and summary statistics (e.g., mean, maximum, minimum, standard deviation, and percentiles). This has the benefits of getting the analyst more familiar with the data and is a spot check for data input errors or conventions that could impact the results of the analyses. For example, some datasets include "99" or "-99" for missing values. Imagine not reading the data dictionary and calculating the average of something you are interested in that has a bunch of -99's in as values!
df.describe()

# The summary stats for permno and sic are meaningless. Price appears strange because the minimum is a negative number. Negative stock prices don't really exist. This is an artifact of the CRSP using a leading "-" sign if price is generated off using the average of the bid and ask. A negative return of 44.98% and a positive return of 65.53% on a monthly basis is also something we should look into a little closer- not that these can't happen, but just that we want to take a closer look. The return on the s&p 500 is much less volatile than the returns for the individual stocks. This is not surprising. Price also appears reasonable other than the negative minimum.

# Below, I am using .loc to find the "index" of a return that meets a certain logical condition. The minimum return is -.44979, but I am using -.44 as the condition for the check.

df.head()
df.loc[df['ret']<= -.44]

# Can see above that the index is 476 for this observation. Our index is a row number identifier. Below, we will return a "slice" of two indices to look at the data and manually calculate the return.
df.loc[475:476]

(2.63/4.78)-1

# The lower bound of the return appears reasonable. p/f/r.

# Similar procedure for the maximum return.
df.loc[df['ret']>= .65]

df.loc[485:486]

(3.41/2.06)-1

# The maximum return also appears reasonable. p/f/r.

# Now for the negative price or prices...
df.loc[df['price']<=0]

# The negative prices are all connected to one firm. Googling the ticker, 'BDL', reveals that these prices appear accurate once we strip off the minus sign. Another option would be to exclude this firm from the analysis if one could argue that firms with prices obtained from bid/ask averages, which is how the data provider tags prices with leading minus signs, were systematically different from the other firms. I'm going to assume that we can include these for our purposes and will convert the negative values to positive.

# Let's create a function that will multiply each negative value of what we feed into it by negative 1 and do nothing for positive values.
def undo_negative(series):
    if series < 0:
        series= series * -1
        return series
    else:
        return series

# Next, change the price variable to be equal to price after applying out function to each element of the series. It may seem strange to you that we haven't explicitly written: undo_negative(df['price']), but by linking the column of the DataFrame we want to apply the function to with '.apply(undo_negative)', we have done all we need to do to tell the function which series we are feeding into it. Note: think of a series as a single column of a DataFrame. See below.
series=df['ret']
series
type(series)
%whos

# Now back to applying the function above to a series of the DataFrame.
df['price']= df['price'].apply(undo_negative)
df['price'].describe()

df.head()
# The minimum price is now 1.50, so it appears our function worked. Let's look again at the prices for BDL.
df.loc[df['ticker']=='BDL']

# Can see above that there are "..." where pandas is not displaying all of the rows. We can modify that setting below
pd.set_option('display.max_rows', None)

df.loc[df['ticker']=='BDL']

# Now that we have looked at summary statistics and checked into values that appear to perhaps be unreasonable, let's move on with the analysis.

# Question 1: What are the starting and ending dates for each firm?
# Question 2: Do we have the same number of observations for each firm (i.e., is this a balanced panel?)

# To answer these, we are going to feed in a list of columns from the DataFrame, then use "groupby" and "describe"
df[['date', 'name']].groupby('name').describe()

# Answer 1: 1/3/2012 and 12/29/2017, respectively.
# Answer 2: Yes. This is a balanced panel.

# Question 3): How many times were dividends paid?
# Question 4) What was the average dividend?
# Question 5) What was the largest dividend?
# Question 6) Which firm paid the highest dividend?
# Question 7) Which firm paid the lowest dividend?
# Question 8): How many firms paid dividends?

# The dataset above doesn't directly have the amount of the dividend, but using the formulas for the returns we know that the dividend will be the difference between the ret and retx (i.e., ret- retx= div). Let's see how often ret is not equal to retx.
df[['ticker', 'date', 'ret', 'retx' ]].loc[df['ret'] != df['retx']]
len(df[df['ret']!= df['retx']])

# Answer 3: There are 97 months where dividends were paid.

df['div']= df['ret'] - df['retx']

df['div'].describe()

# Answer 4: The average dividend was .00141.
# Answer 5: The largest dividend was .01237.

max_div=  df['div'].describe()
max_div
%whos
max_div.loc['max']

df.loc[df['div']== max_div.loc['max']]

# Answer 6: Chevron paid the highest dividend.

# To answer Question 7 we can't simply take the minimum of the max_div series since the minimum is 0 since the variable includes firms that did not pay dividends. We need to take the minimum of firms that actually paid dividends. So, the minimum of where df['div'] is > 0.
temp= df['div'].loc[df['div'] > 0].describe()
temp

# We know from Question 3 that dividends were paid 97 times. We should keep this in mind when we review the results of the above. It would not make sense for us to condition on firms that only paid dividends, summarize these dividends, and see a different "count" returned by .describe(). When we are writing code and working with data to create new variables, we always want to test results or ball park results for reasonableness.
df.dtypes

df.loc[df['div']== temp.loc['min']]

# Answer 7: Apple paid the smallest dividend, and again the dividend of .00373 lines up with the minimum of the summary statistics for firms that paid dividends. Reconciling these makes us feel more confident that the code we have written is accurate.

# Firms with a maximum dividend of 0 did not pay dividends. Below we will identify the maximum dividend for each company.
df['div'].groupby(df['ticker']).max()
# Above we can see the maximum dividend listed for each firm and easily see that two firms did not pay dividends, but this may not be feasible for large datasets or we may need to work with this number later rather than just seeing it for ourselves. Note the parentheses below around the conditional statement:
(df['div'].groupby(df['ticker']).max() ==0).sum()

# Answer 8: Two of the seven firms (AMZN and CLD) did not pay dividends.

# Say we wanted to pull in the maximum dividend paid for each firm as a variable/column/field in the DataFrame. Below uses .transform() and NumPy's maximum.
df['paid']= df['div'].groupby(df['ticker']).transform(np.max)

df.head(80)

df.head()

df.head()
df.loc[df['ret'] >= .13751, 'Lawrence']= 'Something Else'

df['Lawrence'].value_counts()

df.loc[df['ticker']== 'MSFT']
df['ticker']== 'MSFT'
df['ticker']

df.head(100)


# Again, the results in the DataFrame for MSFT and XOM line up with the previous results. We need to continually consider whether our code and modifications to the DataFrame are accurate otherwise the results of our analyses may be erroneous which could lead consumers of the analyses to make incorrect decisions. Spot checking results, manually calculating things in Excel and comparing to the DataFrame, and doing a few individual operations and reconciling to the results of what automated loops return are all good practices.

# Question 9: What was the average monthly return, including dividends?
df['ret'].mean()
# Answer 9: .01367

# Question 10: What was the average return for each year, excluding dividends?
# To answer the above, first we need to create a year variable which is the year component of the date variable.
df['year']= df['date'].dt.year

# Let's spot check the code we wrote for accuracy
df.head(20)
df.tail(10)

# Appears reasonable. p/f/r
df['retx'].groupby(df['year']).describe()
# Answer 10: Refer to the above results.

# Question 11: What was the average return, including dividends, for each firm for each year?
# To answer the above, we will group by both firm and year.
df['ret'].groupby([df['year'], df['ticker']]).mean()
# Or
df['ret'].groupby([df['year'], df['ticker']]).describe()

# Answer 11: Refer to the above results.

# Question 12: What was the average return for XOM for each year.
df['ret'].loc[df['ticker']== 'XOM'].groupby(df['year']).mean()

# Answer 12: See above results. Again, the results returned for XOM here line up with our previous results.
