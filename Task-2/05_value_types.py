values = [100,105.5,192.56j,10+6j,'10','hello world',[10,20,50,100],{'name':'sachin','age':24,'language':'python'}]
for v in values:
    print(repr(v),':',type(v).__name__)
