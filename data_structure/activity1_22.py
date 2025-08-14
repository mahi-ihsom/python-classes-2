#dictionary
#first create a dictionary that consists of ID, name, class, and subject integration of student
#write a program to retrive unique entities and elim the rest
st_dt={'id1' : {'name' : ['Mahi'], 'class' : ['vi'], 'subject_integration' : ['english, maths, science']},
       'id2' : {'name' : ['Gayatri'], 'class' : ['vi'], 'subject_integration' : ['english, maths, science']},
       'id3' : {'name' : ['Mahi'], 'class' : ['vi'], 'subject_integration' : ['english, maths, science']}}
mt_dt={}
for key,value in st_dt.items():
    if value not in mt_dt.values():
        mt_dt[key]=value
print(mt_dt)