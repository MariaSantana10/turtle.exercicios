############ questao 1

# import turtle

# turtle = turtle.Turtle()
# turtle.shape('turtle')

#main code 
'''turtle.forward(100)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.forward(100)
turtle.left(90)'''

#1) reduzir as duas linhas com forward
'''for x in range (4):
    turtle.forward(200)
    turtle.left(90)'''

#2) virar para direita
'''for x in range (4):
    turtle.forward(200)
    turtle.right(90)'''

#3)
'''for x in range (4):
    turtle.forward(300)
    turtle.right(90)'''

#4) 
# for x in range (2):
#     turtle.forward(90)
#     turtle.left(90)
#     turtle.forward(200)
#     turtle.left(90)





############ questao 2





# import turtle
# turtle = turtle.Turtle()

#main code
'''turtle.color('red')
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)'''

#1) mudar a cor da tartaruga
'''turtle.color('pink')
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)'''

#2) mudar o formato da tartaruga
'''turtle.color('pink')
turtle.shape('arrow')
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)'''

#3) mudar o tamanho do quadrado
# 





################ questao 3






# import turtle
# turtle = turtle.Turtle()

#main code
'''turtle.pensize(5)
for color in ['blue', 'black', 'red', 'pink']:
    turtle.color(color)
    turtle.forward(100)
    turtle.right(90)'''


#1) mude a forma da tartaruga
# turtle.shape('circle')
# for color in ['blue', 'black', 'red', 'pink']:
#     turtle.color(color)
#     turtle.forward(100)
#     turtle.right(90)

#2) mudar a ordem das cores
# turtle.shape('circle')
# for color in ['black', 'red', 'pink', 'blue']:
#     turtle.color(color)
#     turtle.forward(100)
#     turtle.right(90)

#3) mudar a largura da linha
# turtle.shape('circle')
# for color in ['black', 'red', 'pink', 'blue']:
#     turtle.color(color)
#     turtle.forward(60)
#     turtle.right(90)

#4) desenhar dois quadrados
# turtle.shape('circle')
# for color in ['black', 'red', 'pink', 'blue']:
#     turtle.color(color)
#     turtle.forward(100)
#     turtle.right(90)

# turtle.up()
# turtle.forward(300)
# turtle.down()
# turtle.right(90)

# for color in ['black', 'red', 'pink', 'blue']:
#     turtle.color(color)
#     turtle.forward(100)
#     turtle.right(90)






######### questao 4






# import turtle
# import random
# turtle = turtle.Turtle()

#main code
'''colors = ['red', 'purple', 'blue']

for _ in [1, 2, 3]:
    color = random.choice(colors)
    turtle.color(color)
    turtle.forward(100)
    turtle.right(120)'''

#1) acrescentar duas cores a mais
'''colors = ['red', 'purple', 'blue', 'pink', 'yellow', 'lightsteelblue'] #as cores 'pink','yellow', e 'lightsteelblue' foram add

for _ in [1, 2, 3, 4, 5, 6]:
    color = random.choice(colors)
    turtle.color(color)
    turtle.forward(100)
    turtle.right(120)'''

#2) triangulo apontar para cima
# colors = ['red', 'purple', 'blue']
# for _ in [1, 2, 3]:
#     color = random.choice(colors)
#     turtle.color(color)
#     turtle.forward(100)
#     turtle.right(240)

#3) remover a cor vermelha
'''colors = ['purple', 'blue']
for _ in [1, 2, 3]: #msm sem a vermelha precisa ter o 3 ali 
    color = random.choice(colors)
    turtle.color(color)
    turtle.forward(100)
    turtle.right(120)'''

#4) mudar a largura da linha
'''colors = ['red', 'purple', 'blue']
for _ in [1, 2, 3]:
    color = random.choice(colors)
    turtle.color(color)
    turtle.forward(200)
    turtle.right(120)'''






########## questao 5






# import turtle
# import random
# turtle = turtle.Turtle()

#main code
'''turtle.color('red')
for _ in [1, 2, 3]: #o triangulo
    turtle.forward(100)
    turtle.right(120)

for _ in [1, 2, 3, 4]: #o retangulo
  turtle.forward(100)
  turtle.right(90)'''

#1) aumentar o tamanho do envelope
'''turtle.color('red')
for _ in [1, 2, 3]:
    turtle.forward(150)
    turtle.right(120)

for _ in [1, 2, 3, 4]:
  turtle.forward(150)
  turtle.right(90)'''

#2) usar formas diferentes da tartaruga 
'''turtle.color('red')
for _ in [1, 2, 3]:
    turtle.shape('arrow')
    turtle.forward(150)
    turtle.right(120)

for _ in [1, 2, 3, 4]:
    turtle.shape('circle')
    turtle.forward(150)
    turtle.right(90)'''

#3) deixar o envelope colorido
# rainbow = ('red', 'purple', 'pink', 'green')
# color = random.choice(rainbow)
# turtle.color(color)
# for _ in [1, 2, 3]:
#     cores = random.choice(rainbow)
#     turtle.color(cores)
#     turtle.forward(150)
#     turtle.right(120)

# for _ in [1, 2, 3, 4]:
#     cores = random.choice(rainbow)
#     turtle.color(cores)
#     turtle.forward(150)
#     turtle.right(90)

#4) reduzir a aba do envelope
'''turtle.color('red')
for _ in range(3): 
    turtle.forward(90)
    turtle.right(120)

for _ in range (4): 
  turtle.forward(100)
  turtle.right(90)'''





########### questao 6






# import turtle

# turtle = turtle.Turtle()
# turtle.color('green')

#main code
'''for _ in [1, 2, 3]:
    turtle.forward(100)
    turtle.right(120)

for _ in [1, 2, 3, 4]:
  turtle.left(90)
  turtle.forward(100)'''



#mudando
# for _ in [1, 2, 3]:
#     turtle.forward(100)
#     turtle.right(120)

# for _ in [1, 2, 3, 4]:
#   turtle.forward(100)
#   turtle.right(90)






################### questao 7





# import turtle

# turtle = turtle.Turtle()
# turtle.color('green')

#main code
'''for _ in range(4):
    turtle.left(90)
    turtle.backward(100)

turtle.backward(50)
turtle.backward(100)
turtle.right(90)

for _ in range(3):
  turtle.forward(100)
  turtle.left(90)'''

#1) mudar a distancia entre as lentes
'''for _ in range(4):
    turtle.left(90)
    turtle.backward(100)

turtle.backward(60)
turtle.backward(60)
turtle.right(90)

for _ in range(3):
  turtle.forward(100)
  turtle.left(90)'''

#2) mudar o tamanho das lentes
# for _ in range(4):
#     turtle.left(90)
#     turtle.backward(150)

# turtle.backward(100)
# turtle.backward(100)
# turtle.right(90)

# for _ in range(3):
#   turtle.forward(150)
#   turtle.left(90)





############# questao 8 





# import turtle
# import random
# turtle = turtle.Turtle()

#main code
'''colors = ['purple', 'blue', 'yellow', 'green', 'pink']
for _ in range (8):
    color = random.choice(colors)
    turtle.color(color)
    turtle.forward(100)
    turtle.backward(100)
    turtle.right(45)'''

#1) acrecentar cores
'''colors = ['purple', 'blue', 'yellow', 'green', 'pink', 'orange', 'red']
for _ in range (8):
    color = random.choice(colors)
    turtle.color(color)
    turtle.forward(100)
    turtle.backward(100)
    turtle.right(45)'''

#2) mudar largura das linhas
'''colors = ['purple', 'blue', 'yellow', 'green', 'pink']
for _ in range (8):
    color = random.choice(colors)
    turtle.color(color)
    turtle.forward(90)
    turtle.backward(90)
    turtle.right(45)'''

#3) aumentar quantidade de linhas
# colors = ['purple', 'blue', 'yellow', 'green', 'pink']
# for _ in range (8):
#     color = random.choice(colors)
#     turtle.color(color)
#     turtle.forward(100)
#     turtle.backward(100)
#     turtle.right(60)
#     turtle.forward(100)
#     turtle.backward(100)
#     turtle.right(90)






#################### questao 9 






# import turtle
# turtle = turtle.Turtle()
# import random

#main code 
'''for c in range(360):
    turtle.color('red')
    turtle.forward(1)
    turtle.right(1)'''


#1) cada passo ter cor diferente
'''colors = ['green', 'pink', 'blue','red']
for c in range(120):
    color = random.choice(colors)
    turtle.color(color)
    turtle.forward(2)
    turtle.right(2)'''

#2) aumentar/diminuir o diametro
# for c in range(200):
#     turtle.color('red')
#     turtle.forward(5)
#     turtle.right(2)





########## questao 10








# import turtle
# turtle = turtle.Turtle()
#main code
'''for _ in range(4):
    turtle.forward(100)
    turtle.right(90)

for _ in range(4):
   turtle.left(90)
   turtle.forward(100)

for _ in range(4):
   turtle.forward(100)
   turtle.left(90)

for _ in range(4):
   turtle.right(90)
   turtle.forward(100)'''

#1) cada quadrado ter uma cor
'''for _ in range(4):
    turtle.color('pink')
    turtle.forward(100)
    turtle.right(90)

for _ in range(4):
   turtle.color('blue')
   turtle.left(90)
   turtle.forward(100)

for _ in range(4):
   turtle.color('green')
   turtle.forward(100)
   turtle.left(90)

for _ in range(4):
   turtle.color('red')
   turtle.right(90)
   turtle.forward(100)'''

#2) cada quadrado com um formato diferente da tartaruga
'''for _ in range(4):
    turtle.shape('arrow')
    turtle.forward(100)
    turtle.right(90)

for _ in range(4):
   turtle.shape('circle')
   turtle.left(90)
   turtle.forward(100)

for _ in range(4):
   turtle.shape('turtle')
   turtle.forward(100)
   turtle.left(90)

for _ in range(4):
   turtle.shape('triangle')
   turtle.right(90)
   turtle.forward(100)'''

#3) Faça os quadrados não se tocarem
#NAO TENHO CAPACIDADE

#4) desenhar quadradop maior #nao tenho inteligencia suficiente p isso
# for _ in range(4):
#     turtle.forward(100)
#     turtle.right(90)

# for _ in range(4):
#    turtle.left(90)
#    turtle.forward(100)

# for _ in range(4):
#    turtle.forward(100)
#    turtle.left(90)

# for _ in range(4):
#    turtle.right(90)
#    turtle.forward(100)


# turtle.forward(220)
# turtle.left(90)
# turtle.forward(220)
# turtle.left(90)
# turtle.forward(400)
# turtle.left(90)
# turtle.forward(400)
# turtle.left(90)
# turtle.forward(400)
# turtle.left(90)
# turtle.forward(220)


   
    
    
    

    
    
    