def calculate_states(*args):
    if not args:
        print("没有数据统计")
    numbers = []
    for arg in args:
        numbers.append(arg)
    max_val = max(numbers)
    min_val = min(numbers)
    sum_val = sum(numbers)
    avg_val = sum(numbers)/len(numbers)
    return {"max":max_val,"min":min_val,"sum":sum_val,"avg":avg_val}