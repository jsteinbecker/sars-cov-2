def dictExplode (Dict,headName):

    k, v = Dict.items()
    for val in v:
        val.update({headName: k})
    out = dict(map(k,v))
    
    return out