def calculate_love_score(name1, name2):
    n1 = (name1 + name2).lower()
    p1 = "true"
    p2 = "love"
    b1 = 0
    b2 = 0
    for i in n1:
        if i in p1:
            b1 += 1
        else:
            b1 += 0
    for i in n1:
        if i in p1:
            b2 += 1
        else:
            b2 += 0

    print(f"{b1}{b2}")
     
calculate_love_score("Andika Setiawa", "Anggia Putri Andini")