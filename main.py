# 定义判断列表是否有重复元素的函数
def has_duplicates(lst):
    # 将列表转换为集合（集合自动去重）
    unique_set = set(lst)
    # 比较原列表和集合的长度，长度不同则有重复元素
    return len(lst) != len(unique_set)
# 测试函数
# 测试列表1：包含重复元素
test_list1 = [1, 2, 3, 3, 4]
print(f"列表 {test_list1} 是否有重复元素：{has_duplicates(test_list1)}")
# 测试列表2：不包含重复元素
test_list2 = [5, 6, 7, 8, 9]
print(f"列表 {test_list2} 是否有重复元素：{has_duplicates(test_list2)}")
# 测试列表3：所有元素都重复
test_list3 = [10, 10, 10, 10]
print(f"列表 {test_list3} 是否有重复元素：{has_duplicates(test_list3)}")
