selected = []

def selection(item):
    global selected
    if item in selected:
        selected.remove(item)
    else:
        selected.append(item)
        


