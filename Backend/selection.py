selected = []

def selection(selected,item):
    if item in selected:
        selected.remove(item)
    else:
        selected.append(item)
    print(selected)
    return


