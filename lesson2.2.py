myname=input('Введите логин: ')
mypass=input('Введите пароль: ')
if(((myname=='Ivan') and (mypass=='superpassword123')) or ((myname=='Marina')
and (mypass=='marinka93'))):
    print('Привет)' + myname + '. Добро пожаловать!')
else:
    print('Ты кто такой давай, досвидания...')
