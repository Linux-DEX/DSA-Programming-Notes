import sys 

# def func(lst=None):
#     if lst == None:
#         lst = []
#     lst.append(1)
#     print(lst)

def func(lst=[]):
    lst.append(1)
    print(lst)

func() 
func()  
func()  

def ErrorFunction():
    try:
        value = 10/0
    except Exception as e:
        print(f'error : {str(e)}')

try:
    ErrorFunction()
except Exception as e:
    print(f'error : {str(e)}')


for path in sys.path:
    print(path)
