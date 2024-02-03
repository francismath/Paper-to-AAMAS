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
    print(filename+'写入完成')#写入完成后给出完成信号，生成的txt在本文件所在的文件夹
##函数定义完成，下面开始调用函数


my_filename = '实验文件.txt' #我想储存信息的文件名
my_values = [root1, diff_on_x, diff_on_z] #我想储存的值
my_valuename = ['root1', 'diff_on_x', 'diff_on_z'] #valuename用来给每个值赋一个名字，方便自己查阅
save_to_file(my_filename, my_valuename, my_values) #调用save_to_file函数储存信息

#valuename可以是自己随便设定，只要自己能明白就行，下面是一个例子
my_filename2 = '一个例子.txt'
my_values2 = [root1, diff_on_x, diff_on_z]
my_valuename2 = ['第一个值', '第二个值', '第三个值']
save_to_file(my_filename2, my_valuename2, my_values2) #调用save_to_file函数储存信息

##下面定义一个储存函数以latex格式储存运行结果
def save_to_file(filename, valuename, value):
    notebook = open(filename, 'w')
    for i in range(len(valuename)):
        notebook.write(valuename[i]+'='+str(sympy.latex(value[i]))+'\n')#调用sympy的latex把value里的值latex化
        notebook.write('\n')
    notebook.close()
    print(filename+'写入完成')
#下面开始调用函数
my_filename2 = '另一个例子.txt'
my_values2 = [root1, diff_on_x, diff_on_z]
my_valuename2 = ['第一个值', '第二个值', '第三个值']
save_to_file(my_filename2, my_valuename2, my_values2) #调用save_to_file函数储存信息
