import os
from collections import defaultdict

FILENAME = "student_grades.txt"

# (1) 写入初始数据 (如果文件不存在或需要覆盖)
def write_grades(data_list):
    try:
        with open(FILENAME, 'w', encoding='utf-8') as f:
            for record in data_list:
                # 将列表中的所有元素转为字符串再连接
                f.write(','.join(map(str, record)) + '\n')
        print(f"学生成绩已写入 {FILENAME}")
    except IOError as e:
        print(f"写入文件时出错: {e}")

# (2) 读取、分析并返回所有记录
def read_and_analyze():
    records = []
    grades_by_course = defaultdict(list)
    if not os.path.exists(FILENAME):
        print(f"文件 {FILENAME} 不存在。")
        return records # 返回空列表

    try:
        with open(FILENAME, 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) == 4:
                    try:
                        course, name, sid = parts[0], parts[1], parts[2]
                        grade = float(parts[3]) # 成绩转为浮点数
                        records.append([course, name, sid, grade])
                        grades_by_course[course].append(grade)
                    except ValueError:
                        print(f"警告: 跳过格式错误或成绩无效的行: {line.strip()}")

        print("\n--- 各课程成绩统计 ---")
        for course, grades in grades_by_course.items():
            if grades:
                avg = sum(grades) / len(grades)
                print(f"{course}: 平均分={avg:.2f}, 最高分={max(grades)}, 最低分={min(grades)}")
        return records
    except IOError as e:
        print(f"读取文件时出错: {e}")
        return [] # 出错时返回空列表

# (3) 查找指定学生的成绩
def find_student_grades(records, student_name):
    found = False
    print(f"\n--- 查找学生 {student_name} 的成绩 ---")
    for course, name, sid, grade in records:
        if name == student_name:
            print(f"  课程: {course}, 学号: {sid}, 成绩: {grade}")
            found = True
    if not found:
        print(f"未找到学生 {student_name} 的成绩记录。")

# (4) 修改指定学生指定课程的成绩并重写文件
def modify_grade(records, student_name, course_name, new_grade):
    modified = False
    try:
        new_grade_float = float(new_grade) # 验证新成绩是否为数字
        for i in range(len(records)):
            # 直接通过索引修改列表中的元素
            if records[i][1] == student_name and records[i][0] == course_name:
                records[i][3] = new_grade_float
                modified = True
                print(f"已修改 {student_name} 的 {course_name} 成绩为 {new_grade_float}")
                break # 假设每个学生每门课只有一条记录，找到后即可退出
        if modified:
            write_grades(records) # 如果修改成功，则将整个更新后的列表写回文件
        else:
            print(f"未找到 {student_name} 的 {course_name} 成绩记录，无法修改。")
    except ValueError:
        print("错误: 新成绩必须是有效的数字。")
    except Exception as e:
        print(f"修改并写入文件时发生错误: {e}")


initial_student_data = [
    ["高等数学", "张三", "S1001", 85.5],
    ["大学英语", "张三", "S1001", 78.0],
    ["高等数学", "李四", "S1002", 92.0],
    ["程序设计", "李四", "S1002", 88.5],
    ["高等数学", "王五", "S1003", 76.0],
    ["大学英语", "王五", "S1003", 81.0],
]

if not os.path.exists(FILENAME):
     write_grades(initial_student_data)


all_records = read_and_analyze()

if all_records: # 确保读取到了数据
    find_student_grades(all_records, "张三")
    find_student_grades(all_records, "赵六") # 查找不存在的学生

if all_records:
    modify_grade(all_records, "李四", "高等数学", 95.0)
    # 尝试修改不存在的记录
    modify_grade(all_records, "张三", "体育", 90.0)
    # 尝试使用无效成绩修改
    modify_grade(all_records, "王五", "大学英语", "Excellent")

    # 可以选择再次读取并分析来查看修改后的结果
    print("\n--- 修改后的数据分析 ---")
    updated_records = read_and_analyze()