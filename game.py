from time import sleep
import random
import string
sample=[{"SHERSHAH":["_","_","E","_","_","_","A","_"]},
        {"DOCTOR G":["_","O","_","_","O","_"," ","_"]},
        {"DANGAL":["_","A","_","_","A","_"]},
        {"JAB WE MET":["_","A","_"," ","_","E"," ","_","E","_"]},
        {"SHOLAY":["_","_","O","_","A","_"]},
        {"TAMASHA":["_","A","_","A","_","_","A"]},
        {"SULTAN":["_","U","_","_","A","_"]},
        {"LOOTERA":["_","O","O","_","E","_","A"]},
        {"COCKTAIL":["_","O","_","_","_","A","I","_"]},
        {"VICKY DONOR":["_","I","_","_","_"," ","_","O","_","O","_"]},
        {"PAD MAN":["_","A","_"," ","_","A","_"]},
        {"RAW":["_","A","_"]},
        {"KICK":["_","I","_","_"]},
        {"ANTIM":["A","_","_","I","_"]},
        {"JAI HO":["_","A","I"," ","_","O"]},
        {"READY":["_","E","A","_","_"]},
        {"HERO":["_","E","_","O"]},
        {"GARV":["_","A","_","_"]},
        {"LAGAAN":["_","A","_","A","A","_"]},
        {"CHALTE CHALTE":["_","_","A","_","_","E"," ","_","_","A","_","_","E"]},
        {"DHADKAN":["_","_","A","_","_","A","_"]},
        {"GULLY BOY":["_","U","_","_","_"," ","_","O","_"]},
        {"KOI MIL GAYA":["_","O","I"," ","_","I","_"," ","_","A","_","A"]},
        {"KABIR SINGH":["_","A","_","I","_"," ","_","I","_","_","_"]},
        {"BAGHBAN":["_","A","_","_","_","A","_"]},
        {"BAJIRAO MASTANI":["_","A","_","I","_","A","O"," ","_","A","_","_","A","_","I"]},
        {"VEER":["_","E","E","_"]},
        {"HUM SAATH SAATH HAIN":["_","U","_"," ","_","A","A","_","_"," ","_","A","A","_","_"," ","_","A","I","_"]},
        {"DILWALE":["_","I","_","_","A","_","E"]},
        {"RAJA HINDUSTANI":["_","A","_","A"," ","_","I","_","_","U","_","_","A","_","I"]},
        {"WAR":["_","A","_"]},
        {"HUM DIL DE CHUKE SANAM":["_","U","_"," ","_","I","_"," ","_","E"," ","_","_","U","_","E"," ","_","A","_","A","_"]},
        {"HUM AAPKE HAI KOUN":["_","U","_"," ","A","A","_","_","E"," ","_","A","I"," ","_","O","U","_"]},
        {"RAEES":["_","A","E","E","_"]},
        {"DIL TO PAGAL HAI":["_","I","_"," ","_","O"," ","_","A","_","A","_"," ","_","A","I"]},
        {"TIGER ZINDA HAI":["_","I","_","E","_"," ","_","I","_","_","A"," ","_","A","I"]},
        {"CHHICHHORE":["_","_","_","I","_","_","_","O","_","E"]},
        {"LAAL SINGH CHADDHA":["_","A","A","_"," ","_","I","_","_","_"," ","_","_","A","_","_","_","A"]},
        {"DILJALE":["_","I","_","_","A","_","E"]},
        {"SANAM TERI KASAM":["_","A","_","A","_"," ","_","E","_","I"," ","_","A","_","A","_"]},
        {"RAM SETU":["_","A","_"," ","_","E","_","U"]},
        {"AE DIL HAI MUSHKIL":["A","E"," ","_","I","_"," ","_","A","I"," ","_","U","_","_","_","I","_"]},
        {"SOORYAVANSHI":["_","O","O","_","_","A","_","A","_","_","_","I"]},
        {"BADHAAI HO":["_","A","_","_","A","A","I"," ","_","O"]},
        {"PREM RATAN DHAN PAYO":["_","_","E","_"," ","_","A","_","A","_"," ","_","_","A","_"," ","_","A","_","O"]},
        {"DANGAL":["_","A","_","_","A","_"]},
        {"LOVE AAJ KAL":["_","O","_","E"," ","A",'A',"_"," ","_","A","_"]},
        {"DRISHYAM":["_","_","I","_","_","_","A","_"]},
        {"HALF GIRLFRIEND":["_","A","_","_"," ","_","I","_","_","_","_","I","E","_"]}]
songs=[{"The heart wants that the bright days never ever pass, the heart wantsthat we should never be without friends.":["1 dil diyan gallan","2 Aae dil hai mushkil","3 dil to pagal hai","2 ae dil hai mushkil"]},
       {"Sun came out,some mercury had melted,there was a storm,when my heart sighed":["1 dil se re","2 dilwale","3 dil chahta hai" ,"3 dil chahta hai"]},
       {"This boy is crazy ,O Allah,how difficult it is to explain to him,that slowly the heart becomes desperate , that is love ":["1 ladka bada anjana hai","2 yeh ladka hai allah","3 ladki pagal hai","2 yeh ladka hai allah"]},
       {"We will not break this friendship we will die but never leave each other's side":["1 dost dost na raha","2 yeh dosti hum nahi todenge","3 pyaar ke pal","2 yeh dosti hum nahi todenge"]},
       {"In the moon,hid the cloud,blush and come hid in my arms":["1 chand wala mukhda","2 chand ke pyaar chalo","3 chaand chupa badal mei","3 chaad chupa badal mei"]},
       {"When i saw a girl,it felt like a blooming rose,like a poet's dream,like a bright ray,like a deer in a bun,like a moonlit night":["1 ladki badi anjaani hai","2 ye ladki pagal hai","3 ek ladki ko dekha","3 ek ladki ko dekha"]},
       {"You are my journey ,you are my destination,living without you,o heart is difficult":["1 ae dil hai mushkil","2 aati kya khandala","3 ae mere humsafar","1 ae dil hai mushkil"]},{"the birds of dreams fly in open skies.the birds of dream fly in the world of my heart":["1 khaabon ke parinday","2 Teri Daastan","3 pyar ke pal","1 khaabon ke parinday"]},
       {"Those dark dark eyes,those fair fair cheeks,these spicy spicy looks,that walk just like a dear.":["1 kala chashma","2 ye kaali kaali aankhen","3 ae mera humsafar","2 ye kaali kaali aankhen"]},
       {"The lord also plays games,every day he puts up carnival,says that nothing has changed,lies all the time.":["1 mehrama","2 sham","3 ranjha","3 ranjha"]},
       {"These threads of attachement have got entangled in your fingers,i seem to have no clue how to solve this knot":["1 dheemi dheemi","2 yeh moh moh ke dhaage","3 piya bina piya bina","2 yeh moh moh ke dhaage"]},
       {"Say sweet sweet things,mix syrup into my ears,let the drums beat,and you always sway with fun":["1 sajan tumse pyar","2 gud naal","3 gal mitthi mitthi","3 gal mitthi mitthi"]},
       {"You,without teeling me,take me somewhere,where you smile,that itself is my destination":["1 tu bin bataye","2 dum dum diga diga","3 lo chali main","1 tu bin bataye"]},
       {"When a dream shatters in an instant,the whole world seems lonely,the whole world seems lonely":["1 jag soona soona lage","2 akela","3 mauja hi mauja","1 jag soona soona lage"]},
       {"I have stolen you from lines of my destiny,we have met you by great luck,i have stolen you from lines of my destiny":["1 laila mai laila","2 chura ke dil mera","3 mile ho tum humko","3 mile ho tum humko"]},
       {"You move like the wind i fly like sand,who will love you like this like i do":["1 dilbar","2 kaun tujhe","3 ae mera humsafar","2 kaun tujhe"]},
       {"The heart is crazy,the heart is crazy,first time mixing this rekindles fire in the chest":["1 dil diyaan galan","2 dhadkan","3 dil to pagal hai","3 dil to pagal hai"]},
       {"Steal us from us ,only hide it somewhere in your heart, steal us from us only hide it somewhere in your heart":["1 saas","2 hum ko humi se chura lo","3 dil toh pagal hai","2 hum ko humi se chura lo"]},
       {"The fairy lady walks away after stealing my heart":["1 chura ke dil mera","2 chori chori jab nazre mili","3 kal hoo na hoo","1 chura ke dil mera"]},
       {"Should i tell you or should i stay quiet about what's in my heart":["1 tune jo na kahan","2 zindagi ke yahi raat hai","3 keh doon tumhein","3 keh doon tumhein"]}]
names=["Payal","Rakesh","Sonam","Prem","Naina","Gabbar","Pooh","Suman","Simran","Raj","Kiran","Aman","Varun","Shivansh","Tanmay"]
movies=["ae dil hai mushkil","aa ab laut chalen","aa dekhen zara","aankhen","aam danni athani kharcha rupiya","aarakshan","aladin","aetbaar","armaan","agneepath","ardaas","ae gaye munda uk de","aashiqui not allowed","aashiqui","aaja mexico challiye","baghban","bhoothnath returns","bduddah hoga terra baap","baabul","bade miyan chote miyan","brahmastra","baadshah","baazigar","baaz","bhaji in problem","best of luck","buraah","chalo ishq ladaaye","chamatkar","chak de india","cirkus","company","chehre","chhichhore","carry on jatta","chori chori chupke chupke","control bhaji control","dhadkan","dilwale","diljale","dabangg","dil ne jise apna","dilwale dulhania le jayenge","don","dil to pagal hai","devdas","deewana","dhoom","dear zindagi","disco singh","desi munde","dil diya gallan","ek main ek tum","ek deewana tha","ek tha tiger","eklavya","ek rishtaa:the bond of love","ek villian","ek hi raaasta","everything is fine","ek jind ek jaan","farz","fateh","ghayal once again","gadar:ek prem katha","godfather","garv:pride and honour","golmaal","golmaal:fun unlimited","gangubai kathiawadi","gangaajal","gundaraj","gulabo sitabo","god tussi great ho","guddiyan patole","hum saath saath hain","hum aapke hain koun","hulchul","hungama","hum dil de chuke sanam","himmatwala","hero","hum tumhare hain sanam","har dil jo pyar karega","happy new year","heer ranjha","ishq","identity card","imtihaan","iilzaam","impatient vivek","indra the tiger","jawan","jab tak hain jaan","jab harry met sejal","jab we met","jhoom barabar jhoom","jaan","jigar","jung","jo bole so nihaal","jeet","jaal the trap","jinde meriye","jind mahi","jatt brothers","jatt and juliet","koyla","kal ho naa ho","kuch kuch hota hai","kabhi khushi kabhie gham","kabhi alvida naa kehna","kachche dhaage","kaal","karan arjun","karz:the burden of truth","kirpaan","kabaddi once again","loafer","lagaan","laal rang","laal singh chaddha","laali ki shaadi mein laaddo deewana","london dreams","lucku:no time for love","lakshya","lucky di unlucky story","lakeer","malang","mubarakan","mashaal","meri jung","my name is khan","mohabbatein","main hoo na","maidaan","mujhse shaadi karogi","mujhse dosti karogi","mr and mrs.khanna","maine pyaar kyun kiya","mohra","mission mangal","nayak the real hero","nakkash","namaste london","nanu ki janu","nastik","nassrbaaz","naajayaz","no entry","no problem","nishabd","nikka zaildar","o my god","ok jaanu","ok mein dhokhe","oh my pyo ji","padman","pagalpanti","paani","paathshaala","prem ratan dhan payo","phir hera pheri","phool aur kaante","pyaar to hona hi tha","pink","piku","pk","paheli","qala","qissa","qaidi band","qayamat","qismat","qayamat se qayamat tak","raakh","raaste","raavan","raanjhanaa","raat gayi baat gayi","rowdy rathore","rowdy boys","raees","runway 34","rann","race 3","rab ne bana di jodi","raid","saanjh","singh vs kaur","singham","singham returns","simmba","sholay","sooryavanshi","street dance 3d","sita ranam","swadesh","swarg","sooryavansham","son of sardar","singh is king","singh is bling","suhaag","taish","taj mahal","talvar","takkar","talaash","tanhaji","tiger zinda hai","total dhamaal","teen","udta punjab","udaan","vijaypath","vishwatma","veere de weeding","veer-zaara","veerana","victory","vikram vedha","vijay","vicky donor","veele","wanted","war","warning","weeding anniversery","wazir","wake up sid","what the jatt","welcome to punjab","yeh raaste hai pyaar ke","yahaan","yaar anmulle","yaariyan","yaara","yaar anmulle returns","yamla pagla deewana","yes i am a student","yamla pagla deewana 2","yeh mera india","yakeen","yahaan sabki lagi hai","zaalim","zakhm","zameen","zakhmi rooh","zakhmi dil","zalzala","zameer","zameen aasmaan","zakhmi","zinda bhaag"]
print("\033[1;35mWELCOME TO TEEN TIGADA KAAM BIGADA  ".center(120))
print("\033[1;31mTHE ULTIMATE BOLLYWOOD QUIZ FOR CRAZY BOLLYWOOD FANS  ".center(120))
sleep(3)
print("\033[1;34mSO LET'S GET STARTED".center(120))
sleep(2)
name=input("\033[1;34mENTER YOUR NAME\nBUT HERE'S A TWIST DON'T WRITE YOUR ACTUAL NAME\nPICK ANY OF YOUR FAVOURITE CHARACTER FROM ANY BOLLYWOOD MOVIE AND THAT IS GOING TO BE YOUR NAME FOR THE REST OF THE GAME \nSO WHOM YOU HAVE DECIDED TO BE TODAY ")
print("\033[1;33mHEY {}, ITS A PLEASURE MEETING YOU".format(name.upper()))
print("\033[1;31mSO {} CHOOSE YOUR GAME \nPRESS 1 IF YOU WANT TO PLAY THE BOOLYWOOD MANIA \nPRESS 2 IF YOU WANT TO PLAY MUSICAL QUIZ \nPRESS 3 IF YOU WANT TO PLAY BOLLYWOOD BINGO".format(name.upper()))
game=int(input("\033[1;34mSO WHAT DO YOU WANT TO PLAY "))
if game==1:
    points=0
    chances=5
    while chances>0:
        for ele in random.choices(sample) :
            for i,j in ele.items():
                s=j.count("_")
                print("\033[1;35m SO GUESS THIS MOVIE RIGHT , ALL THE BEST !!!")
            li=[]
            li=j
        for k in range(s+6):
            string=""
            for ele in li:
                string=string+" "+ele
            print("\033[1;35m  {} \n".format(string).center(120," ")) 
            a=input().upper()
            l,cnt=0,0
            for  p in range (len(j)) :
                if a==i[p]:
                    if j[p]=="_":
                        li[p]=a
                        l=l+1
                    else:
                        cnt=cnt+1
            if l==0:
                if s+6-k-1>1 :
                    print("\033[1;31mOOPS!!! This is a wrong guess :( \nBut no worries you still have {} chances left \n".format(s+6-k-1))
                elif s+6-k-1==1:
                    print("\033[1;31mOOPS!!! This is a wrong guess :( \nBut no worries you still have {} chance left \n".format(1))
            else:
                print("\033[1;34m GOOD GOING CHAMP!!! That was a correct guess ")
            if s+6-k-1==3:
                if j.count("_")>3:
                    for t in range(len(j)):
                        if j[t]=="_":
                            j[t]=i[t]
                            break
                    print("\033[1;36mYou seems a little bit lost, well take this hint,\nBut now churn your thoughts real quick because its 3 more chances only ")       
            if cnt>0:
                print("\033[1;35mCheck out its already present, you have wasted a chance ")
            if a=="A" or a=="E"or a=="I" or a=="O" or a=="U":
                print("\033[1;35mC'mon its a vowel , if it was in the movie we would have already given , why are you wasting a chance ")
                    
            if k==s+5:
                if i !=("".join(str(ele) for ele in j)):
                    print("\033[1;33mOH NOOO!!! You ran out of chances , well maybe its just not your day\nBETTER LUCK NEXT TIME :)  ")
                    print("\033[1;36mWell your final answer was {} which is not correct ".format("".join(str(ele) for ele in j)))
                    print("\033[1;33mThe correct answer was {} ".format(i))
                    chances=chances-1
                    if chances>1:
                        print("\033[1;36mWell now gear up for the next one now \nbut you are now left with {} lives only ".format(chances))
                    elif chances==1:
                        print("\033[1;36mThis is your last life, guess correctly ")
            if i ==("".join(str(ele) for ele in j)):
                print("\033[1;32mYes the correct movie was {} ".format(i))
                points=points+10
                print("\033[1;32mGREAT!!! You have successfully guessed the correct movie,\nWELL DONE!!! Its time to move to the next one now :)  ")
                break            
            if chances==0:
                print("\033[1;36mOh No!!! You ran out of 5 lives \nWe are so sorry for you")          
    print("\033[1;32mYou have score a total score of {} points".format(points))
elif game==2:
    print("\033[1;35mHi {} ".format(name.upper()))
    print("\033[1;33mThis game will present some boolywood songs translated in English \nYou have to guess the songs correctly")
    print("\033[1;36mThe lyrics of a bollywood song will be displayed on the screen \nYou will be given 3 options out of which one is correct \nYou have to enter the number written in front of the option and submit your answer ")
    sleep(5)
    n=1
    points=0
    while n>0:
        for ele in random.choices(songs):
            for i,j in ele.items():
                print("\033[1;32m {} ".format(i))
                for i in range(len(j)-1):
                    print("\033[1;39m {} ".format(j[i]))
            a=int(input())
            if j[a-1]==j[-1]:
                print("\033[1;35mYes!!!It's a coorrect answer,Good going :) ")
                points=points+10
            
            else:
                print("\033[1;31mNo Its not a correct answer :(\nBut keep trying ")
                print("\033[1;36mThe correct answer was {} ".format(j[-1]))
            print("\033[1;33mIf you want to exit the game , press 5 ")
            print("\033[1;31mIf you want to continue with the game , press 6")
        tell=int(input())
        if tell==5:
            print("\033[1;36mThe final points are {} ".format(points))
            break
        else:
            pass
        
elif game==3:
    print("\033[1;35mHi {} , How are you ".format(name.upper()))
    p=random.choices(names)
    strings=""
    for ele in p:
        strings=strings+ele
    print("\033[1;34mThis is {} \nAnd I am going to play this  game with you \nSo are you ready to have a tough battle with me".format(strings))
    sleep(2)
    print("\033[1;31mSo this game is basically based on your knowledge of movies\nAn alphabet will be given to you and you have to think of a movie with that alphabet")
    sleep(4)
    print("\033[1;32mThen return the last alphabet of the movie you thought and i will give the movie for that alphabet \nThen think of a next movie with the last alphabet of the movie i return")
    sleep(4)
    wer=random.choice(string.ascii_letters)
    wer=wer.lower()
    print("\033[1;36mSo let's start the game, So start with the alphabet \n{} ".format(wer))
    print("\033[1;33mIf you dont know the answer press 7\nOr press 9 if you know the answer ")
    start=int(input())
    if start==7:
            random.shuffle(movies)
            b= [x for x in movies if x.startswith(wer)]
            if len(b)==0:
                print("\033[1;36mI dont think many movies start with that alphabet, lets change the alphabet")
                su=random.choice(string.ascii_letters)
                print("\033[1;36mSo the alphabet  is \n{} ".format(su))
                b= [x for x in movies if x.startswith(su)]                
            num=random.randrange(0,len(b))
            c=b[num]
            mv=""
            for ele in c:
                mv=mv+ele 
            print("\033[1;31mSo my answer to this alphabet would be \n{} ".format(mv))
            print("\033[1;35mNow you tell a movie name with \n{} alphabet".format(mv[-1]))
    else:
        pass
    loop=1
    while loop>0:
        sleep(4)
        a=input("\033[1;34mSo tell me which is the last alphabet of your movie \nI am ready to answer with a movie\n")
        random.shuffle(movies)
        a=a.lower()
        b= [x for x in movies if x.startswith(a)]
        if len(b)==0:
            print("\033[1;36mI dont think many movies start with that alphabet, lets change the alphabet")
            su=random.choice(string.ascii_letters)
            print("\033[1;36mSo the alphabet  is \n{} ".format(su))
            b= [x for x in movies if x.startswith(su)]                
        num=random.randrange(0,len(b))
        c=b[num]
        mv=""
        for ele in c:
            mv=mv+ele 
        print("\033[1;31mSo my answer to this alphabet would be \n{} ".format(mv))
        print("\033[1;35mNow you tell a movie name with \n{} alphabet".format(mv[-1]))
        print("\033[1;33mIf you dont know the answer , press 7")
        print("\033[1;33mIf you want to exit the game , press 8 ")
        print("\033[1;31mIf you want to continue with the game , press 9")
        exit=int(input())
        if exit==8:
            break
        elif exit==7:
            random.shuffle(movies)
            b= [x for x in movies if x.startswith(mv[-1])]
            if len(b)==0:
                print("\033[1;36mI dont think many movies start with that alphabet, lets change the alphabet")
                su=random.choice(string.ascii_letters)
                print("\033[1;36mSo the alphabet  is \n{} ".format(su))
                b= [x for x in movies if x.startswith(su)]                
    
            num=random.randrange(0,len(b))
            c=b[num]
            mv=""
            for ele in c:
                mv=mv+ele 
            print("\033[1;31mSo my answer to this alphabet would be \n{} ".format(mv))
            print("\033[1;35mNow you tell a movie name with \n{} alphabet".format(mv[-1])) 
        elif exit==9:
            continue
