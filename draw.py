from turtle import * 
color('red','blue')
begin_fill()
while True:
    forward(200)
    left(100)
    if abs(pos())<1:
        break 
end_fill()
done()
print("draw")
print("program started")
print("i wrote a second line")