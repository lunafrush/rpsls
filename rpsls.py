#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：龚婕妤
日期：2021/5/28
"""
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
player_choice=input()
import random
def name_to_number(name):
 if name=='rock':
	 return 0
 elif name=='spock':
	 return 1
 elif name=='paper':
	 return 2
 elif name=='lizard':
	 return 3
 elif name=='scissors':
	 return 4
 else:
	 print("Error: No Correct Name")
def number_to_name(number):
 if number==0:
	 return'rock'
 elif number==1:
     return'spock'
 elif number==2:
     return'paper'
 elif number==3:
     return'lizard'
 elif number==4:
	 return'scissors'
 else:
	 print("Error: No Correct Name")
def rpsls(player_choice):
  print("The player's choice is "+str(player_choice))
  player_choice_number=name_to_number(player_choice)
  comp_number=random.randrange(0,4)
  comp_choice=number_to_name(comp_number)
  print("The computer's choice is "+str(comp_choice))
  diff=(comp_number-player_choice_number)%5
  if diff==1 or diff==2:
       print("The computer win!")
  elif diff==3 or diff==4:
       print("The player win!")
  elif diff==0:
       print("Tie")
  else:
	  print("Error: No Correct Name")
	  
rpsls(player_choice)
 

