

def pouring(capacities, bottles, from_id, to_id):

    for index in range(0, len(to_id)):
        f = from_id[index]
        t = to_id[index]

        space = capacities[t] - bottles[t]

        if bottles[f] < space:
            bottles[t] = bottles[f] + bottles[t]
            bottles[f] = 0
        else:
            bottles[t] = capacities[t]
            bottles[f] = bottles[f] - space

    print (bottles)
    return bottles

pouring([30,20, 10], [10,5,5], [0,1,2], [1,2,0])



