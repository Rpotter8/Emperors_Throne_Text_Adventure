#Emperor's Throne Pre-Alpha 0.0.01
#Game Core
from Entity import *
import random
from Environment import *

#Testing RunCode
objects = []
for i in range(0,10):
    generate = random.randint(0,2)
    Object = ""
    if(generate == 0):
        generate1 = random.randint(0,10)
        generate2 = random.randint(0,10)
        Object = Entity("Dragon","Enemy",generate1,generate2)
    elif(generate == 1):
        generate1 = random.randint(0,10)
        Object = Entity("Silver Key","Key",generate1,0)
    else:
        generate1 = random.randint(0,10)
        generate2 = random.randint(0,10)
        Object = Entity("Potion","Potion",generate1,generate2)
    objects.append(Object)
cEnvironment = Environment(objects,"a small room")
print(cEnvironment.toString())
