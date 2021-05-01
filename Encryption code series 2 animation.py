import time

'''    
Hi fishy stop watching why do you watch all day you should do something else more productive. did you know that you wasted 3 bike patches in total?? wow what a waster. You wasted 2 bike patches on fatty and 1 bike patch on "smarty" Also stop breaking super hard and making your back wheel slide on the ground. first of all, it leaves icky black marks all over the backyard, and secondly, it sill ruin your tire and make it as smooth as fatty's anyways too bad, see ya later    Message Password: catfish
7H9$69o8g$opty$d1p389r7$d8g$4t$gta$d1p38$1ww$41g$gta$o8taw4$4t$ote5p89r7$5wo5$eti5$yit4a3p9s5`$494$gta$qrtd$p81p$gta$d1op54$z$29q5$y1p385o$9r$ptp1w!!$dtd$d81p$1$d1op5i`$Yta$d1op54$l$29q5$y1p385o$tr$61ppg$1r4$k$29q5$y1p38$tr$"oe1ipg"$Awot$opty$2i51q9r7$oay5i$81i4$1r4$e1q9r7$gtai$213q$d855w$ow945$tr$p85$7itar4`$69iop$t6$1ww#$9p$w51s5o$93qg$2w13q$e1iqo$1ww$ts5i$p85$213qg1i4#$1r4$o53tr4wg#$9p$o9ww$ia9r$gtai$p9i5$1r4$e1q5$9p$1o$oettp8$1o$61ppg%o$1rgd1go$ptt$214#$o55$g1$w1p5i´osgnmjt   Password: catfish

text: bunny  password: catfish
Encrypted text: 8∑≈ƒƒ˜˛osgnmjt 

'''

def clearscreen():
    print('\n'*50)
if True:
    print('   _________'), time.sleep(0.07), clearscreen() ,print('   _________'),print('  /         \    __________'), time.sleep(0.07), clearscreen(), print('   __________'),print('  /          \    _________'),print(' /   Encrypt  \  /         \  _________'), time.sleep(0.07), clearscreen(),print('  __________    __________'),print(' /          \  /          \   __________'),print('/   Encrypt  \/   Decrypt  \ /  Privacy \  _________ '), time.sleep(0.07), clearscreen(), print('  __________    __________    __________'),print(' /          \  /          \  /  Privacy \   __________'),print('/   Encrypt  \/   Decrypt  \/   policy   \ /          \   _________'), time.sleep(0.07), clearscreen(),print('  __________    __________    __________    __________'),print(' /          \  /          \  /  Privacy \  /          \   __________'),print('/   Encrypt  \/   Decrypt  \/   policy   \/ Contact us \ /          \   _________'), time.sleep(0.07), clearscreen(),print('  __________    __________    __________    __________    __________'),print(' /          \  /          \  /  Privacy \  /          \  /          \   __________'),print('/   Encrypt  \/   Decrypt  \/   policy   \/ Contact us \/   Memory   \ /   About  \   _________ '), time.sleep(0.07), clearscreen(),print('  __________    __________    __________    __________    __________    __________'),print(' /          \  /          \  /  Privacy \  /          \  /          \  /  About   \   __________ '),print('/   Encrypt  \/   Decrypt  \/   policy   \/ Contact us \/   Memory   \/  This code \ /          \ '), time.sleep(0.07), clearscreen(),print('  __________    __________    __________    __________    __________    __________    __________'),print(' /          \  /          \  /  Privacy \  /          \  /          \  /  About   \  /          \ '),print('/   Encrypt  \/   Decrypt  \/   policy   \/ Contact us \/   Memory   \/  This code \/  Settings  \ '), time.sleep(0.07)
    time.sleep(0.07)
    input()
    clearscreen(), print('  __________    __________    __________    __________    __________    __________'),print(' /          \  /          \  /  Privacy \  /          \  /          \  /  About   \   __________ '),print('/   Encrypt  \/   Decrypt  \/   policy   \/ Contact us \/   Memory   \/  This code \ /          \ '), time.sleep(0.07), clearscreen(), print('  __________    __________    __________    __________    __________'),print(' /          \  /          \  /  Privacy \  /          \  /          \   __________'),print('/   Encrypt  \/   Decrypt  \/   policy   \/ Contact us \/   Memory   \ /   About  \   _________ '), time.sleep(0.07), clearscreen(), print('  __________    __________    __________    __________'),print(' /          \  /          \  /  Privacy \  /          \   __________'),print('/   Encrypt  \/   Decrypt  \/   policy   \/ Contact us \ /          \   _________'), time.sleep(0.07), clearscreen(), print('  __________    __________    __________'),print(' /          \  /          \  /  Privacy \   __________'),print('/   Encrypt  \/   Decrypt  \/   policy   \ /          \   _________'), time.sleep(0.07), clearscreen(),print('  __________    __________'),print(' /          \  /          \   __________'),print('/   Encrypt  \/   Decrypt  \ /  Privacy \  _________ '), time.sleep(0.07), clearscreen(),  print('   __________'),print('  /          \    _________'),print(' /   Encrypt  \  /         \  _________'), time.sleep(0.07), clearscreen(),print('   _________'),print('  /         \    __________'), time.sleep(0.07), clearscreen(),print('   _________'),print('  /         \    __________'), time.sleep(0.07), clearscreen(),print('   _________'), time.sleep(0.07), clearscreen() 
    input()
p = input('enter the phrase')
#length = len(p)
ep = input('enter e phrase')

def encryption_animation(phrase, encrypted_phrase):
    global animation_speed
    phraselength = len(phrase)
    wait_time, cut1, halfcut, cut2 , counter = (0.09 if phraselength <= 10 else (0.07 if phraselength <= 20 else (0.05 if phraselength <= 35 else (0.04 if phraselength <= 50 else (0.03 if phraselength <= 75 else (0.02)))))), 0, int(round(phraselength/2,0)), 0, 0
    while counter <= 7:
        print(phrase,'\nYour Encrypted text is being generated','.'*counter), time.sleep(0.07), clearscreen()
        counter += 1
    counter = 0
    while (cut2 + halfcut) < phraselength:
        cut2interpreter = cut2 + halfcut
        print(cut1,'   ',halfcut, cut2interpreter, cut2, phraselength)
        toprint = (encrypted_phrase[:cut1] if cut1 <= halfcut else encrypted_phrase[:halfcut])  + phrase[cut1:halfcut] + encrypted_phrase[halfcut:cut2interpreter] + phrase[cut2interpreter:phraselength]
        toprint = toprint
        print(toprint), print('Your Encrypted text is being generated','.'* round(counter)), time.sleep(wait_time), clearscreen()
        counter, cut1, cut2 = 1 if counter >= 7 else counter + 0.33, cut1 + 1 if phraselength <= 768 else (cut1 if cut1 == halfcutcut else (cut1 + 6)), cut2 + 1 if phraselength <= 768 else cut2 + 6
    counter = 0
    while counter <= 7:
        print(encrypted_phrase,'\nYour Encrypted text is being generated','.'*counter), time.sleep(0.07), clearscreen()
        counter += 1
#encryption_animation(p,ep)
def decryption_animation(phrase, encrypted_phrase):
    global animation_speed
    phraselength = len(phrase)
    wait_time, cut1, halfcut, cut2 , counter = (0.09 if phraselength <= 10 else (0.07 if phraselength <= 20 else (0.05 if phraselength <= 35 else (0.04 if phraselength <= 50 else (0.03 if phraselength <= 75 else (0.02)))))), 0, int(round(phraselength/2,0)), 0, 0
    while counter <= 7:
        print(phrase,'\nYour Decrypted text is being generated','.'*counter), time.sleep(0.07), clearscreen()
        counter += 1
    counter = 0
    while (cut2 + halfcut) < phraselength:
        cut2interpreter = cut2 + halfcut
        print(cut1,'   ',halfcut, cut2interpreter, cut2, phraselength)
        toprint = (encrypted_phrase[:cut1] if cut1 <= halfcut else encrypted_phrase[:halfcut])  + phrase[cut1:halfcut] + encrypted_phrase[halfcut:cut2interpreter] + phrase[cut2interpreter:phraselength]
        toprint = toprint
        print(toprint), print('Your Decrypted text is being generated','.'* round(counter)), time.sleep(wait_time), clearscreen()
        counter, cut1, cut2 = 1 if counter >= 7 else counter + 0.33, cut1 + 1 if phraselength <= 768 else (cut1 if cut1 == halfcutcut else (cut1 + 6)), cut2 + 1 if phraselength <= 768 else cut2 + 6
    counter = 0
    while counter <= 7:
        print(encrypted_phrase,'\nYour Decrypted text is being generated','.'*counter), time.sleep(0.07), clearscreen()
        counter += 1
encryption_animation(ep,p)