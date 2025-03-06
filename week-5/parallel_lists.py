def new_sighting(kinds: list[str], count: list[int], sighting: str) -> None:
    '''
    add new sightning and upgrade count
    '''
    if sighting not in kinds:
        kinds.append(new_sighting)
        count.append(1)
kinds = ["Monarch", "Painted Lady", "Bronze Copper", "Orange Sulphur"]
count = [5,3,2,14]


new_sighting(kinds, count, 'Common Blue')

for i in range(len(kinds)):
    print(f'{kinds[i]}: {count[i]}')