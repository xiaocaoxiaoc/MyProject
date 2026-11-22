def add_sum(a,b):
    return a+b

def max_num(nums):
    return max(nums)
def min_num(nums):
    return min(nums)
def study():
    # =====================================================
    # Python基础学习：数据类型及相关操作
    # =====================================================

    print("=" * 50)
    print("Python基础数据类型学习")
    print("=" * 50)

    # =====================================================
    # 1. 数字类型：int、float
    # =====================================================

    print("\n【1. 数字类型】")

    # 整数
    a = 10
    b = 20

    print("整数a:", a)
    print("整数b:", b)
    print("数据类型:", type(a))

    # 基本数学运算
    print("加法:", a + b)
    print("减法:", a - b)
    print("乘法:", a * b)
    print("除法:", a / b)
    print("整除:", a // 3)
    print("取余:", a % 3)
    print("幂运算:", a ** 2)

    # 浮点数
    price = 19.99
    discount = 0.8

    print("商品价格:", price)
    print("折后价格:", price * discount)
    print("浮点数类型:", type(price))

    # =====================================================
    # 2. 布尔类型：bool
    # =====================================================

    print("\n【2. 布尔类型】")

    is_login = True
    is_admin = False

    print("是否登录:", is_login)
    print("是否管理员:", is_admin)

    # 比较运算
    print("10 > 5:", 10 > 5)
    print("10 < 5:", 10 < 5)
    print("10 == 10:", 10 == 10)
    print("10 != 5:", 10 != 5)

    # 逻辑运算
    print("AND:", True and False)
    print("OR:", True or False)
    print("NOT:", not True)

    # 布尔值转换
    print("bool(0):", bool(0))
    print("bool(1):", bool(1))

    # =====================================================
    # 3. 字符串类型：str
    # =====================================================

    print("\n【3. 字符串类型】")

    name = "Python"
    message = "Hello Python"

    # 字符串基本操作
    print("字符串:", name)
    print("字符串长度:", len(name))
    print("第一个字符:", name[0])
    print("最后一个字符:", name[-1])

    # 字符串切片
    print("前两个字符:", name[0:2])
    print("后面三个字符:", name[3:])
    print("反转字符串:", name[::-1])

    # 字符串拼接
    print("字符串拼接:", "Hello " + name)

    # 字符串重复
    print("字符串重复:", name * 3)

    # 常用字符串方法
    text = "  Hello Python  "

    print("去除空格:", text.strip())
    print("转换大写:", name.upper())
    print("转换小写:", name.lower())
    print("替换内容:", name.replace("Python", "AI"))
    print("是否包含:", "Py" in name)
    print("字符串分割:", "Java,Python,Swift".split(","))

    # 字符串格式化
    age = 25
    print(f"我的名字是{name}，年龄是{age}")

    # =====================================================
    # 4. 列表类型：list
    # =====================================================

    print("\n【4. 列表类型】")

    numbers = [10, 20, 30, 40, 50]

    print("列表:", numbers)
    print("列表长度:", len(numbers))
    print("第一个元素:", numbers[0])
    print("最后一个元素:", numbers[-1])

    # 修改元素
    numbers[0] = 100
    print("修改元素:", numbers)

    # 添加元素
    numbers.append(60)
    print("末尾添加:", numbers)

    numbers.insert(1, 15)
    print("指定位置添加:", numbers)

    # 删除元素
    numbers.remove(30)
    print("根据值删除:", numbers)

    deleted = numbers.pop()
    print("删除末尾元素:", deleted)
    print("删除后列表:", numbers)

    # 列表切片
    print("列表切片:", numbers[1:3])

    # 排序
    numbers.sort()
    print("升序排序:", numbers)

    numbers.sort(reverse=True)
    print("降序排序:", numbers)

    # 查询
    print("是否包含20:", 20 in numbers)
    print("20出现次数:", numbers.count(20))
    print("20所在位置:", numbers.index(20))

    # 遍历列表
    for item in numbers:
        print("列表元素:", item)

    # 列表推导式
    squares = [x ** 2 for x in range(1, 6)]
    print("平方列表:", squares)

    # =====================================================
    # 5. 元组类型：tuple
    # =====================================================

    print("\n【5. 元组类型】")

    person = ("Tom", 25, "Python")

    print("元组:", person)
    print("第一个元素:", person[0])
    print("元组长度:", len(person))

    # 元组切片
    print("元组切片:", person[0:2])

    # 元组查询
    print("是否包含Tom:", "Tom" in person)
    print("Tom出现次数:", person.count("Tom"))
    print("Tom所在位置:", person.index("Tom"))

    # 元组不可修改
    # person[0] = "Jack"  # 会报错

    # 元组拆包
    name, age, language = person
    print("姓名:", name)
    print("年龄:", age)
    print("语言:", language)

    # =====================================================
    # 6. 字典类型：dict
    # =====================================================

    print("\n【6. 字典类型】")

    user = {
        "name": "Tom",
        "age": 25,
        "gender": "男",
        "language": "Python"
    }

    print("字典:", user)

    # 获取数据
    print("姓名:", user["name"])
    print("年龄:", user.get("age"))

    # 添加数据
    user["city"] = "北京"
    print("添加数据:", user)

    # 修改数据
    user["age"] = 26
    print("修改数据:", user)

    # 删除数据
    user.pop("gender")
    print("删除数据:", user)

    # 获取所有键和值
    print("所有键:", user.keys())
    print("所有值:", user.values())
    print("所有键值对:", user.items())

    # 遍历字典
    for key, value in user.items():
        print(f"{key}: {value}")

    # 字典合并
    user.update({
        "email": "tom@example.com",
        "phone": "13800000000"
    })

    print("合并字典:", user)

    # =====================================================
    # 7. 集合类型：set
    # =====================================================

    print("\n【7. 集合类型】")

    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}

    print("集合A:", set_a)
    print("集合B:", set_b)

    # 添加元素
    set_a.add(6)
    print("添加元素:", set_a)

    # 删除元素
    set_a.discard(1)
    print("删除元素:", set_a)

    # 集合运算
    print("交集:", set_a & set_b)
    print("并集:", set_a | set_b)
    print("差集:", set_a - set_b)
    print("对称差集:", set_a ^ set_b)

    # 列表去重
    list_data = [1, 2, 2, 3, 3, 4]
    unique_data = list(set(list_data))

    print("原始列表:", list_data)
    print("去重结果:", unique_data)

    # =====================================================
    # 8. 空值类型：None
    # =====================================================

    print("\n【8. None类型】")

    result = None

    print("变量值:", result)
    print("变量类型:", type(result))
    print("是否为空:", result is None)

    # =====================================================
    # 9. 数据类型转换
    # =====================================================

    print("\n【9. 数据类型转换】")

    # 字符串转整数
    str_num = "100"
    int_num = int(str_num)
    print("字符串转整数:", int_num, type(int_num))

    # 整数转字符串
    num = 200
    str_value = str(num)
    print("整数转字符串:", str_value, type(str_value))

    # 字符串转浮点数
    float_value = float("3.14")
    print("字符串转浮点数:", float_value)

    # 列表转元组
    list_value = [1, 2, 3]
    tuple_value = tuple(list_value)
    print("列表转元组:", tuple_value)

    # 元组转列表
    tuple_data = (4, 5, 6)
    list_result = list(tuple_data)
    print("元组转列表:", list_result)

    # 列表转集合
    list_data = [1, 1, 2, 2, 3]
    set_data = set(list_data)
    print("列表转集合:", set_data)

    # =====================================================
    # 10. 综合应用：用户信息管理
    # =====================================================

    print("\n【10. 综合应用】")

    users = [
        {"name": "张三", "age": 25, "score": 90},
        {"name": "李四", "age": 30, "score": 85},
        {"name": "王五", "age": 22, "score": 95}
    ]

    # 遍历用户
    for user in users:
        print(
            f"姓名:{user['name']}, "
            f"年龄:{user['age']}, "
            f"成绩:{user['score']}"
        )

    # 计算平均成绩
    total_score = sum(user["score"] for user in users)
    average_score = total_score / len(users)

    print("总成绩:", total_score)
    print("平均成绩:", average_score)

    # 筛选成绩大于90的用户
    high_score_users = [
        user for user in users
        if user["score"] > 90
    ]

    print("高分用户:", high_score_users)

    print("\nPython基础数据类型学习结束！")

