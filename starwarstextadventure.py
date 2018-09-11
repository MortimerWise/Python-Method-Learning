#made for a quick Star Wars themed game jam event.
#Code is ugly, but functional, designed to work as opposed to look nice.

#initial start up

print '''
   .           .        .                     .        .            .
             .               .    .          .              .   .         .
               _________________      ____         __________
 .       .    /                 |    /    \    .  |          `
     .       /    ______   _____| . /      \      |    ___    |     .     .
             \    \    |   |       /   /\   \     |   |___>   |
           .  \    \   |   |      /   /__\   \  . |         _/               .
 .     ________>    |  |   | .   /            \   |   |\    \_______    .
      |            /   |   |    /    ______    \  |   | \           |
      |___________/    |___|   /____/      \____\ |___|  \__________|    .
  .     ____    __  . _____   ____      .  __________   .  _________
       \    \  /  \  /    /  /    \       |          \    /         |      .
        \    \/    \/    /  /      \      |    ___    |  /    ______|  .
         \              /  /   /\   \ .   |   |___>   |  \    `
   .      \            /  /   /__\   \    |         _/.   \    \            +
           \    /\    /  /            \   |   |\    \______>    |   .
            \  /  \  /  /    ______    \  |   | \              /          .
 .       .   \/    \/  /____/      \____\ |___|  \____________/  
                               .                                        .
     .                                           .
                .                                   .            .
'''

image_0= '''
                                     _____
                                   .'/L|__`.
                                  / =[_]O|`|
                                  "+_____":|
                                __:='|____`-:__
                               |[] ||====| []||
                               ||[] | |=| | []||
                               |:||_|=|U| |_||:|
                               |:|||]_=_ =[_||:| 
                               | |||] [_][]C|| |
                               | ||-'"""""`-|| |
                               /|\\_\_|_|_/_//\_|
                              |___|   /|\   |___|   
                              `---'  |___|  `---'       
                                     `---'
                                Droid Detective 
         '''
print (image_0)

print "\nA deep hum vibrates through your body,\nyour senses slowly come online,\nyou are a droid."
print "\nPowering up you push through the rubble which covers you.\nAround you lay parts of other droids, damaged and destroyed.\n" 

# Error message

def Error():
    print "\nError, unknown command..."

# fail scan

def scan1():
    print "\nScannig area... nothing found"

# good scan

def scan2():
    print "\nObject of interest detected..."

#computer terminal.

def comp1():
    
        print "\n You move to the computer terminal and access the system. The only actie file is a diary"
        print "what to do"
        print "1. Read the last entry"
        print "2. Log off"

        choice = raw_input(">>>")
        
        if choice == "Read the last entry" or choice == "1":
            print '''\nYou open the file, it reads as follows.

"Simmons personal log.

The client was pleased with the payment and we didn't ask any questions.

Had another row with Ren, he forgot the password for the reactor room again,
decied to name it after his dog, yes I know, it's weak, but that idiot can't even find his way out of a tar pit let alone a password system"

Entry ends

you shut down the computer.'''
            room2()
        elif choice == "Log off" or choice == "2":
            print "You shut down the computer."
            room2()
        else: Error() + comp1()
       
#Main introduction & First choice
def intro():
    print "\nWhat do you do? Enter instructions as keypad number or type exactly as shown."
    print "\n1. Dance"
    print "2. Access memory files"

    choice = raw_input(">>>")

    if choice == "Dance" or choice == "1":
        print "\nYou start to dance, who knew droids had such moves?"
        intro()
    elif choice == "Access memory files" or choice == "2":
        print "\nAcessing memory files, please wait... ... \n\n... .\n ... ... \n...\n"
        memory()
    else: Error() + intro()

#2nd choice memory files        
def memory():
    print '''
Your memory is restored, but pieces of it are missing, the last record file is still active.

What do you do?"'''
    
    print "\n1. Play file."
    print "2. Do nothing"

    choice = raw_input(">>>")

    if choice == "Play File" or choice == "1":
        print '''
Acessing memory files, please wait... ... ... .
... ...

You play the file, it is an audio message the message is full of static.

in the static, the sounds of a blaster firing
the cries of screaming and exploding droids can be heard.
a voice can be heard after the carnage,
"the data is not present my lord."'''
        message()
        
    elif choice == "Do nothing" or choice == "2":
        print "\nThe force is not strong with this one..."
        memory()
    else: Error() + memory()

#3rd choice meessage

def message():

    print '''\n
It seems that your fellow droids met a terrible end.
Before you can act, you detect an incomming message from the Jedi Council,
it's addressed to one of the destroyed droids.'''

    print"\nwhat will you do?"
    print"\n1. Tap into the transmission."
    print"2. Try to open the airlock."

    choice = raw_input(">>>")

    if choice == "Tap into the transmission." or choice == "1":
        print '''\nYou tap into the transmission, transmission reads...

                                   ____                  
                                _.' :  `._               
                            .-.'`.  ;   .'`.-.           
                   __      / : ___\ ;  /___ ; `      __  
                 ,'_ ""--.:__;".-.";: :".-.":__;.--"" _`,
                 :' `.t""--.. '<@.`;_  ',@>` ..--""j.' `;
                      `:-.._J '-.-'L__ `-- ' L_..-;'     
                        "-.__ ;  .-"  "-.  : __.-"       
                            L ' /.------.\ ' J           
                             "-.   "--"   .-"            
                              .l"-:___;-";.           

"Sith Assassin detected on ship has, to Deck 18, retrieve data core you must.
Coruscant with data core, return you must."

It looks like your droid palls were murdered.'''
    elif choice == "Try to open the airlock." or choice == "2":
        print '''\nYou struggle for a while, suddenly the airlock explodes out.
you blast into the vaccum of space... for years to come explorers will
tell ghost stories about a phantom flying droid'''
        message()
    else: Error() + message()

    print '''\nConsidering options you perform a situation analysis.
Your droid mind takes in all the variables and comes to the following conclusion.

        "Attempt to find the droid killer & recover the data core"'''
    room1()

#1st room.

def room1():
    print "\nYou are in a room full of destroyed droids, there are no clues here."
    print "You can only go north"
    print "\nWhat do you want to do?"
    print "\n1. Whistle"
    print "2. Read a book"
    print "3. Go North"
    
    choice = raw_input(">>>")

    if choice == "Whistle" or choice == "1":
        print "\nYou whistle loudly. If anyone was listening they'd think you were happy"
        room1()
    elif choice == "Read a book" or choice == "2":
        print '''\nYou pick a book at random from your media library, it's a detective novel.
how appropriate.
You now consider yourself fully qualified to solve crimes'''
        room1()
    elif choice == "Go North" or choice == "3":
        print "You head north"
    else: Error() + room1()

    print "\nYou exit through a large door into a new room."

    print ''' \n\n
                             |`:.
                             |  `:.
                             | |`.`:;@.
                             | |;.`.`;|
                             ; `.';| ||
                            ,(`;.`.| ||
                           /8o (`:.  ||
                         /o8888o  `; ||
                       /@o8888888o (`;|
                      (`.()oO888888o (<
                       `.`.;:oO08c{)/ |
                         `.`.(),0 /  /
                           `.`.`/  /
                             `.( /'''
    room2()
    
# 2nd room    
def room2():

    print "\nThe room is a small space, full of consoles and computer systems. to the west is a door, to the north is a window to another room"
    print "\nWhat do you want to do?"
    print "1. Scan room"
    print "2. Go west (This option will terminate the game)."
    print "3. Look through window"
    print "4. Access computer system"
   
    choice = raw_input(">>>")
    
    if choice == "Scan room" or choice == "1":
        scan2() + room2()
    elif choice == "Go west" or choice == "2":
        print "\nYou exit west into a new room"
        room3()
    elif choice == "Look through window" or choice == "3":
        print '''\nYou move slowly towards the window, the next room is dark.
However, you can just make out the faint outline of a severely damaged droid
Looking closer you can just make out a potrait of a dog with the name "MAX" printed under it'''
        room2()
    elif choice == "Access computer System" or choice == "4":
        comp1() 

    else: Error() + room2()   

# I think this is where the main program is...?
intro()     
