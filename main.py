
userinput = input("Would you like to create,read, or write a file? (c , r , w)")

if userinput == 'c':
  # I'll put this code in a try statement incase the user already has a file with this name
  try:
    name = input("What should be the name of the file ? (With the .filetype)")
    
    file = open(name,"x")
    
    print(" A file called " + name + "was created!") 
    
  except: 
    print("There was an error creating the file")
 
       
              
                  
                  
  
                  
                
    
    

    
   
