"""
    Гадалка
"""
from brain import Brain

brain = Brain()
prompt = "Что Вас интересует?"

question = ""
while question != "хватит": 
    print(prompt, end = ' ')
    answer = brain.think(input())
    print(answer)
    