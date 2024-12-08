import aiohttp
import asyncio
from lxml import etree
import re
import random
import csv
import logging
import argparse
from datetime import datetime
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# 设置日志记录
logging.basicConfig(filename='C:/Users/20212/Desktop/smzy_study/Python_study/爬虫/豆瓣/douban_data.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69',
}

MAX_RETRIES = 3  # 最大重试次数


async def make_request(session, url):
    """发送异步 GET 请求并返回解析后的 HTML 树"""
    for attempt in range(MAX_RETRIES):
        try:
            async with session.get(url, headers=HEADERS) as res:
                res.raise_for_status()  # 检查请求是否成功
                return etree.HTML(await res.text())
        except Exception as e:
            logging.error(f"请求失败: {e}")
            if attempt < MAX_RETRIES - 1:
                logging.info(f"重试 {attempt + 1}/{MAX_RETRIES}...")
            else:
                return None


async def get_titles(page):
    """获取指定页数的电影标题"""
    titles = []
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(0, (page - 1) * 25 + 1, 25):
            url = f'https://movie.douban.com/top250?start={i}&filter='
            tasks.append(make_request(session, url))

        for future in asyncio.as_completed(tasks):
            tree = await future
            if tree is None:
                logging.error(f"无法解析页面: {url}")
                continue  # 跳过无法解析的页面
            div_list = tree.xpath('//div[@class="item"]')
            if not div_list:  # 如果没有找到电影项
                logging.warning("没有找到电影项")
                continue

            for div in div_list:
                title = div.xpath('.//a//text()')
                clean_title = re.sub(r'\s+', '', ''.join(title))
                titles.append(clean_title)
                print(f"抓取到的标题: {clean_title}")
                logging.info(f"抓取到的标题: {clean_title}")  # 写入日志
    return titles


async def get_best_reviews():
    """获取豆瓣评论页面的最佳评论"""
    reviews = []
    url = "https://movie.douban.com/review/best/"
    async with aiohttp.ClientSession() as session:
        tree = await make_request(session, url)
        if tree is None:
            logging.error("无法解析最佳评论页面")
            return reviews

        div_list = tree.xpath('.//div[@class="review-list chart "]/div')
        if not div_list:  # 如果没有找到评论
            logging.warning("没有找到评论")
            return reviews

        for div in div_list:
            short_content = re.sub(r'\s+', ' ', ''.join(div.xpath('.//div[@class="short-content"]/text()')))
            reviews.append(short_content.strip())
            print(f"抓取到的评论: {short_content.strip()}")
            logging.info(f"抓取到的评论: {short_content.strip()}")  # 写入日志
            await asyncio.sleep(random.randint(1, 5))  # 确保请求间隔
    return reviews


def save_to_csv(titles, reviews, filename='douban_data.csv'):
    """将标题和评论保存到 CSV 文件中"""
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Title'])  # 写入标题表头
            for title in titles:
                writer.writerow([title])  # 写入标题
            writer.writerow([])  # 空行分隔
            writer.writerow(['Review'])  # 写入评论表头
            for review in reviews:
                writer.writerow([review])  # 写入评论
        logging.info(f"数据已成功保存到 {filename}")
    except Exception as e:
        logging.error(f"保存数据失败: {e}")


def save_to_json(titles, reviews, filename='douban_data.json'):
    """将标题和评论保存到 JSON 文件中"""
    import json
    data = {
        "titles": titles,
        "reviews": reviews
    }
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        logging.info(f"数据已成功保存到 {filename}")
    except Exception as e:
        logging.error(f"保存数据失败: {e}")


async def main(titles_needed, reviews_needed, page, output_format):
    """主函数，用于获取标题和评论"""
    start_time = datetime.now()
    logging.info("程序开始运行")

    titles = []
    reviews = []

    if titles_needed:
        titles = await get_titles(page)
    if reviews_needed:
        reviews = await get_best_reviews()

    if output_format == 'csv':
        save_to_csv(titles, reviews)
    elif output_format == 'json':
        save_to_json(titles, reviews)

    end_time = datetime.now()
    logging.info(f"程序运行完成, 耗时: {end_time - start_time}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="豆瓣电影爬虫")
    parser.add_argument('--titles', action='store_true', help='获取电影标题')
    parser.add_argument('--reviews', action='store_true', help='获取最佳评论')
    parser.add_argument('--page', type=int, default=3, help='要获取的页数')
    parser.add_argument('--output', choices=['csv', 'json'], default='csv', help='输出文件格式')
    args = parser.parse_args()

    # 如果没有传入命令行参数，使用默认值
    if not args.titles and not args.reviews:
        args.titles = True  # 默认获取标题
        args.reviews = True  # 默认不获取评论

    asyncio.run(main(args.titles, args.reviews, args.page, args.output))
