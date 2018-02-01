# list3 = [
#     {"name": "alex", "hobby": "抽烟"},
#     {"name": "alex", "hobby": "喝酒"},
#     {"name": "alex", "hobby": "烫头"},
#     {"name": "alex", "hobby": "Massage"},
#     {"name": "wusir", "hobby": "喊麦"},
#     {"name": "wusir", "hobby": "街舞"},]
#[{'name':alex,'hobby':[1,2,3,4]},{}]
#
# list_dic={}
# for x in list3:
# 	if x['name'] not in list_dic:
# 		list_dic[x['name']] ={'name':x['name'],'hobby':[x['hobby']]}
# 	else:
# 		dic=list_dic[x['name']]
# 		dic['hobby'].append(x['hobby'])
# lists=[]
# for i in list_dic.values():
# 	lists.append(i)
# print(lists)




# def position(li,left,right):
#     tmp = li[left]
#     while left<right:
#         while left < right and li[left] >li[right]:
#           pass
#     li[left]=tmp



# 抱着抱着抱着我的小鲤鱼的我的我的我
# def fun(n):
#     if n>0:
#       print("抱着",end="")
#       fun(n-1)
#       print("的我",end="")
#     else:
#       print("我的小鲤鱼",end="")
# fun(3)


# 汉诺塔问题
# def hanol(n,a,b,c):
#   if n>0:
#     hanol(n-1,a,c,b)
#     print('%d:   %s-->%s'%(n,a,c))
#     hanol(n-1,b,a,c)
#
# hanol(3,'A','B','C')


# 二分查找
# def linear_search(li,left,right,val):
#     if left <= right:
#         mid = (left + right) // 2
#         if li[mid]==val:
#             return mid
#         elif li[mid]<val:
#             return linear_search(li,mid+1,right,val)
#         else:
#             return linear_search(li,left,mid-1,val)
#     else:
#         return -1
#
# li=[1,2,3,4,5,6,7,8,9]
# print(linear_search(li,0,len(li)-1,1))
#
# li=[1,2,3,4,5,6,7,8,9]
# def linear_search(data_set, value):
#     for i in range(len(data_set)):
#         if data_set[i] == value:
#             return i
#     return -1
# print(linear_search(li,9))
#
#
#
# def bin_search(data_set, value):
#     low = 0
#     high = len(data_set) - 1
#     while low <= high:
#         mid = (low+high)//2
#         if data_set[mid] == value:
#             return mid
#         elif data_set[mid] > value:
#             high = mid - 1
#         else:
#             low = mid + 1
#
# li=[1,2,3,4,5,6,7,8,9]
# print(bin_search(li,8))


# li=[1,9,2,8,3,6,4,5,7]
#
# def bubble_sort(li):
#     for i in range(len(li)-1):
#         state=False #如果已经排序好，时间复杂度为O(n),否则为O(n^2)
#         for x in range(len(li)-1-i):
#             if li[x]>li[x+1]:
#                 li[x],li[x+1]=li[x+1],li[x]
#                 state=True
#         if not state:
#            return
#
# bubble_sort(li)
# print(li)


li = [1, 9, 2, 8, 3, 6, 4, 5, 7]
# def select_sort(li):
#     for i in range(len(li)-1):
#         min_loc=i
#         for j in range(i+1,len(li)):
#             if li[j] < li[min_loc]:
#                 min_loc = j
#             if min_loc !=i:
#                 li[i],li[min_loc] = li[min_loc],li[i]
# select_sort(li)
# print(li)

#
# def insert_sort(li):  #时间复杂度 O(n^2)
#     for i in range(1, len(li)):
#         print(li)
#         tmp = li[i]
#         j = i - 1
#         while j >= 0 and tmp < li[j]:
#             print('tmp=%s   li[j + 1]=%s    li[j]=%s   j=%s'%(tmp,li[j + 1],li[j],j))
#             li[j + 1] = li[j]
#             j = j - 1
#
#         li[j + 1] = tmp
#
#
# insert_sort(li)
# print(li)





# def func():
#     print('====>first')
#     b=yield 1
#     print('====>second',b)
#     a=yield 2
#     print('====>third',a)
#     yield 3
#     print('====>end')
#
# g=func()
# print(next(g))
# print(g.send('asdasd'))
# next(g)
