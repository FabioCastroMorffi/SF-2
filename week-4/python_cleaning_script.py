# Your code for steps 6-9 go here:
import pandas as pd
#read chosen file

#replaces NaNs with arbitrary values on given data frame
#new_df = data_df.fillna(9)
single_filter_df = pd.read_csv('data_with_terminal_speed.csv', encoding='unicode_escape')


data1_df = single_filter_df.iloc[:, 0::4]
data2_df = single_filter_df.iloc[:, 1::4]
data_df = pd.concat([data1_df,data2_df], axis = 1)
data_df = data_df.fillna(0) 
#position_df = data_df['Position (m) Run #4']
clean_df = pd.DataFrame()
def mainCleanData(data_df, clean_df):
    positions_df = data_df.iloc[:,11:] #all position columns in the data_df, 11 cause we had 11 runs
    num_columns = len(positions_df.columns) #number of columns
    for column in range(num_columns): 
        position = positions_df.iloc[:,column] #individual column
        first_index = minVal(position)
        first_truncated_df = data_df.iloc[:first_index-6, [column,column+11]]
        #(first_truncated_df)# -6 in order to reduce errors when cutting right, also want to truncate time that column that goes with it
        second_index = cutStart(first_truncated_df)
        second_truncated_df = first_truncated_df.iloc[second_index:, :]
        print(second_truncated_df)
        second_truncated_df.plot(kind="line", x = second_truncated_df.columns[0], y = second_truncated_df.columns[1])#graphs for each run 
        clean_df = pd.concat([clean_df,second_truncated_df], axis=1)
        print(clean_df)
        #print(second_truncated_df)

    return clean_df
        

#Function that finds the minimum value in position and returns its index
def minVal(position):
    index = 0
    min = position.iat[0]
    for i in range(1, len(position)-1):
        curr = position.iat[i]
        if curr < min and curr:
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


print(mainCleanData(data_df, clean_df))
# %%
