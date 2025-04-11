#Fabio Castro Morffi 2438078

#Start of the assignment

def toCelsius(temp_F):
    return round(((temp_F - 32) * (5/9)),2) 

def avgTempYear(dict, year):
    try:
        existing_year = dict[year]
    except KeyError:
        print("The year is not present in the dictionary.")
    else:
        return (round(sum(existing_year)/len(existing_year),2))
    
def topThreeYears(dict):
    lst = []
    removal_set = set()
    for key in dict:
        curr_avg = avgTempYear(dict, key)
        removal_set.add(curr_avg)
    for i in range(3):
        maxes = max(removal_set)
        removal_set.remove(maxes)
        lst.append(maxes)
    return lst

        
    
def avgTempMonth(dict, month):
    avg_temp = []
    month_dict = {'JAN': 1, 'FEB': 2, 'MAR': 3, 'APR': 4, 'MAY': 5, 'JUN': 6, 'JUL':7, 'AUG': 8,'SEP':9 ,'OCT':10,'NOV':10,'DEC':12}
    for value in dict:
        avg_temp.append(dict[value][month_dict[month] -1])
    return round(sum(avg_temp)/len(avg_temp),2)

def belowFreezing(dict):
    lst_months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'September', 'October', 'November', 'December']
    set_months = set()
    for key in dict:
        for i in range(len(dict[key])):
            if dict[key][i] < 0:
                set_months.add(lst_months[i])
    return set_months



def main():
    input_file = open('data.txt', 'r')
    temp_dict = {}
    #lst_lines = input_file.readlines()
    for line in input_file:
        if line[0] == "1":
            line = line.rstrip().split()
            temp = list(map(float, line[1:]))
            temp_dict[int(line[0])] = list(map(toCelsius, temp))
    #print(temp_dict)
    #print(topThreeYears(temp_dict))
    input_file.seek(0)
    output_file = open("data_celsius.txt", 'w')

    flag = False
    for line in input_file:
        if not flag:
            if line[0] != '1':
                output_file.write(line)
            else:
                flag = True
    
    for key in temp_dict:
        output_file.write(f'{key}'+'\t')
        for i in range(len(temp_dict[key])):
            monthly_temp = temp_dict[key][i]
            if i == 11:
                #print(temp_dict[key][i])
                output_file.write(f'{monthly_temp}' + '\n')
            else:
                output_file.write(f'{monthly_temp}'+ '\t')

    output_file.close()
    input_file.close()
    

main()