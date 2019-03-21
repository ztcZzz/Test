try:
    f = open('hhh.txt',encoding='utf-8')
    print(f,read())
    f.close()
except OSError as reason:
    print('文件出错了' + str(reason))
