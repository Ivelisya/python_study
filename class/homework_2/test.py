import pickle

def main():
    records = []
    print("请输入3个记录:")
    
    for i in range(3):
        print(f"\nRecord {i+1}:")
        string_data = input("Enter string: ")
        int_data = int(input("Enter integer: "))
        float_data = float(input("Enter float: "))
        
        record = (string_data, int_data, float_data)
        records.append(record)
    
    with open("myfile.dat", "wb") as file:
        pickle.dump(records, file)
    
    print("\nData已成功写入myfile.dat")
    print("\n从myfile.dat读取data:")
    with open("myfile.dat", "rb") as file:
        read_records = pickle.load(file)
    
    print("\nContents of myfile.dat:")
    for i, record in enumerate(read_records):
        print(f"Record {i+1}: String='{record[0]}', Integer={record[1]}, Float={record[2]}")
    
    if records == read_records:
        print("\nVerification: 验证通过.")
    else:
        print("\nWarning: 检查代码问题.")
        

if __name__ == "__main__":
    main()