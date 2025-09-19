x,y=0,0
goal=(2,0)
a=4
b=3
while True:
  print(x,y)
  if(x,y)==goal:
    print(x,y)
    break
  elif x==0:
    x=a
  elif y==b:
    y=0
  else
  pour=min(x,b-y)
  x-=pour
  y+=pour
