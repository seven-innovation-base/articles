# ⚡演讲顺序安排

import random
import time

speakers_list = ['叶汕', '刘思志', '陈展熹', '张鹏礼', '吕少梅', '农林舒甄', '大数据', '董宇晨', '王俊杰']

head_count = 9
results = []

order = 0

while head_count:
    result = random.sample(speakers_list, 1)
    if result in results:
        result = random.sample(speakers_list, 1)
        continue
    order = order + 1
    results.append(result)
    print(f'第{order}位：,{result}')
    time.sleep(1)
    head_count = head_count - 1

print('done !')