import numpy as np

players=np.array(["Cristiano Ronaldo","Lionel Messi","Neymar Jr","Mbappe"])
scores=np.array([ 
    [99,85,78,90],
    [88,67,78,56],
    [84,89,96,69],
    [80,77,90,92]
])

print("\n----players and scores----")
for i in range(len(players)):
    print(players[i],":",scores[i])

print("\n----Each player total scores----")
total_score=np.sum(scores,axis=1)
for i in range(len(players)):
    print(players[i],":",total_score[i])

print("\n----Average score----")
avgScores=np.mean(scores,axis=1)
for i in range(len(players)):
    print(players[i],":",avgScores[i])

print("\n----Best score----")
bestScores=np.max(scores,axis=1)
for i in range(len(players)):
    print(players[i],":",bestScores[i])

print("\n----Best player----")
best_index=np.argmax(avgScores)
 
print(players[best_index],":",avgScores[best_index])

print("\n----Consistency----")
consistency=np.std(scores,axis=1)
for i in range(len(players)):
    print(players[i],"std :",round(consistency[i],2))  

mostConsistent=np.argmin(consistency)
print("most consistent player:",players[mostConsistent])  

print("\n----Performance----")
level=np.where(avgScores>=85,"PRO",np.where(avgScores>=50,"AVG","needs practice"))
for i in range(len(players)):
    print(players[i],":",level[i])

print("\n----Players in form----")   
last_match=scores[:,-1]

print("Last match scores:",last_match)

in_form=players[last_match>50]
print("\n Players in form:")
print(in_form) 

print("\n----Filtered----")
print("players with avg>60:")
print(players[avgScores>60])

print("\n Players with any match score>90:")
print(players[np.any(scores>90,axis=1)])

print("\n----Sorted average----")
sorted_avg=np.sort(avgScores)
print(sorted_avg)

print("\n----Improved scores----")
improved_scores=scores+10
print(improved_scores)

print("\n----Final summary----")
print("overall game average:",np.mean(scores))
print("highets score:",np.max(scores))
print("lowest score:",np.min(scores))

print("\n----End----")


#To push on github after finishing:
# Run : git add .
# Run : git commit -m "Some msg"
# Run : git push 