# -*-coding:utf-8-*-
# 计算小明一个月出勤费用
# 假设里程固定，仅计算轨道交通i
cost=0
for i in range(1,41):
    if cost<100:
        cost+=5
    elif 150>cost>=100:
        cost+=4
    elif 400>=cost>=150:
        cost+=2.5
    print(f"{cost}为小明这个月花费的通勤费用，次数：{i}")
































