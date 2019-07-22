from src.classes import Handler

f = open('input1.txt', 'r')
output = open('output.txt', 'w+')

lines = f.readlines()
handler = Handler(ttask=5, umax=10)

while not handler.completed:
    log = ''
    if len(lines) > 0:
        log = handler.handle_tick(int(lines.pop(0)))
    else:
        log = handler.handle_tick(None)    

    output.write(log + '\n')

output.write('\n')
output.write(handler.get_total_cost())

output.close()
f.close()