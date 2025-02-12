# %%
import pandas as pd
#read chosen file
coffee_df = pd.read_csv('data_for_coffee.csv') #encoding='unicode_escape')
#replaces NaNs with arbitrary values on given data frame
#new_df = coffee_df.fillna(9)

 
#position_df = coffee_df['Position (m) Run #4']
new_list = []
def mainCleanData():
    j = 0 #arbitrary pointer for cut, it advances by 4 because the position column for each run is 4 columns away
    positions_df = coffee_df.iloc[:,1::4] #all position columns in the main_df
    num_columns = len(positions_df.columns) #number of columns -4 to look ahead
    for column in range(num_columns): #there are 4 columns for this type of csv file, but we want to access the position ones
        position = positions_df.iloc[:,column] #individual column
        first_index = minVal(position)
        first_truncated_df = coffee_df.iloc[:first_index-6, j:j+4] #truncate first all values from the end to first index that go with i run, -6 in order to reduce errors on the first cut
        sec_index = cutStart(first_truncated_df)
        second_truncated_df = first_truncated_df.iloc[sec_index:, :4]
        second_truncated_df.plot(kind="line", x = second_truncated_df.columns[0], y = second_truncated_df.columns[1])#graphs for each run 
        new_list.append(second_truncated_df)#put each group of 4 columns in a list
        j+=4
        #print(second_truncated_df)

    return new_list
        

#Function that finds the minimum value in position and returns its index
def minVal(position):
    index = 0
    min = position.iat[0]
    for i in range(1, len(position)-1):
        curr = position.iat[i]
        if curr < min:
            min = curr
            index = i
    #print(index)
    return index



#Function that gives index to make cut at the start
def cutStart(first_truncated_df):
    for i in range(len(first_truncated_df)-7):#checked with 7 values,it should be big enough to check the start of the descent
        temp_df = first_truncated_df.iloc[i:i+7, [1]]
        flag = 0
        #print(temp_df)
        for j in range(len(temp_df)-1):#checks if the next 7 values go down(reverse list type of problem)
            if temp_df.iat[j, 0] <= temp_df.iat[j+1, 0]:
                flag = 1
        if not flag:
            return i


mainCleanData()
# %%
