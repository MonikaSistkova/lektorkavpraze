import random
while True:
    noun = ("já", "ty", "on", "ona", "my","vy", "oni","Jane","John", "můj strýc", "tvoje teta","jeho táta","naše máma", "jeho bratr", "její sestra", " moji přátelé", "studenti", "ženy", " muži","vaše učitelka","její kamarád")
    verb = ("být tady", "čistit zuby"," plavat v moři", "platit v restauraci", "prodat auto","stavět dům","pít kafe", "jet na dovolenou", "mít nové auto", "vařit večeři","dělat domácí úkol","jít do školy","psát jí", "přijít", "dívat se na TV", "vstávat", "číst knížku", " psát email","poslat dopis", "volat domů")
    mood = ("?", "+","-")
    tense = ("present simple","present continous", "past simple")
    noun = random.choice(noun)
    verb = random.choice(verb)
    mood = random.choice(mood)
    tense = random.choice(tense)
    # byt tady a mit nove auto nemuze mit present continous.
    if verb == "být tady" or verb == "mít nové auto":
        print('{}\ {}\ {}\ present simple'.format(noun,verb,mood))
        clovek = (input(""))
        if clovek == 'end':
            print('Děkujeme za použití programu.')
            break
    else:
        print('{}\ {}\ {}\{}'.format(noun,verb,mood,tense))
        clovek = (input(""))
        if clovek == 'end':
            print('Děkujeme za použití programu.')
            break
        else:
            continue
