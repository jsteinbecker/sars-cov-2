x='gcactagctttgataggggcgggcgtg'

def ntCenter(seq,letter):
    ind = []
    for i in range(len(seq)):
       if seq[i] == letter:
          ind.append(i)
    center = sum(ind)/len(ind)
    center = int(center)
    dist = round(((0.5 * len(seq)) - center) / len(seq),2)
    return letter, center, dist

for nt in 'acgt':
    ntCenter(x,nt)