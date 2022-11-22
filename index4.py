keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dic = {}
for k in keys:
    for v in values:
        dic[k] = v
        values.remove(v)
        break
print(dic)
