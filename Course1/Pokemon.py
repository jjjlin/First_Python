
# coding: utf-8

# In[1]:

import random
command = int(input('是否要開始對戰？ 0. 來打R   1. 滾吧'))
c_choice = random.randint(0, 1)
 
if command == 0:
  choice = int(input('選一隻神奇寶貝 0. 固拉多 1. 烈空座'))
  
  if choice == 0:
    print('你選擇了帝王龍')
    if c_choice == 0:
      print('平手拉')
      print(c_choice)
    if c_choice == 1:
      print('被打爆惹')
      print(c_choice)
    
      
  elif choice == 1:
    print('你選擇了天王龍')
    if c_choice == 0:
      print('吊起來打')
    if c_choice == 1:
      print('平手')

elif command == 1:
  print('沒得打拉')


# In[ ]:



