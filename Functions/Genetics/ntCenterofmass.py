x='gcactagctttgataggggcgggcgtg'

def ntCenter(seq):
    """
    FUNCTION WILL RETURN AN ARRAY WITH VALUES:
    NUCLEOTIDE, 
    AVERAGE POSITION IN CHAIN, AND 
    %DISTANCE TO THE TRUE CENTER
    """
    centers = []

    for nt in 'acgt':
        ind = []
        
        for i in range(len(seq)):
            if seq[i] == nt:
                ind.append(i)

        center = sum(ind)/len(ind)
        center = int(center)

        dist = round(((0.5 * len(seq)) - center) / len(seq),2)
        centers.append([nt,center,dist])

    return centers

print(ntCenter(x))