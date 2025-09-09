import asyncio
import websockets
import json
import threading
import time


def start_websocket_server():
    async def handler(websocket, path):
        try:
            async for message in websocket:
                data = json.loads(message)
                print("\n" + "=" * 50)
                print("接收到用户会话数据:")
                print(f"用户ID: {data['userId']}")
                print(f"完成时间: {data['completedAt']}")

                # 打印任务1数据
                t1 = data['task1']
                print("\n任务1:")
                print(f"  - 标题: {t1['title']}")
                print(f"  - 类型: {t1['type']}")
                print(f"  - 答案：{t1['answer']}")
                print(f"  - 用时: 答题{t1['answerTime']}秒, 评分{t1['ratingTime']}秒")
                print(f"  - 评分: 理解{t1['ratings']['understanding']}, 相关{t1['ratings']['relevance']}, " +
                      f"质量{t1['ratings']['quality']}, 响应{t1['ratings']['responsiveness']}")

                # 打印任务2数据
                t2 = data['task2']
                print("\n任务2:")
                print(f"  - 标题: {t2['title']}")
                print(f"  - 类型: {t2['type']}")
                print(f"  - 答案：{t2['answer']}")
                print(f"  - 用时: 答题{t2['answerTime']}秒, 评分{t2['ratingTime']}秒")
                print(f"  - 评分: 理解{t2['ratings']['understanding']}, 相关{t2['ratings']['relevance']}, " +
                      f"质量{t2['ratings']['quality']}, 响应{t2['ratings']['responsiveness']}")

                print("=" * 50 + "\n")
        except Exception as e:
            print(f"导出， {e}")

    # 创建新的事件循环
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    # 创建服务器
    server = websockets.serve(handler, "localhost", 8765)

    # 启动服务器
    loop.run_until_complete(server)
    print("Python后端已启动，监听端口 8765...")

    # 永久运行事件循环
    loop.run_forever()


def run_server():
    # 在单独的线程中运行WebSocket服务器
    threading.Thread(target=start_websocket_server, daemon=True).start()

    # 保持主线程运行
    while True:
        time.sleep(1)


if __name__ == "__main__":
    print("启动拉丁方格任务数据接收器...")
    run_server()