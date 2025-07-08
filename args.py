def calcul(**kwargs):
    print(f"kwargs is {kwargs}")
    if 'tool' in kwargs:
        return kwargs['tool'] * kwargs['ertefa']
    if 'shoa' in kwargs:
        return kwargs['shoa'] *3.14
    return 100

print(calcul(shoa=5))




'''
 اگر بخوایم به عنوان یه تاپل بهش پاس بدیم که نمیدونیم مثلا چنتا ممکن متغیر داشته باشه از **arg  استفاده میکنیم 
 اگر بخوایم به عنوان key  , value  پاسش بدیم و ازش به عنوان دیکشنری استفاده کنیم به همین صورتی که داخل تمرین گفته شده ازش استفاده میکنیم 
 
'''