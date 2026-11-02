n1=float(input("donner la premiére note:"))
n2=float(input("donner la deuxiéme note:"))
n3=float(input("donner la troisiéme note:"))
moy=(n1+n2+n3)/3
print("la moyenne est :",moy)
if moy<10:
    
    print("Mention: Insuffisant")
elif moy <12:
    print("Mention:passable")
elif moy <14:
    
    print("Mention:Asser bien")
elif moy <16:
    print("Mention:trés bien")
else :
    
    print("Mention:trés trés bien")

         
        






