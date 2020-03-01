# 02.28
# 判断是否有重复元素
def all_unique(lst):
    return len(lst) == len(set(lst))
x = [1,1,221,11,4,5,6]
y = [1,2,3,4,5]

from collections import Counter
# '判断组成元素是否相等'
def anagram(origin,des):
    return Counter(origin) == Counter(des)



# 02.29  
# '内存占用查看'
def varSizeof(var):
    import sys
    return sys.getsizeof(var)
def byte_size(string):
    import string
    return len(string.encode('utf-8'))
def name_test(name='',num=1):
    nameStrinfg = name*num
    return nameStrinfg.title()

def test_func(func):
    def wapper(*args,**kwargs):
        print("start")
        return func(*args,**kwargs)
        print('end')
    return wapper

@test_func
def test(name):
    print("666666 %s" % (name))


# mysql
    
if __name__ == "__main__":
    all_unique(x)
    print(name_test("lishen ",5))
    test("lishen")
     
