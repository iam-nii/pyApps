import lists

toVisit = ['sweden', 'the grand canyon', 'thailand', 'hamburg', 'south africa', 'tanzania']
print(f"original list: {toVisit}")

print(f"using sorted() to print the list: {sorted(toVisit)}")

print(f"proof that the list is still in its original order: {toVisit}")

print(f"printing the list in reverse alphabetical order using sorted(): {sorted(toVisit,reverse=True)}")

print(f"proof that the list is still in its original order: {toVisit}")

toVisit.reverse()
print(f"printing the list in a reversed order using reverse():{toVisit} ")

print(f"reversing the earlier revered list using reverse():{toVisit} ")

toVisit.sort()
print(f"using sort() to print the list: {toVisit}")
toVisit.sort(reverse=True)
print(f"using sort() to print the list: {toVisit}")

print(f"\nTell the bar man that there will be {len(lists.invitation)} people at the dinner")