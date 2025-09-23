from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import random

app = Flask(__name__)

# 生成任务分配结果
def generate_task_assignments(n_users):
    # 任务类型定义
    levels = ["评估类", "创造类"]
    aspects = ["生活", "学习", "工作"]

    # 生成两个独立的3阶拉丁方阵
    def generate_latin_square(n):
        base = np.array([np.roll(np.arange(1, n + 1), i) for i in range(n)])
        np.random.shuffle(base)
        return base[:, np.random.permutation(n)]

    latin_square_level = generate_latin_square(3)
    latin_square_aspect = generate_latin_square(3)

    # 创建任务池
    task_pool = {}
    task_id = 1
    for level in levels:
        for aspect in aspects:
            task_pool[task_id] = {
                "id": task_id,
                "level": level,
                "aspect": aspect,
                "name": f"{level}-{aspect}",
                "description": f"这是一个{aspect}方面的{level}问题，需要您通过与对话式AI的交互获取相应的信息和让您觉得充分满意的答案。"
            }
            task_id += 1

    # 为每个用户分配任务
    assignments = {}
    for user_idx in range(n_users):
        row_idx = user_idx % 3
        col_level = latin_square_level[row_idx, user_idx % 3] - 1
        col_aspect = latin_square_aspect[row_idx, user_idx % 3] - 1

        # 分配评估任务
        eval_aspect = aspects[col_aspect]
        eval_task = None
        for task_id, task in task_pool.items():
            if task["level"] == "评估类" and task["aspect"] == eval_aspect:
                eval_task = task
                break

        # 分配创造任务（不同方面）
        create_aspect = aspects[(col_aspect + 1) % 3]
        create_task = None
        for task_id, task in task_pool.items():
            if task["level"] == "创造类" and task["aspect"] == create_aspect:
                create_task = task
                break

        # 随机决定任务出现的顺序
        if random.random() < 0.5:  # 50%概率先评估后创造
            task_order = [eval_task, create_task]
            task_order_names = ["先评估后创造", "评估→创造"]
        else:  # 50%概率先创造后评估
            task_order = [create_task, eval_task]
            task_order_names = ["先创造后评估", "创造→评估"]

        assignments[user_idx + 1] = {
            "user_id": user_idx + 1,
            "tasks": task_order,
            "order": task_order_names[0],
            "order_symbol": task_order_names[1]
        }

    return assignments

# 全局存储任务分配结果
n_users = 200
task_assignments = generate_task_assignments(n_users)

@app.route('/')
def index():
    return render_template('tasks.html', n_users=n_users)

@app.route('/tasks', methods=['POST'])
def show_tasks():
    try:
        user_id = int(request.form['user_id'])
        if user_id < 1 or user_id > n_users:
            return render_template('error.html',
                                   message=f"用户ID必须在1-{n_users}之间")

        user_tasks = task_assignments.get(user_id)
        if not user_tasks:
            return render_template('error.html',
                                   message=f"找不到用户ID {user_id} 的任务")

        return render_template('tasks.html', user=user_tasks, n_users=n_users)
    except ValueError:
        return render_template('error.html',
                               message="请输入有效的数字ID")

if __name__ == '__main__':
    app.run(debug=True)
