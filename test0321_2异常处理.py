try :
    f = open('我是谁.txt','w')
    print(f.write('我存在了！'))
    sum = 1+'1'
except(OSError,TypeError):
    print('出错了')
finally:
    f.close()
    
