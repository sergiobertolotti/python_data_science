photo1_tags = {'coffee','breakfast','drink','table','tabbleware', 'cup', 'food'}
photo2_tags = {'food', 'dish','meat','meal','tabbleware', 'dinner', 'vegetable'}

intersezione = photo1_tags.intersection(photo2_tags)
if len(intersezione) >= 2:
    print("The foto contains similar objects")