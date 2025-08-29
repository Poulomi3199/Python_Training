# Assignment 1
scores = []
scores.extend(['85', '90', '78', '92', '88'])
print("Scores : ", scores)
scores.insert(5, '80')
print("Scores : ", scores)
scores.remove('92')
print("Scores : ", scores)
scores.sort()
print("Scores : ", scores)
scores.reverse()
print("Scores : ", scores)
print("Maximum number = ", max(scores))
print("Minimum number = ", min(scores))
print("Is 90 is present inside this list ? ", '90' in scores)
print("Total number of element present : ", len(scores))
print("First 3 items in scores : ", scores[:3])

# Assignment 2
print("Last element: ",scores[-1])
scores[2] = 100
print("Scores : ", scores)

copiedScore = scores.copy()
print("copiedScore : ", copiedScore)

print("*"*50)
#Assignment 3
marks = 85

if (marks > 90):
    print("Grade A")
else:
    if (marks > 80):
        print("Grade B")
    else:
        if (marks > 70):
            print("Grade C")
        else:
            if (marks > 60):
                print("Grade D")
            else:
                print("Grade E")