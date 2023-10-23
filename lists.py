invitation = ['jody', 'beryl', 'fendi']

for x in invitation:
    print(f"hello, {x} i would like to invite you for an event on saturday!")

print(f"\nhello everyone, {invitation[0]} cannot make it unfortunately\n")

replacement = 'abigail'
invitation[0] = replacement
print(f"{invitation[0]} would stand in for her\n")

for x in invitation:
    print(f"hello, {x} i would like to invite you for an event on saturday!")

print("\nhurray! a bigger dinner table has been found, so there is more space available!\n")

invitation.insert(0, 'pokua')
invitation.insert(2, 'pearl')
invitation.append('lisbeth')

for person in invitation:
    print(f"hello, {person} i would like to invite you for an event on saturday!")

print("\nhey guys, it's me again :(, with not so good news\n")

while len(invitation) > 2:
    popped = invitation.pop()
    print(f"hey,{popped} sorry, i can't invite you to dinner anymore")
print("\n")
for person in invitation:
    print(f"hello, {person} i'd like to let you know that you're still being invited for dinner")

#while len(invitation) > 0:
 #   del invitation[0]
#print("\n")
#print(invitation)
