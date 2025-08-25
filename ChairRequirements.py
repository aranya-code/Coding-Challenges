# Chair Requirements Challenge




def MinChairs(simulations):
    chairs = []
    
    for simulation in simulations:
        chairCount = 0
        chair_needed = 0     
        for letter in simulation:            
            if letter == 'C' or letter == 'U':
                if chairCount == 0:
                    chair_needed+=1
                else:
                    chairCount-=1
            elif letter == 'R' or letter == 'L':
                chairCount+=1
        chairs.append(chair_needed)
    return chairs


    
print(MinChairs(['CCRUCL', 'CRUC', 'CCC'])) 