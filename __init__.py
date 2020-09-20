def say():
    print()

def ip():
    input()

def jian():
    import time
    time.ctime ()

def weather():
   # -*- coding: 'utf-8' -*-

   import requests
   import time

   while True:
       city = input('请输入城市:\n')
       if not city:
           break

       try:
          req = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=%s' % city)
       except:
             print ('查询失败')
             break

       # print(req.text)
       dic_city = req.json() # 转换为字典
       # print(dic_city)

       city_data = dic_city.get('data')  # 没有’data‘的话返回 None
    
       if city_data:
           city_forecast = city_data['forecast'][0] # 下面的都可以换成'get'方法
           print(city_forecast.get('date'))
           print(city_forecast.get('high'))
           print(city_forecast.get('low'))
           print(city_forecast.get('type'))
       else:
           print('未获得')

def canshu():
    # coding: gbk
    print('请在下方输入游戏范围')
    fangwe = int(input())
    from random import randint
    num = randint(1,fangwe)
    print('猜猜这个数是几?（不想玩了回-1)')
    bingo = False
    count = 0

    while bingo == False:
        count +=1
        answer = int(input())
        num1 = 10+num
        x = randint(1,10)
        y = randint(1,10)
        z = randint(1,10)

        if answer<num:
            print(str(answer) + '太小了!')
            num = num+x
        
        if answer>num:
            print(str(answer) + '太大了')
            num = num+y
   
        if answer==num1:
            print(str(answer) + '接近了')
            num = num+z
            count==count-1
        
        if answer==-1:
            print(str(num) +  '是正确的答案,游戏失败')
            bingo = True

        if count==100:
            print('游戏失败')
            bingo = True
        
        if answer==num:
           print('答对了,'+ str(answer) +' 是正确的答案')
           bingo = True

    print(count)




 

