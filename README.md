 USERS-conversational-search-platform <br>
用于对话式搜索的实验本地平台代码，内含拉丁方随机分配的任务六个，分为评估/创造、生活/学习/工作两个维度，用户通过跳转按钮“go AI"跳转至ChatGPT软件并在其帮助之下完成评估任务和创造任务各一个，完成后对AI的使用感受进行评分，平台会记录用户的id（自动生成下一个用户id+1）、输入数据、输入时间、评分数据、评分时间 <br>
app.py运行后可以点击链接进入平台，根据需要调整"go AI"的网址以达到跳转不同平台界面的效果
 backend.py将用户交互数据实时记录下来，需要在打开平台后同步打开以记录用户行为 <br>
*更新 评估类和创造类的任务出现先后顺序随机

Code for an experimental local platform for conversational search, containing six tasks randomly assigned using the Latin square method, divided into evaluation and Creativity, and the two dimensions of Life/Study/Work. Users click the “go AI” button to navigate to ChatGPT and, with its assistance, complete one evaluation task and one creativity task. After completion, they rate their experience with the AI. The platform records the user ID (automatically generated as the next user ID + 1), input data, input time, rating data, and rating time. <br>
After running app.py, you can click the link to access the platform. Adjust the “go AI” URL as needed to redirect to different platform interfaces.
backend.py records user interaction data in real time; it must be opened simultaneously with the platform to track user behavior <br>
*Update: The order in which evaluation and creative tasks appear is now randomized

