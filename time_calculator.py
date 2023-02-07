def starter_hr(x,y,z=""):
    p = x.find(":")
    res = x[:p]
    return res
def adding_hr(x,y,z=""):
    p = y.find(":")
    res = y[:p]
    return res
def starter_min(x,y,z=""):
    p = x.find(":")
    b = x.find(" ")
    res = x[p+1:b]
    return res
def adding_min(x,y,z=""):
    p = y.find(":")
    res = y[p+1:]
    return res
def am_pm(x,y,z=""):
    p = x.find(" ")
    res = x[1+p:]
    return str(res)
def ap(x,y,z=""):
    f = am_pm(x,y,z)
    if f == "AM":
        res = True
    elif f == "PM":
        res = False

    return res
def min_pls(x,y,z=""):
    first_min = starter_min(x,y,z)
    second_min = adding_min(x,y,z)
    result = int(first_min) + int(second_min)
    if result >= 60:
        result -= 60
    return result
def min_pls_hr(x,y,z=""):
    first_min = starter_min(x,y,z)
    second_min = adding_min(x,y,z)
    if int(first_min) + int(second_min) >= 60:
        result = 1
    else:
        result = 0
    return result

def even_odd(x):
    if x % 2 == 0:
        return True
    elif x % 2 != 0 :
        return False
def number_ap(x,y,z=""):
    m = ap(x,y,z)
    if m == True:
        resu = 0
    elif m == False:
        resu = 1
    return resu
def day(x,y,z=""):
    da = z

    if da == "Saturday":
        return 1
    elif da == "Sunday":
        return 2
    elif da == "Monday":
        return 3
    elif da == "Tuesday":
         return 4
    elif da == "Wednesday":
        return 5
    elif da == "Thursday":
        return 6
    elif da == "Friday":
        return 7
    elif da == "":
        return  0
def str_days(x):
    if x == 1:
        return "Saturday"
    elif x == 2:
        return "Sunday"
    elif x == 3:
        return "Monday"
    elif x == 4:
        return "Tuesday"
    elif x == 5:
        return "Wednesday"
    elif x == 6:
        return "Thursday"
    elif x == 7:
        return "Friday"
    elif x == 0:
        return ""
def sub_seven(x):
    res = x
    while res > 7:
        res -= 7
    return res
    
def next_day(x):

    if x == 1:
        return "(next day)"
    elif x > 1:
        return f"({x} days later)"
    elif x < 1:
        return ""
def hr_pls(x,y,z=""):
    n_day = 0
    res_day = day(x,y,z)
    res_am_pm = am_pm(x,y,z)
    jot = number_ap(x,y,z)
    first = starter_hr(x,y,z)
    secound = adding_hr(x,y,z)
    addaition = min_pls_hr(x,y,z)
    first_min = starter_min(x,y,z)
    secound_min = adding_min(x,y,z)
    min_res = int(first_min) + int(secound_min)
    if min_res >= 60:
        min_res -= 60
    if len(str(min_res)) <2:
        min_res = "0" + str(min_res)
    li = list()
    for i in range(int(secound)):
        li.append(1)
    result = int(first) + int(addaition)
    if result > 11:
        jot += 1
        if even_odd(jot) == True:
            res_am_pm = "AM"
            n_day += 1
            if res_day > 0:
                res_day = res_day + 1
        elif even_odd(jot) == False:
            res_am_pm = "PM"
    if result > 12:
        result -= 12
    while len(li) > 0:
        result += li.pop()
        if result > 12:
            result -= 12
        if result > 11:
            jot += 1
            if even_odd(jot) == True:
                res_am_pm = "AM"
                n_day += 1
                if res_day > 0:
                    res_day = res_day + 1
            elif even_odd(jot) == False:
                res_am_pm = "PM"
    result_next_day = next_day(n_day)
    day_res= sub_seven(res_day)
    day_result = str_days(day_res)
    if day_result == "" and result_next_day == "":
        return f"{result}:{min_res} {res_am_pm}"
    elif day_result == "":
        return f"{result}:{min_res} {res_am_pm}" + " " + (result_next_day)
    elif len(str(day_result)) > 0 and result_next_day == "":
        return f"{result}:{min_res} {res_am_pm}" + ", " + str(day_result)
    elif len(str(day_result)) > 0 and len(result_next_day) > 0:
        return f"{result}:{min_res} {res_am_pm}" + ", " + (str(day_result)) + " " + (result_next_day)

def add_time(start, duration, z=""):

  new_time = hr_pls(start, duration, z)

  return new_time


print(add_time("5:51 PM", "240:00"))