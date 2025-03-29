import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

def get_lagou_jobs():
    url = 'https://www.lagou.com/wn/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62"
    }
    cookie_string = "index_location_city=%E5%8C%97%E4%BA%AC; RECOMMEND_TIP=1; WEBTJ-ID=03282025%2C102918-195da95152a26c0-040fb21594bda1-26011d51-1821369-195da95152b369a; JSESSIONID=ABAACCCACFEAAAC3C4BFF3F6E7581B32E4FA09281668AA0; sajssdk_2015_cross_new_user=1; sensorsdata2015session=%7B%7D; user_trace_token=20250328102933-4d065fc4-dc48-4b1a-aef1-ed66ef16eaff; gate_login_token=v1####ce19ec9bfec3f5a8b3e81983dea0b21f663c0209fc44721e562f8a794da69ce7; LG_HAS_LOGIN=1; _putrc=9A17C7F66CE16FD2123F89F2B170EADC; login=true; unick=%E7%94%A8%E6%88%B79225; hasDeliver=0; privacyPolicyPopup=false; X_HTTP_TOKEN=fd6943937c1514a827092134719faaae9b15a1c74e; LGSID=20250328103112-e7fd4335-0757-4c6d-9231-d651d2f54987; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Feasy.lagou.com%2Falpha%2Fportal.htm%3Bjsessionid%3DABAABJAAAEJABDD3799DA623B7FA2D2702919361C8248F5; LGUID=20250328103112-d30a0dc0-f0d0-4d4a-a66b-cc40d0781919; mds_login_authToken=\"cosspAgfA6wGQBKtyEeGAAnxtD6rqikKveDaUWORg1UVMIhWZuJ4t4HAJFw3B7piY20tJJPV4OYlvbPYBx5WgxMyYH/6V5coD6i+9QfTTwhe/JPPLM+i9pZsvg+DuALAuBpFxqpS0oBo8LS6Una6FJo0UnmO2w6Ye0/C0dklfTR4rucJXOpldXhUiavxhcCELWDotJ+bmNVwmAvQCptcy5e7czUcjiQC32Lco44BMYXrQ+AIOfEccJKHpj0vJ+ngq/27aqj1hWq8tEPFFjdnxMSfKgAnjbIEAX3F9CIW8BSiMHYmPBt7FDDY0CCVFICHr2dp5gQVGvhfbqg7VzvNsw==\"; LGRID=20250328103128-5df7966c-cb73-434c-ad34-12ca4284bc58; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22195da9515ee14e4-00aa914b083dd5-26011d51-1821369-195da9515ef360c%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%22134.0.0.0%22%7D%2C%22%24device_id%22%3A%22195da9515ee14e4-00aa914b083dd5-26011d51-1821369-195da9515ef360c%22%7D"

    try:
        res = requests.get(url, headers=headers, cookies={'cookie': cookie_string}, timeout=10)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'lxml')
        positions = soup.find_all('div', class_='positionItem__2n56R')
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        csv_filename = f"lagou_jobs_{timestamp}.csv"
        
        with open(csv_filename, 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f)
            writer.writerow(["岗位名称", "薪资", "经验要求", "学历要求", "公司名称", "职位标签"])
            
            job_count = 0
            for position in positions:
                try:
                    job_name = position.find('div', class_='title__2Omkt').text.strip()
                    salary = position.find('div', class_='salary__TxYSY').text.strip()
                    base_info = position.find('div', class_='baseInfo__2P4d0').text.strip().split('/')
                    experience = base_info[0].strip()
                    education = base_info[-1].strip()
                    company_element = position.find('div', class_='companyName__3UJRz')
                    company_name = company_element.text.strip() if company_element else "未知"
                    tags_element = position.find('div', class_='positionLabels__1Tuti')
                    tags = tags_element.text.strip() if tags_element else ""
                    writer.writerow([job_name, salary, experience, education, company_name, tags])
                    job_count += 1
                    print(f"已爬取岗位 {job_count}: {job_name}")
                except Exception as e:
                    print(f"解析岗位信息出错: {e}")
                    continue
            print(f"爬取完成，共爬取 {job_count} 个岗位，数据已保存到 {csv_filename}")
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    get_lagou_jobs()