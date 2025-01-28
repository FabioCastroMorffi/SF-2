n = int(input())
streams = []
for i in range(n):
    streams.append(int(input()))
    
done = False
while not done:
    command = int(input())
    if command == 77:
        done = True
    elif command == 99:
        stream_num = int(input()) - 1# index 0
        percentage = int(input())
        left = int(streams[stream_num] * percentage/100)
        right= streams[stream_num] - left
        streams = streams[:stream_num] + [left,right] + streams[stream_num+1:]
    elif command == 88:
        stream_num = int(input()) -1
        right = streams[:stream_num+1] + [left+right] + streams[stream_num+2:]

answer = ''
for flow in streams:
    answer = answer + str(round(flow)) + ' '
print(answer[:-1])
