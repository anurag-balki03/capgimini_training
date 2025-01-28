def check_eligible(salary,age,credit_score):
    if(salary>=50000):
        if(age>20):
            if(credit_score>700):
                print("APPROVED... \nTHE CANDIDATE MATCHES ALL THE REQUIREMENTS.")
            else:
                print("REJECTED.... \nTHE CANDIDATE HAVE THE SALARY AND THE REQUIRED AGE BUT DOES NOT HAVE THE CREDIT SCORE.")
        else:
            print("REJECTED... \nTHE CANDIDATE HAVE THE SALARY BUT DOES NOT HAVE THE REQUIRED AGE.") 
    elif(salary<50000 and age<=20):
        print("REJECTED...\n BOTH SALARY AND AGE DOES NOT MATCH REQUIREMENT")
        
    elif(salary<50000 and credit_score<=700):
        print("REJECTED... \n BOTH SALARY AND CREDIT SCORE DOES NOT MATCH REQUIREMENT")
        
    elif(age<=20 and credit_score<=700):
        print("REJECTED... \n BOTH AGE AND CREDIT SCORE DOES NOT MATCH THE REQUIREMENT")
        
    elif(salary<50000 and age<=20 and credit_score<=700):
        print("REJECTED... \n HAVE REQUIRED AGE AND CREDIT SCORE BUT SALARY ISN'T ENOUGH") 
              
    elif(salary<50000 and age>20 and credit_score>700):
        print("REJECTED... \n does not match any of the requirements.")
        
    elif(salary>=50000 and age<=20 and credit_score>700):
        print("REJECTED... \n HAVE SALARY AND CREDIT SCORE BUT AGE ISN'T ENOUGH")
        
    elif(salary>=50000 and age>20 and credit_score<=700):
        print("REJECTED... \n HAVE SALARY AND AGE BUT CREDIT SCORE ISN'T ENOUGH")
        
    else:
        print("REJECTED... \nSALARY OF THE CANDIDATE IS NOT SUFFICIENT.")
    


salary=int(input("ENTER THE SARARY OF THE CANDIDATE: "))
age=int(input("ENTER THE AGE OF THE CANDIDATE: "))
credit_score=int(input("ENTER THE CREDIT SCORE OF THE CANDIDATE: "))
check_eligible(salary,age,credit_score)
