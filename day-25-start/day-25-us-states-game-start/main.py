'''import pandas as pd
import turtle

screen = turtle.Screen()
screen.title("U.S States Game ")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")
pen = turtle.Turtle(visible=False)
pen.penup()
correct_answers = 0
already_answer = []

big_data = pd.read_csv('50_states.csv')
states = big_data.state.to_list()


while correct_answers != 2:
    answer_state = screen.textinput(title= f"{len(already_answer)}/50 states Correct",prompt='Make your guess').title()
    if answer_state in states:
        correct_answers += 1
        state_data = big_data[big_data.state == answer_state]
        pen.goto(state_data.x.item(),state_data.y.item())
        pen.write(answer_state)
        already_answer.append(answer_state)
    
        
screen.exitonclick()
'''

import pandas as pd
import turtle

correct_answers = 0
already_answer = []

big_data = pd.read_csv('50_states.csv')
states = big_data.state.to_list()

screen = turtle.Screen()
pen = turtle.Turtle()
pen.penup()
pen.hideturtle()

while correct_answers != 50:
    answer_state = screen.textinput(title=f"{len(already_answer)}/50 states Correct", prompt='Make your guess').title()
    if answer_state in states and answer_state not in already_answer:
        correct_answers += 1
        state_data = big_data[big_data.state == answer_state]
        pen.goto(state_data.x.item(), state_data.y.item())
        pen.write(answer_state)
        already_answer.append(answer_state)

screen.exitonclick()