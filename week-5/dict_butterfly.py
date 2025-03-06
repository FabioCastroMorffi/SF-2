def new_sighting(butterfly_dict, sighting):
    #if sighting not in butterfly_dict:
    #    butterfly_dict[sighting] = 0
    #butterfly_dict[sighting] += 1
    butterfly_dict[sighting] = d.get(sighting, 0) + 1


butterflies = {'Monarch': 5, 'Painted Lady': 2, 'Bronze Copper': 5}
for kind, count in butterflies.items():
    print(f'{kinds}: {count}')