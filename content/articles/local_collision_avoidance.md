Title: 机器人局部蔽障
Date: Thu  7 Feb 18:48:59 CET 2019
Category: SLAM
Tags: SLAM

## 动态窗口法(Dynamic window approach)
* 根据运动模型，机器人参数，生成一个合理的搜索空间(search space）
* 根据评价函数，选取最后方案

动态窗口法主要是在速度(v,w)空间(线速度，角速度)中，采样多种速度可能性，并模拟
在一个固定时间sim_period内，机器人的轨迹，得到多组轨迹以后，对轨迹进行评价，
选取最优轨迹对应的速度来驱动机器人。
如何选取可行的二维速度空间，并且使之尽可能小，这样需要模拟的可能路径就少。
在DWA中，这个窗口的确定是根据机器人的加减速性能(kinematic constraint)

(程序每隔0.25秒运行一次，sim_period = 0.25s, 计算出在此时刻，根据不同的速度采样，sim_period以后各自不同的轨迹，选取其中最符合最优标准的速度，转换成机器人控制，完成一次的控制。然后等待下一个sim_period再进行同样的循环操作)

具体解释，可参考：机器人局部避障的动态窗口法(dynamic window approach)[^1]

## 动态窗口法缺点
http://ais.informatik.uni-freiburg.de/teaching/ss10/robotics/slides/16-pathplanning.pdf


[^1]: https://blog.csdn.net/heyijia0327/article/details/44983551


