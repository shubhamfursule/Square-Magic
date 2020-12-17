sq_magic=[[8,11,14,1]
         ,[13,2,7,12]
         ,[3,16,9,6]
         ,[10,5,4,15]]

def square_magic(sq_matrix):
    add_up_row=sum(sq_matrix[0])
    
   #Here first check the sum for rows 
    flag= False
    for i in range(1,len(sq_matrix)):
        if add_up_row==sum(sq_matrix[i]):
            add_up_row=sum(sq_matrix[i])
            flag=True
        else:
            flag=False
            break
    #checking column and diagonal   
    if flag==True:
        list_diagonal=0     
        for i in range(0,len(sq_matrix)):
            list_colm=[]
            for j in range(0,len(sq_matrix[i])):
                list_colm.append(sq_matrix[j][i])
                if i==j:            #calculating for diagonal item
                    list_diagonal += sq_matrix[i][j]
           #checking the sum of columns
            if add_up_row==sum(list_colm):     #comparing same value and sum of columns
                add_up_row=sum(list_colm)
                flag=True
            else:
                flag=False
                break
   #Calculating second diagonal 
    list_diagonal2=0
    z=0
    for k in range(len(sq_matrix[z])-1,-1,-1):
        list_diagonal2+=sq_matrix[z][k]
        z+=1
    if flag==True and list_diagonal==add_up_row and list_diagonal2==add_up_row:
        return  True,add_up_row
    else:
        return False
    
print(f"Square magic is :{square_magic(sq_magic)} with  same value")
    