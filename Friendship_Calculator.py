alphabet = 'bcghjklmpqrtvwxyz'
score = 0
names = input('Enter First name and give space and than enter second name:-')
for charatcter in names:
    if charatcter in 'aeiou':
        score+=5
    if charatcter in 'friends':
        score+=10
    if charatcter in alphabet:
        score+=0
if score>100:
    print('your friendship score is:',score)
    print('Confratulations! you both are best friends')
else:
    print('Your friendship score is:',score)
