import asyncio

async def run(i):
    print('协程开始')
    print('协程结束')
    
async def main():
    takes= []
    for i in range(1,5):
        take = asyncio.create_task(run(i))
        takes.append(take)
    return await asyncio.wait(takes)
    # for d in done:
    #     print(d.result())
if __name__ == '__main__':
     done,pending = asyncio.run(main())
     for d in done:
        print(d.result())
# gather和wait的区别，asyncio.wait 会返回两个值: done 和 pending ， 
# done 为已完成的协程 Task ， pending 为超时未完成的协程 Task ，需通过 
# future.result 调用 Task 的 result ;而 asyncio.gather 返回的是所有已完成
# Task 的 result ，不需要再进行调用或其他操作，就可以得到全部结果