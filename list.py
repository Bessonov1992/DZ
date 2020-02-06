a = {"apple":"iphone", "samsung":"galaxy", "huawei":"mate"}
b = {"xiaomi":"redmi", "oppo":"y", "vivo":"vibe"}
c = {"doogee":"sgm", "blackview":"BV", "meizu":"Note"}
def sumlist():
    dict = {**a, **b, **c}
    return dict
d = sumlist()
print(d)