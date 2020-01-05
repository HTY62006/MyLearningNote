def addBorder(picture):
    for i in range(len(picture)):
        picture[i] = '*'+picture[i]+'*'
    new = '*'*len(picture[0])
    picture.insert(0, new)
    picture.append(new)
    return picture
