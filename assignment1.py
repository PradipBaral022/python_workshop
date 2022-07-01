
staff=[]

def find_max(value):
    max = value[0]
    for val in value:
        if(max<val):
            max = val
    return max

for i in range(3):
    roll = input("Enter you roll number:")
    name = input("Enter your name:")
    scores = input("enter you scores:")
    item = {"roll": (roll), 
            "name": (name),
            "scores": int(list(scores))
    }
    staff.append(item)
    

for item in staff:
    score = item["scores"]
    max = find_max(score)
    print(max)
    item["scores"] = max

print(staff)
