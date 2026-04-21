print("Welcome to maze escape game, your gole is to move K to reach the exit A")
print("use U for Up , L for Left , D for Down ,R for Right")
print()

maze = [ ["#","#","#","#","#"],
         ["#","K"," "," ","#"],
         ["#","#","#"," ","#"],
         ["#","#","#"," ","#"],
         ["#","#","#","A","#"],
         ]


row = 1
col = 1
#==============================================================================================
while True:
    for i in maze:
        print("   ".join(i))
        
        move= input("enter your move (U,D,R,L): ")
        new_row = row
        new_col = col  
            
        if move == "U":
            new_row -= 1
        elif move == "D":
            new_row += 1
        elif move == "L":
            new_col -= 1
        elif move == "R":
            new_col += 1
        else:
            print("try again")
            
        if maze[new_row][new_col] != "#":
             maze[row][col] = " "
             row = new_row
             col = new_col
             
        
        if maze[new_row][new_col] == "#":
            print("you hit the wall, try again")
        ##  maze[new_row][new_col] = "#"
                
        if maze[new_row][new_col] == "A":
            print("you Win, Congratulations")
            break
        
        
        maze[new_row][new_col] = "K"
        print("   ".join(i))
                
        
        
        
        
        
        
        
        
        
        
          

