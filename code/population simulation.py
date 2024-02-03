#!/usr/bin/env python
# coding: utf-8

# In[9]:


tot_pop = 50 # initial total population 
gr_rate = 1.0005 # growth rate of population
data_acc = 0 # report a population every 2 months

while tot_pop < 100000:
    tot_pop *= gr_rate
    data_acc += 1
    if data_acc == 60:
        data_acc = 0
        #rint(tot_pop)
    


# In[12]:


# the code of Terence Shin
import random
startPopulation = 50 # starting population
infantMortality = 5 # the probability of a child dying in his/her first year of life

"""
agriculture measures the unit of food each person produces.
each person must eat one unit of food every year or they will die
if agriculture = 1 in a given year, everyone eats and there is no food left.
if agriculture = 0.5, 50% of the population dies
if agriculture = 1.5, everyone eats and there is 0.5 excess of food which could be stored for the next year
"""
agriculture = 5
# disasterChance means the probability of a disater happens in a given year
disasterChance = 10

"fertilityx and fertilityy denote the two terminal fertility ages for a woman"
fertilityx = 18
fertilityy = 35
food = 0
peopleDictionary = [] # data structure used to store all people

class Person:
    def __init__(self, age):
        self.gender = random.randint(0,1) # gender == 1 means the person is a woman
        self.age = age
        self.pregnant = 0
        
def harvest(food, agriculture):
    '''
    An able peoson is over 8 years old working to produce food
    anyone over 80 years old dies
    ''' 
    ablePeople = 0
    for person in peopleDictionary:
        if person.age > 8:
            ablePeople +=1
            
    food += ablePeople * agriculture
    '''if food < # of people, some people starve to die, else excess of food is stored'''
    if food < len(peopleDictionary):
        del peopleDictionary[0:int(len(peopleDictionary)-food)]
        food = 0
    else:
        food -= len(peopleDictionary)
'''
a certain number of women in the fertility band give birth to babies every year
'''        
def reproduce(fertilityx, fertilityy, infantMortality):
    for person in peopleDictionary:
        if person.gender == 1 and person.age > fertilityx and person.age < fertilityy:
            if random.randint(0,100)==1:#fertility rate = 0.01
                if random.random()>infantMortality:
                    peopleDictionary.append(Person(0))
                            
def beginSim():
    for x in range(startPopulation):
        peopleDictionary.append(Person(random.randint(18,50)))
        
def runYear(food, agriculture, fertilityx, fertilityy, infantMortality, disasterChance):
    harvest(food, agriculture)
    for person in peopleDictionary:
        if person.age > 80:
            peopleDictionary.remove(person)
        else:
            person.age +=1
    
    reproduce(fertilityx, fertilityy, infantMortality)
    
    if random.randint(0,100)<disasterChance:
        del peopleDictionary[0:int(random.uniform(0.05,0.2)*len(peopleDictionary))]
        print(len(peopleDictionary))
        infantMortality *= 0.985
    return infantMortality

beginSim()
while len(peopleDictionary)<100000 and len(peopleDictionary) > 1:
    infantMortality = runYear(food, agriculture, fertilityx, fertilityy, infantMortality, disasterChance)


# In[5]:


import random
startPopulation = 50
infantMortality = 5
youthMortality = 45
agriculture = 5
disasterChance = 10
fertilityx = 18
fertilityy = 35
food = 0
peopleDictionary = []
class Person:
    def __init__(self, age):
        self.gender = random.randint(0,1)
        self.age = age
        self.pregnant = 0
def harvest(food, agriculture):
    ablePeople = 0
    for person in peopleDictionary:
        if person.age > 8:
            ablePeople +=1
    food += ablePeople * agriculture
    
    if food < len(peopleDictionary):
        del peopleDictionary[0:int(len(peopleDictionary)-food)]
        food = 0
    else:
        food -= len(peopleDictionary)
def reproduce(fertilityx, fertilityy, infantMortality):
    for person in peopleDictionary:
        if person.gender == 1:
            if person.age > fertilityx:
                if person.age < fertilityy:
                    if random.randint(0,5)==1:
                        if random.randint(0,100)>infantMortality:
                            peopleDictionary.append(Person(0))
                            
def beginSim():
    for x in range(startPopulation):
        peopleDictionary.append(Person(random.randint(18,50)))

def runYear(food, agriculture, fertilityx, fertilityy, infantMortality, disasterChance):
    harvest(food, agriculture)
    for person in peopleDictionary:
        if person.age > 80:
            peopleDictionary.remove(person)
        else:
            person.age +=1
    
    reproduce(fertilityx, fertilityy, infantMortality)
    if random.randint(0,100)<disasterChance:
        del peopleDictionary[0:int(random.uniform(0.05,0.2)*len(peopleDictionary))]
    print(len(peopleDictionary))
        
    infantMortality *= 0.985
    return infantMortality


beginSim()
while len(peopleDictionary)<100000 and len(peopleDictionary) > 1:
    infantMortality = runYear(food, agriculture, fertilityx, fertilityy, infantMortality, disasterChance)


# In[3]:


import sympy ##符号运算核心包

a, b, c, d, x, z = sympy.symbols('a, b, c, d, x, z')  #调用sympy下的symbols方法告诉计算机 a, b, c, d, x, z是变量

equation1 = a*x**2 + b*x + c #定义一个简单的二次方程
root1 = sympy.solve(equation1, x) #调用sympy下的solve方法解方程，括号内第一项告诉计算机方程式，括号内第二项告诉计算机未知数
print(root1) #显示root1
diff_on_x = sympy.diff(equation1, x) #调用sympy下的diff方法求导，括号内第一项告诉计算机方程式，括号内第二项告诉计算机以谁为底求导
print(diff_on_x)
equation2 = sympy.cos(z)*sympy.sin(z) #sympy内置了一些常用函数
diff_on_z = sympy.diff(equation2, z) #equation2对z求导
print(diff_on_z)
matrix1 = sympy.Matrix([[a, b], [c, d]]) #调用sympy下的diff方法定义一个简单的矩阵，区别于MATLAB， python里的矩阵、向量是用[]而不是()
print(matrix1)
matrix1_det = sympy.det(matrix1) #调用sympy下的det方法求matrix1的determination
print(matrix1_det)


##下面定义一个储存函数来储存运行结果，函数包含两个变量，filename定义你存档的文件名称，valuename为你想储存的变量名字，value为你想储存变量的值
def save_to_file(filename, valuename, value):
    notebook = open(filename, 'w') #打开名为filename的文件，如果文件不存在，则生成一个名为filename的文件
    for i in range(len(valuename)): #用for循环写入每个value
        notebook.write(valuename[i]+'='+str(value[i])+'\n') #'\n'是换行的意思，每写入一个元素就换一行，方便阅读
        notebook.write('\n')#再写入一个空行，方便阅读
    notebook.close()
    print(filename+' write_in completed')#写入完成后给出完成信号，生成的txt在本文件所在的文件夹
##函数定义完成，下面开始调用函数


my_filename = '2nd ex.txt' #我想储存信息的文件名
my_values = [root1, diff_on_x, diff_on_z] #我想储存的值
my_valuename = ['root1', 'diff_on_x', 'diff_on_z'] #valuename用来给每个值赋一个名字，方便自己查阅
save_to_file(my_filename, my_valuename, my_values) #调用save_to_file函数储存信息



# In[3]:


import random
startPopulation = 50
infantMortality = 5
youthMortality = 45
agriculture = 5
disasterChance = 10
fertilityx = 18
fertilityy = 35
food = 0
peopleDictionary = []
class Person:
    def __init__(self, age):
        self.gender = random.randint(0,1)
        self.age = age
        self.pregnant = 0
def harvest(food, agriculture):
    ablePeople = 0
    for person in peopleDictionary:
        if person.age > 8:
            ablePeople +=1
    food += ablePeople * agriculture
    
    if food < len(peopleDictionary):
        del peopleDictionary[0:int(len(peopleDictionary)-food)]
        food = 0
    else:
        food -= len(peopleDictionary)
def reproduce(fertilityx, fertilityy, infantMortality):
    for person in peopleDictionary:
        if person.gender == 1:
            if person.age > fertilityx:
                if person.age < fertilityy:
                    if random.randint(0,5)==1:
                        if random.randint(0,100)>infantMortality:
                            peopleDictionary.append(Person(0))
                            
def beginSim():
    for x in range(startPopulation):
        peopleDictionary.append(Person(random.randint(18,50)))

    
def runYear(food, agriculture, fertilityx, fertilityy, infantMortality, disasterChance):
    harvest(food, agriculture)
    for person in peopleDictionary:
        if person.age > 80:
            peopleDictionary.remove(person)
        else:
            person.age +=1
    
    reproduce(fertilityx, fertilityy, infantMortality)
    if random.randint(0,100)<disasterChance:
        del peopleDictionary[0:int(random.uniform(0.05,0.2)*len(peopleDictionary))]
    #print(len(peopleDictionary))
     
    infantMortality *= 0.985
    return infantMortality

def save_to_file(filename, valuename, value):
    notebook = open(filename, 'w')
    for i in range(len(valuename)): #用for循环写入每个value
        notebook.write(valuename[i]+'='+str(value[i])+'\n') #'\n'是换行的意思，每写入一个元素就换一行，方便阅读
        notebook.write('\n')#再写入一个空行，方便阅读
    notebook.close()
    print(filename+' write_in completed')#写入完成后给出完成信号，生成的txt在本文件所在的文件夹

my_filename = '3rd ex.txt' #我想储存信息的文件名
my_values = [len(peopleDictionary)] #我想储存的值
my_valuename = ['root1'] #valuename用来给每个值赋一个名字，方便自己查阅
save_to_file(my_filename, my_valuename, my_values) #调用save_to_file函数储存信息
    
beginSim()
while len(peopleDictionary)<100000 and len(peopleDictionary) > 1:
    infantMortality = runYear(food, agriculture, fertilityx, fertilityy, infantMortality, disasterChance)



