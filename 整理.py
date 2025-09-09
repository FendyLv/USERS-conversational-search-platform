import json
import csv
from html import unescape

# 读取
with open('user.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 定义表头
headers = [
    'userId', 'completedAt', 'taskId', 'title', 'type', 'description',
    'answer', 'understanding', 'relevance', 'quality', 'responsiveness',
    'answerTime', 'ratingTime'
]

# 写入CSV
with open('user_sessions.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()

    for user in data:
        for task_key in ['task1', 'task2']:
            task = user[task_key]
            writer.writerow({
                'userId': user['userId'],
                'completedAt': user['completedAt'],
                'taskId': task['taskId'],
                'title': task['title'],
                'type': task['type'],
                'description': unescape(task['description']).replace('\n', ' ').strip(),
                'answer': task['answer'],
                'understanding': task['ratings']['understanding'],
                'relevance': task['ratings']['relevance'],
                'quality': task['ratings']['quality'],
                'responsiveness': task['ratings']['responsiveness'],
                'answerTime': task['answerTime'],
                'ratingTime': task['ratingTime']
            })