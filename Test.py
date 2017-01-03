name = input("What's your name? ")
name = name.title()
feeling = input ("Hello " + name + ", how are you? ")
feeling = feeling.lower()

understand = False

while (understand == False):
    confirm = input ("So you're feeling " + feeling + "?")  
    confirm = confirm.upper()

    if (confirm == 'YES'):
        print ("I wish I could feel... ")
        understand = True
    
    else:
        print ("I must have misheard you")
        feeling = input ("Remind how you are feeling please ")
        
    
