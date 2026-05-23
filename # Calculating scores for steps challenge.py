# Calculating scores for steps challenge 
import sys 
import os 
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine 

app = QGuiApplication(sys.argv) 
engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load('./UI/main.qml') 
sys.exit(app.exec())


class StepsChallenge: 
    def __init__(self, user_name, user_score): 
        self.user_name = user_name 
        self.user_score = user_score 
        self.steps_list = [] 
        self.days_check = 1 

    # calculate score for the day 
    def calculate_score(self, placement, steps): 
        if placement == 1: 
            self.user_score += 3 
        elif placement == 2: 
            self.user_score += 2 
        elif placement == 3: 
            self.user_score += 1 
        if steps >= 10000: 
            self.user_score += 3 
        elif 10000 > steps >= 6000: 
            self.user_score +=  2 
        elif 6000 > steps >= 2000:
            self.user_score += 1 
        if self.days_check >= 7: 
            self.bonus_points()
        
        return self.user_score 
    
    # checks whether you've hit 5k --> 10k steps to calculate bonus 
    def ten_k_list_update(self, steps): 
        if steps >= 5000: 
            self.steps_list.append(steps)
        return self.steps_list 
    
    #only called at the end of the week to add any bonus points 
    def bonus_points(self): 
        index = 0 
        five_bonus = 0
        ten_bonus = 0
        while index < len(self.steps_list): 
            curr_num = self.steps_list[index]
            if curr_num < 5000: # [5000, 5003, 5006, 7000, 10000]
                return 0 
            elif 5000 < curr_num < 10000: 
                five_bonus += 1 
            if curr_num >= 10000: 
                ten_bonus += 1 
            
            index += 1 
        
        if ten_bonus >= 7: 
            self.user_score += 10 
        
        elif five_bonus >= 7: 
            self.user_score += 5 
            
        return self.user_score 
    
    # clear steps at the end of the week 
    def clear_steps_list(self): 
        listy = [] 
        self.steps_list = listy 
        return self.steps_list 
    
    def curr_score(self): 
        print(f"{self.user_name}" + f" {self.user_score}")
        return None 
    
"Testing scores"
Bob = StepsChallenge("Bob", 0)
Bob_steps = 10000
Bob.calculate_score(1, Bob_steps)
for i in range(7): 
    Bob.ten_k_list_update(Bob_steps) # [10k, 10k, 10k, 10k, 10k, 10k, 10k]

print(Bob.bonus_points()) # should print 10k bonus and score should be 16

Sally = StepsChallenge("Sally", 0)
Sally_steps = 4090
Sally.calculate_score(2, 4090)
for i in range(7): 
    Sally.ten_k_list_update(Sally_steps) # [4090, 4090, 4090, 4090, 4090, 4090, 4090]

print(Sally.bonus_points()) # should not print 5k or 10k bonus and score should be 3

Karen = StepsChallenge("Karen", 0)
Karen_steps = 5000
Karen.calculate_score(3, 5000)
for i in range(7):
    Karen.ten_k_list_update(Karen_steps) # [5k, 5k, 5k, 5k, 5k, 5k, 5k]
Karen.bonus_points()

""" Real scores
Bruce = StepsChallenge('Bruce', 137)
Bruce.calculate_score(1, 14068)
Bruce.curr_score()

Ed = StepsChallenge("Ed aka Fatass", 131)
Ed.calculate_score(15, 0)
Ed.curr_score()

Bot = StepsChallenge("Bot", 78)
Bot.calculate_score(4, 6920)
Bot.curr_score()

Joy = StepsChallenge("Joy", 52)
Joy.calculate_score(3, 9307)
Joy.curr_score()

Ale = StepsChallenge("Ale", 44)
Ale.calculate_score(2, 9680)
Ale.curr_score()

Tan = StepsChallenge("Tan", 41)
Tan.calculate_score(15, 0)
Tan.curr_score()

Solar = StepsChallenge("Solar", 37)
Solar.calculate_score(15, 0)
Solar.curr_score()

Alexa = StepsChallenge("Alexa", 33)
Alexa.calculate_score(5, 4209)
Alexa.curr_score()

Rhay = StepsChallenge("Ray", 30)
Rhay.calculate_score(7, 1640)
Rhay.curr_score()

Mih = StepsChallenge("Mih", 21)
Mih.calculate_score()
Mih.curr_score()

Natty = StepsChallenge("Natty", 18)
Natty.calculate_score()
Natty.curr_score()

Himi = StepsChallenge("Himi", 14)
Himi.calculate_score()
Himi.curr_score()

Sheep = StepsChallenge("Sheep", 13)
Sheep.calculate_score()
Sheep.curr_score()

Cookie = StepsChallenge("Cookie", 6)
Cookie.calculate_score()
Cookie.curr_score()

Varshika = StepsChallenge("Varshika", 7)
Varshika.calculate_score()
Varshika.curr_score()

Sara = StepsChallenge("Sara", 1)
Sara.calculate_score()
Sara.curr_score()
"""

# at the end of the week clear everybody's lists 