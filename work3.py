# 高级自动邮件机器人
orders=[
    {'buyer':'pony','product':'macbook'},
    {'buyer':'bill','product':'airpods'},
    {'buyer':'hank', 'product':'iphone'},
    ]
def deliver_mail(buyer,product):
    print(f'Dear {buyer}:')
    print(f'Your purchased product:{product} is delivered!')
    print('Thanks for your choosing!')
for order in orders:
    buyer=order['buyer']
    product=order['product']
    deliver_mail(buyer,product)
# 小小数学家1
def auto_sum(max_num):
    min_num=0
    for i in range(1,max_num+1):
        min_num+=i
    return min_num
print(auto_sum(5))
# 小小数学家2
def out_even(max_num):
    lst=[]
    for i in range(1,max_num+1):
        if i%2==0:
            lst.append(i)
    return lst
print(out_even(8))