from src.classes import Handler

f = open('input1.txt', 'r')

lines = f.readlines()
handler = Handler(ttask=5, umax=10)

while not handler.completed:
    if len(lines) > 0:
        handler.handle_tick(int(lines.pop(0)))
    else:
        handler.handle_tick(None)    

print('')        
print(handler.get_total_cost())