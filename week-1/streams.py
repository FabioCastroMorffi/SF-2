def int_list(list_str: list) -> list:
    for i in range(len(list_str)):
        list_str[i] = int(list_str[i])
    return list_str
def split(stream,percentage_split, volume_water):
    new_volume = volume_water[:stream-1] + [(volume_water[stream-1] * percentage_split / 100)] + [volume_water[stream-1] * (100 - percentage_split) / 100] + volume_water[stream:]
    return new_volume
def merge(stream: int, volume_water: list):
    new_volume = volume_water[:stream-1] + [volume_water[stream-1] + volume_water[stream]] + volume_water[stream +1:]
    return new_volume

num_streams = int(input()) 
volume_water = int_list(input().split())
commands = int_list(input().split())
i = 0



while i < len(commands):
    if commands[i] == 99:
        volume_water = split(commands[i+1],commands[i+2], volume_water)
        i += 3
        
    if commands[i] == 88:
        volume_water = merge(commands[i+1], volume_water)
        i += 2
    if commands[i] == 77:
        break
    
    
print(volume_water)

   


    

