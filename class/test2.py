def grade_query_system(grades):
  """
  成绩查询系统。
  Args:
    grades: 学生成绩列表，例如 [[学生1, 200], [学生2, 300], ...]
  """
  # 打印学生列表
  for i, student_grade in enumerate(grades):
    print(f"{i + 1}：{student_grade[0]}")
  while True:
    # 获取用户输入
    query = input("请输入学生编号或姓名（输入q退出）：")
    if query == "q":
      break
    # 尝试将输入转换为整数（学生编号）
    try:
      query_index = int(query) - 1
      if 0 <= query_index < len(grades):
        student_name, student_grade = grades[query_index]
        print(f"学生{student_name}：{student_grade}")
      else:
        print("输入的学生编号不存在！")
    except ValueError:
      # 如果输入不是整数，则视为学生姓名
      found = False
      for student_name, student_grade in grades:
        if student_name == query:
          print(f"学生{student_name}：{student_grade}")
          found = True
          break
      if not found:
        print("输入的学生姓名不存在！")
# 示例数据
grades = [
    ["学生1", 200],
    ["学生2", 300],
    ["学生3", 250],
    ["学生4", 350],
    ["学生5", 280],
    ["学生6", 320],
    ["学生7", 290],
    ["学生8", 310],
    ["学生9", 270],
    ["学生10", 330],
]

# 运行查询系统
grade_query_system(grades)