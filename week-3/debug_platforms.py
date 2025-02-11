def covers(platform, horizontal_pos,x2):
    '''
    :param platform: a platform as defined by the input of the question
    :param horizonal_pos: an integer
    :return : True if platform covers horizontal_post; False otherwise. 
    '''
    return (platform[1] > horizontal_pos and platform[2] > x2) or (platform[1]<horizontal_pos and platform[2] < x2)


def pillar_from(platforms, height, horizontal_pos, x2):
    '''
    :param platforms: a list of platforms (as lists)
    :param height: vertical position
    :param horizontal_pos: horizontal position
    :return : minimum length of pillar from heigh and horizontal_pos to the platform/ground below
    '''
    for platform in platforms:
        bottom = 0            
        if (platform[0] < height and covers(platform, horizontal_pos, x2)):
            bottom = platform[0]
    if bottom == 0:
        return 2 * (height - bottom)
    return (height - bottom) #only doing one leg if we miss the * 2


n = int(input())

platforms = []

# read input from user as lists of integers
for i in range(n):
    platform = input().split()
    print(platform)
    for j in range(len(platform)):
        platform[j] = int(platform[j])
    platforms.append(platform)

print(platforms)

total = 0

for platform in platforms:    
    total = total + pillar_from(platforms, platform[0], platform[1], platform[2])

print(total)
