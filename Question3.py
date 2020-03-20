text = open("New Text Document.txt", "r") 
  
display = dict() 
  
for i in text: 
    i = i.strip() 
  
    i = i.lower() 
  
    words = i.split(" ") 
  
    for word in words: 
        if word in display: 
            display[word] = display[word] + 1
        else: 
            
            display[word] = 1
  
 
for key in list(display.keys()): 
    print(key, ":", display[key]) 