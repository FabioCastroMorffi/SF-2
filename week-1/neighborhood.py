def small_neighborhood(nmb_villages: int, positions: list) -> int:
    last_small = 99
    for i in range(1,nmb_villages-2):
        positions.sort()
        neighborhood_size = ((positions[i+1] - positions[i]) / 2) - ((positions[i-1]-positions[i]) / 2 )
        if neighborhood_size <  last_small:
            last_small = neighborhood_size
    print(last_small)
small_neighborhood(5,[0,4,10,15,16])


