import asyncio

async def run(i):
    print('协程开始')
    print('协程结束')
    
async def main():
    takes= []
    for i in range(1,5):
        take = asyncio.create_task(run(i))
        takes.append(take)
    done = await asyncio.gather(*takes)#*拿出列表元素，解包
    for d in done:
        print(d)
if __name__ == '__main__':
     asyncio.run(main())