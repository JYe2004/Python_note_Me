'''python
    study_1'''
'''
num1 = 10
num2 = 12.2
print(type(num1), type(num2))
sum1 = num1 + int(num2)
print(sum1)


rec = input('Are you OK?') #返回str类型
print(rec)

#两数之和
a = input("请输入一个整数")
b = input("请再输入一个整数")
sum2 = int(a) + int(b)
print(f"{sum2}")
'''

'''
greet = "hello ,"
print(greet + " world!")
print("""hello
world!""")
'''

#库
'''
print()是Python内置库
但是像math这些库就要自己导入
导入方法:
import math
math.函数名(...)
math.sin(1) == sin1
print(math.log2(8))
'''

#求平方根公式
'''
import math

a = input("inter number 'a'")
b = input("inter number 'b'")
c = input("inter number 'c'")

delta = int(b)**2 - 4*int(a)*int(c)
result_1 = (math.sqrt(delta) - int(b)) / 2*int(a)
result_2 = -(delta**(1/2) + int(b)) / 2*int(a)
print(result_1)
print(result_2)
'''

#注释快捷键
'''
先选中一段代码
按住ctrl + '/'
再按一次取消
'''

#len()
'''

s1 = len("hello world!")
print(s1)
'''

#条件语句
# if
# else
'''

mood = int(input("忘掉了吗:"))
if mood == 0:
    print("忘掉了")
    print("好、(*^▽^*)")
else:
    print("你还想她")
    print("o(╥﹏╥)o")
'''

#嵌套语句
#elif()

#在Python中可以直接用and or not
#if(x < 10 and x >= 5)

#列表[] , 最值
'''
shop_list = []
shop_list.append("数据类型")
shop_list.append("数组")
shop_list.remove("数组")
shop_list.append("指针")
shop_list[1] = "结构体"
#注意这里赋值不用加(),
#也不用加append

print(shop_list)
print(len(shop_list))
print(shop_list[0])

price = [122 , 233 , 1024 , 667]
max_price = max(price)
min_price = min(price)
a = sorted(price)
print(min_price,max_price,a)'''

#dict -- 字典类型
#用于存储键值对 -- { "" : ""}
#元组tuple

# -- ()
# del -- 删除键
'''
Fashion_dict = {("张伟"): "律师",
                ("张伟", 26): "医生",
                ("张伟", 99): "演员"}
Fashion_dict["男神"] = "周杰伦"

query = input("Please inter the word you want:")

if query in Fashion_dict:
    print("Enter" + query + "this :")
    print(Fashion_dict[query])
else :
    print("Sb!")
    print("all is " + str(len(Fashion_dict)),"条")
'''

#for循环

#循环 for (变量名) in 有迭代性质的东西
#列表
'''
temperature_1ist = [36.4, 36.6, 36.2, 37.0, 38.4]
# 字典
temperature_dict = {"111": 36.4, "112": 36.6, "113": 66.6}
for staff_id, temperature in temperature_dict.items():
    if temperature >= 37:
        print(staff_id, temperature)
        # print(temperature)
        print("You Over!")
'''

#range(5,10)  -- x >= 5 and x < 10
# range(5 , 10 ,2) -- 2是步长,每次夸跨两个数字

#1 + ... + 100
'''
total = 0
for i in range(1,101):
    total += i
print("total is",total)
'''

#while循环 -- 在不确定循环多少次的时候用
# while  （条件）
# 输入数字求平均值
'''

total = 0
count = 0
print("哈喽呀！我是一个求平均值的程序。")
User_input=input("请输入数字"
                 "（完成所有数字输入后"
                 ",请输入g终止程序）:")
while User_input != 'q':
    num = int(User_input)
    total += num
    count += 1
    User_input = input("请输入数字"
                       "（完成所有数字输入后"
                       ",请输入g终止程序）:")

print("while is " ,count)
print("total is " ,total/count)
'''

#format()
'''
name= "老林"
year="虎"
message_content = f"""
律回春渐,新元肇启。
新岁甫至,福气东来。
金{year}贺岁,欢乐祥瑞。
金{year}敲门,五福临门。
给{name}及家人拜年啦！
新春快乐,{year}年大吉！
"""
print(message_content)
'''
'''
name= "老林"
year="虎"
#初始化变量
message_content = """
律回春渐,新元肇启。
新岁甫至,福气东来。
金{0}贺岁,欢乐祥瑞。
金{0}敲门,五福临门。
给{1}及家人拜年啦！
新春快乐,{0}年大吉！
""".format(year,name)
print(message_content)'''

'''
grade_dict = {"小明": 3.251,
            "小花": 3.869,
            "小李": 2.683,
            "小张": 3.685}

for name in grade_dict:
    grade = grade_dict[name]
    print("name :{0} -- your grade is : {1:.2f} "
          .format(name, grade))
# {1:.2f} -- 不能写空格'''
'''
def countBMI(Weight , Height):
    BMI = Weight / Height ** 2
    if BMI <= 18.5:
        category = "thinner"
        print(category)

    elif BMI > 18.5 and BMI <= 25:
        category = "normal"
        print(category)

    else :
        category = "bigger"
        print(category)

    return BMI

# weight = input("Enter you Weight:")
# height = input("Enter you Height:")
# float(weight)
# float(height)
# countBMI(weight , height)
countBMI(50 ,1.62)
'''

#面向对象编程
# 类
'''
class CuteCat:
    def __init__(self , cat_name,
                 cat_age,cat_color):
        self.name = cat_name
        self.age = cat_age
        self.color =cat_color

    # 方法
    def speak(self):
        print("mi" *self.age)

    def think(self , content):
        print(f"Cat {self.name} is "
              f"thinking {content}...")

cat_1 = CuteCat("Amy" , 2 , "red")
print(f"Cat called {cat_1.name},it is {cat_1.age} "
      f"and its color is {cat_1.color}")

cat_2 = CuteCat("Jojo" , 4 , "Blue")
cat_2.think("3245y64164")

# print(f"this is the second cat{cat_2}")'''

'''
#大写切换风格
class Student:
    def __init__(self, name, student_ID):
        self.name = name
        self.student_ID = student_ID
        self.grades = {"Chinese":0,
                       "Math": 0,
                       "English":0}

    def set_grade(self, course, grade):
        if course in self.grades:
            self.grades[course] = grade

    def print_grades(self):
        print(f"Student {self.name}(number:{self.student_ID})"
              f",your grade is:")
        for course in self.grades:
            print(f"{course}:{self.grades[course]}")

Chen = Student("chen",4)
Chen.set_grade("Chinese" ,100)
Chen.set_grade("English", 120)
Chen.print_grades()
'''

# 继承 -- 父类子类
#类继承练习：人力系统
# A1
# #-员工分为两类：全职员工FullTimeEmployee、兼职员工PartTimeEmployee。
# #-全职和兼职都有"姓名name"、"工号id"属性，
# #
# 都具备"打印信息print_info”(打印姓名、工号)方法。
# #-全职有"月薪monthly_salary"属性，
# #
# 兼职有"日薪daily_salary"属性、"每月工作天数work_days"的属性。
# #-
# 全职和兼职都有"计算月薪calculate_monthly_pay"的方法，但具体计算过程不一样。
#
'''
class Employee:#用不上
    def __init__(self,name,id):#为了赋值
        self.name = name
        self.id = id

    def print_info(self):
        print(f"Employee:{self.name} ,"
              f"number:{self.id}")
class FullTimeEmployee(Employee):
    # def初始化的是全部的变量，包含继承的和自己的
    def __init__(self ,name ,id ,monthly_salary):
        #super()初始化的是需要继承的东西，这里是Employee有的
        #name和id
        super().__init__(name, id)
        self.monthly_salary = monthly_salary

    def calculate_monthly_pay(self):
        return self.monthly_salary

Chen = FullTimeEmployee("chen" ,"10" ,6000)
Chen.print_info()
print(Chen.monthly_salary)
'''


########################
# 使用循环

'''

for i in range(1, 5, 2):
    print(i)
'''
'''

num = 1
for i in range(1, 6):
    num *= i
print(num)
'''
#有关列表
'''
cities = ["beijing", "guangzhou", "shanghai", "shenzhen"]
for i in cities:
    if i == "guangzhou":
        print(i)
'''
'''
cities = ["beijing", "guangzhou", "shanghai", "shenzhen"]
for i in range(0, len(cities)):
    print(i, cities[i])
'''

#有关字典
#法1
'''
cities = {"zhangsan": 100, "LIsi": 101, "Wangwu": 102}
for name in cities:
    print(name) # -- key
    print(cities[name])
    print(f"{name}: {cities[name]}")
'''
#法2
'''
scores = {'zhangsan':98, 'lisi':89, 'maishu':96}
for name in scores.items():
    print(name)
'''
# 法3

# 直到输入exit才停止让你输入内容
# 否则会一直要求你输入内容

print(999)








