#冒泡排序
# li = [1, 9, 2, 8, 3, 6, 4, 5, 7]
# def maopao (li):
#     for i in range(len(li)-1):
#         state =False
#         for j in range(len(li)-1-i):
#             if li[j] < li[j+1]:
#                 li[j],li[j+1]=li[j+1],li[j]
#                 state = True
#         if not state:
#             return
# maopao(li)
# print(li)


#选择排序
# li = [1, 9, 2, 8, 3, 6, 4, 5, 7]
# def xuanze(li):
#     for i in range(len(li)-1):
#         tmp=i
#         for j in range(i+1,len(li)):
#             if li[tmp] > li[j]:
#                 tmp=j
#         li[i],li[tmp] = li[tmp],li[i]
# xuanze(li)
# print(li)

# 插入排序
# li = [1, 9, 2, 8, 3, 6, 4, 5, 7]
#
# def charu(li):
#     for i in range(len(li)):
#         tmp = li[i] # 3
#         j=i-1       # 3
#         while j >= 0 and tmp > li[j]: #2
#             li[j],li[j+1]=li[j+1],li[j]
#             j = j-1 # j=1
# charu(li)
# print(li)

# 快速排序
# li=[5,7,4,6,3,1,2,9,8]
# def partition(li,left,right):
#     while left < right:
#         while left < right and li[left] < li[right]:
#             right-=1
#         li[left],li[right] = li[right],li[left]
#         while left < right and li[left] < li[right]:
#             left+=1
#         li[left], li[right] = li[right], li[left]
#     return left
#
# def quick_sort(li,left,right):
#     if left < right:
#         mid = partition(li,left,right)
#         quick_sort(li,left,mid-1)
#         quick_sort(li,mid+1,right)
#
# quick_sort(li,0,len(li)-1)
# print(li)



# 归并排序
# li=[2,5,7,8,9,1,3,4,6]
# li=[5,7,4,6,3,1,2,9,8]
# def merge(li,left,mid,right):
#     i=left
#     j=mid +1
#     ltmp = []
#     while i <= mid and j<=right:
#         if li[i] < li[j]:
#             ltmp.append(li[i])
#             i+=1
#         else:
#             ltmp.append(li[j])
#             j+=1
#     while i <= mid :
#         ltmp.append(li[i])
#         i+=1
#     while j <=right :
#         ltmp.append(li[j])
#         j+=1
#     li[left:right+1]=ltmp
#
# def merge_sort(li,left,right):
#     if left < right:
#         mid = (left+right)//2
#         merge_sort(li,left,mid)
#         merge_sort(li,mid+1,right)
#         merge(li, left, mid, right)
#
# merge_sort(li,0,len(li)-1)
# print(li)
#
#
# a=[1,2,5,6,7,8,9]
# b=[3,4,10,11,12,13]
# a[2:4] =b
# print(a)


#希尔排序
# li=[5,7,4,6,3,1,2,9,8]
# def shell_sort(li):
#     d = len(li) // 2
#     while d > 0:
#         for i in range(d,len(li)):
#             tmp = li[i]
#             j = i - d
#             while j >=0 and tmp < li[j]:
#                 li[j],li[j+d] = li[j+d] ,li[j]
#                 j -=d
#         d//=2
# shell_sort(li)
# print(li)


# 计数排序
# import random
# li =[ random.randint(1,100) for x in range(100)]
#
# def count_sort(li,max_num):
#     counts = [0 for x in range(max_num+1)]
#
#     for i in li:
#         counts[i] +=1
#
#     for k,j in enumerate(counts):
#         for x in range(j):
#             print(k,end=" ")
# count_sort(li,100)


# 桶排序
import random
li =[ random.randint(1,100) for x in range(50)]

def charu(li):
    for i in range(len(li)):
        tmp = li[i]
        j = i - 1
        while j >= 0 and tmp < li[j]:
          li[j], li[j + 1] = li[j + 1], li[j]
          j = j - 1
    return li
def bucket_sort(li,max_num,n):
    bucket_count = max_num //n
    buckets = [[] for _ in range(0,max_num,bucket_count)]
    # print(buckets)
    print(bucket_count)

    for x in li:
        n = x // bucket_count
        if n ==10:
            n-=1
        buckets[n].append(x)

    li.clear()
    for bucket in buckets:
        b=charu(bucket)
        li.extend(b)

# [[9, 8], [10, 11, 12], [20, 23], [], [40], [], [], [], [], []]
bucket_sort(li,100,10)
print(li)






