jaut = input('Ievadīt tekstu jā vai nē:')
fails=open('teksts.txt', 'a+', encoding='utf-8')
if jaut == 'jā' or jaut == 'Jā':
    teksts=input('Ievadi tekstu:')
    fails.write(teksts)
    fails=open('teksts.txt', 'r', encoding='utf-8')
    print(fails.read())
else:
    print('Programma beidz darbu!')

fails.close()




