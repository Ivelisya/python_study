import frequency_analysis

def main():
    # 测试字符串，包含中英文混合
    test_string = "hello 世界 hello 世界"

    # 调用analyze_frequency函数
    frequency_list = frequency_analysis.analyze_frequency(test_string)

    # 打印结果
    for char, freq in frequency_list:
        print(f"字符 '{char}' 出现 {freq} 次")

if __name__ == "__main__":
    main()