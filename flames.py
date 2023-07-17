print('\t\t\t  ........FLAMES........')
def flames():
	a=input('\nenter the boy name : ')
	b=input('\nenter the girl name ; ')
	c=a+b
	s=set(c)
	g=(len(s))
	if g==1 or g==7 or g==13 or g==19 or g==25:
		a='Friend'
		print('\n\t\t\t\t==========\n\t\t\t\t= FRIEND =\n\t\t\t\t==========')
		pro(a)
	elif g==2 or g==8 or g==14 or g==20 or g==2:
		a='Love'
		print('\n\t\t\t\t========\n\t\t\t\t= LOVE =\n\t\t\t\t========')
		print('\n\t\t\t\t❤')
		pro(a)
	elif g==3 or g==9 or g==15 or g==21 or g==27:
		a='Affection'
		print('\n\t\t\t\t=============\n\t\t\t\t= AFFECTION =\n\t\t\t\t=============')
		pro(a)
	elif g==4 or g==10 or g==16 or g==22 or g==28:
		a='Marriage'
		print('\n\t\t\t\t============\n\t\t\t\t= MARRIAGE =\n\t\t\t\t============')
		pro(a)
	elif g==5 or g==11 or g==17 or g==23 or g==29:
		a='Enemy'
		print('\n\t\t\t\t=========\n\t\t\t\t= ENEMY =\n\t\t\t\t=========')
		pro(a)
	elif g==6 or g==12 or g==18 or g==24 or g==30:
		a='Sister'
		print('\n\t\t\t\t==========\n\t\t\t\t= SISTER =\n\t\t\t\t==========')
		pro(a)
	else:
		print('try one more time')
def pro(a):
	print('Your life made up of ',a)
	print('\n\n')
	n=input('Are you try one more time (yes/no): ')
	if(n=='yes' or n=='y'):
		flames()
	else:
		print('Have a nice day.....Thankyou...')
flames()