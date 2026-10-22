import numpy as np
import random as rn
import math

# problem 1
#input array of report IDs (as +integers)
#output two lists: list1 = unique IDs, list2 = [(id,cnt),...] ids and occurrences
print("\n Problem 1")
def duplicate_reports(r_ids):
    unique = []
    duplicates = []
    for i in r_ids:
        count = list(r_ids).count(i)
        if count == 1:
            unique.append(int(i))
        if count > 1:
            if (int(i), count) not in duplicates:
                duplicates.append((int(i),count))
    return unique,duplicates
            

report_ids = np.array([rn.randint(0,10) for _ in range(rn.randint(1,10))], dtype=int)
print(report_ids)
print(duplicate_reports(report_ids))

# problem 2
# input two NumPy array
# output dot product
# cannot use NumPy.dot(x,y)

print("\nProblem 2")
def my_scalar(x,y):
    total = 0
    for i in range(len(x)):
        total = total + x[i] * y[i]
    return total
        
    
a2 = np.array([1,2,3])
b2 = np.array([-3,4,0])
print(my_scalar(a2,b2), np.dot(a2,b2))
r2_r = rn.randint(2,10)
x2,y2 = np.array([rn.randint(-10,10) for _ in range(r2_r)]), np.array([rn.randint(-10,10) for _ in range(r2_r)])
print(x2,y2)
print(my_scalar(x2,y2), np.dot(x2,y2))

# problem 3
# input NumPy array
# output magnitude
# must use my_scalar
# cnnot use NumPy.linalg.norm(x)

print("\nProblem 3")
def my_magnitude(x):
    sum = 0
    for i in range(len(x)):
        sum = my_scalar(x,x)
    return math.sqrt(sum)


a3 = np.array([1,2,3])
print(my_magnitude(a3), np.linalg.norm(a3))
r3_r = rn.randint(2,10)
x3 = np.array([rn.randint(-10,10) for _ in range(r3_r)])
print(my_magnitude(x3),np.linalg.norm(x3))

print("\nProblem 4")

# problem 4
# input two NumPy arrays
# output cos in degrees
# must use my_scalar, my_magnitude
# cannot use NumPy functions
# two decimal places
def my_cos(x,y):
    cos = 0
    for i in range(len(x)):
        cos = (my_scalar(x,y))/my_magnitude(x)*my_magnitude(y)
    return (round(math.degrees(math.acos(a)),2))


x4 = np.array([1,0,0,1])
y4 = np.array([0,1,0,1])
a = np.dot(x4,y4)/(np.linalg.norm(x4)*np.linalg.norm(y4))
print(math.degrees(math.acos(a)),my_cos(x4,y4))


x4_1 = np.array([3,4])
y4_1 = np.array([8,15])
a = np.dot(x4_1,y4_1)/(np.linalg.norm(x4_1)*np.linalg.norm(y4_1))
print(my_cos(x4_1,y4_1),math.degrees(math.acos(a)))


# problem 5
#input proportion of house seats
#output proportion of presidential vote
# three decimal places

print("\nProblem 5")
def required_presidential_vote(h):
    alpha = (h/(1-h))**(1/3)
    final = alpha/(1+alpha)
    return round(final,3)
    
p5 = lambda x:(x**3)/(x**3 + (1-x)**3)
house_seats = 60/100
pres_vote = .534
print(p5(pres_vote), required_presidential_vote(house_seats), p5(required_presidential_vote(house_seats)))


print("\nProblem 6")
# problem 6
# input data described in HW
# output average of 1st,2nd 6-months
# this is done for you!
def q1(d):
    n = len(d)
    A = sum([x for _,(x,y) in d])/n
    B = sum([y for _,(x,y) in d])/n
    return round(A,2),round(B,2)

#input data
#output returns names of sales people who
#had zero sales either half
#must use comprhension
def q2(d):
    return [name for name, (x,y) in d if x==0 or y==0]


#input data
#output returns names of people who were better than the average
#of both halfs
def q3(d):
    return [name for name, (x,y) in d if x >= q1(d)[0] and y>=q1(d)[1]]

#input data
#output returns names of max sales (sum of both 6 months)
def q4(d):
    max_sales = max([x+y for name,(x,y)in d])
    return [name for name,(x,y) in d if x+y == max_sales]

d6 = [('a',(4,4)),('b',(0,5)),('c',(4,5)),('d',(3,2))]
print(q1(d6))
print(q2(d6))
print(q3(d6))
print(q4(d6))

print("\nProblem 7")

# problem 7
#input coef = (a,b,c) for ax^2 + bx + c
#output tuple ( 'up'|'down',(vertex,y-value of vertex) )
# round to two decimal places
def q(coef):
    a = coef[0]
    b = coef[1]
    c = coef[2]

    graph_pos = ""

    if a<0:
        graph_pos = "down"
    else:
        graph_pos = "up"

    vertex = (b*-1)/(2*a)
    f_of_vertex = a*(vertex**2)+b*vertex+c
    max_point = (round(vertex,2), round(f_of_vertex,2))

    return graph_pos, max_point

d7 = [(-2.6,7.6,-10),(1,-10.2,26.01)]
verticies = [q(d) for d in d7]
print(verticies)

print("\nProblem 8")

#problem 8
#input time, speed1, speed2 both heading in same direction
#output time train 2 reaches train 1
# round 2 decimal places
def train_type1(t0,s1,s2):
    return (t0*s1)/(s2-s1)
    

#input speed 1, speed 2, distance heading towards each other
#output time to reach each other
# round 2 decimal places
def train_type2(s1,s2,d):
    return d/(s1+s2)

t0_12,s1_12,s2_12 = 2,40,60
print(f"Time = {train_type1(t0_12,s1_12,s2_12)} hr")
d_12 = 400
print(f"Time = {train_type2(s1_12,s2_12,d_12)} hr")

print("\nProblem 9")

#problem 9
#input n >= k, use math module
#output nCr
def C(n,k):
    top =math.factorial(n)
    bottom = math.factorial(n-k)*math.factorial(k)
    return top/bottom

print(C(8,3))
############# do not change the following line ###################
if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the unit testing Feel free to add print statements. 
    You should uncomment *after* you've completed the function
    """

# uncomment to see output
# problem 1
# report_ids = np.array([rn.randint(0,10) for _ in range(rn.randint(1,10))],dtype=int)
# print(report_ids)
# print(duplicate_reports(report_ids))

#problem 2
# a2 = np.array([1,2,3])
# b2 = np.array([-3,4,0])
# print(my_scalar(a2,b2),np.dot(a2,b2))
# r2_r = rn.randint(2,10)
# x2,y2 = np.array([rn.randint(-10,10) for _ in range(r2_r)]),np.array([rn.randint(-10,10) for _ in range(r2_r)])
# print(x2,y2)
# print(my_scalar(x2,y2),np.dot(x2,y2))

#problem 3
# a3 = np.array([1,2,3])
# print(my_magnitude(a3), np.linalg.norm(a3))
# r3_r = rn.randint(2,10)
# x3 = np.array([rn.randint(-10,10) for _ in range(r3_r)])
# print(my_magnitude(x3),np.linalg.norm(x3))

#problem 4
# x4 = np.array([1,0,0,1])
# y4 = np.array([0,1,0,1])
# a = np.dot(x4,y4)/(np.linalg.norm(x4)*np.linalg.norm(y4))
# print(math.degrees(math.acos(a)),my_cos(x4,y4))

# x4_1 = np.array([3,4])
# y4_1 = np.array([8,15])
# a = np.dot(x4_1,y4_1)/(np.linalg.norm(x4_1)*np.linalg.norm(y4_1))
# print(my_cos(x4_1,y4_1),math.degrees(math.acos(a)))

# problem 5
# p5 = lambda x:(x**3)/(x**3 + (1-x)**3)
# house_seats = 60/100
# pres_vote = .534
# print(p5(pres_vote), required_presidential_vote(house_seats), p5(required_presidential_vote(house_seats)))

# problem 6
# d6 = [('a',(4,4)),('b',(0,5)),('c',(4,5)),('d',(3,2))]
# print(q1(d6))
# print(q2(d6))
# print(q3(d6))
# print(q4(d6))

# problem 7
# d7 = [(-2.6,7.6,-10),(1,-10.2,26.01)]
# verticies = [q(d) for d in d7]
# print(verticies)

# #problem 8
# t0_12,s1_12,s2_12 = 2,40,60
# print(f"Time = {train_type1(t0_12,s1_12,s2_12)} hr")
# d_12 = 400
# print(f"Time = {train_type2(s1_12,s2_12,d_12)} hr")

#problem 9
# print(C(8,3))