f = open('record.txt',encoding='utf-8')

boy = []
girl = []
count = 1

for each_line in f:
    #这里进行分割字符串操作
    if each_line[:4] != '====':
        (role,line_spoken) = each_line.split(':',1)
        if role == '小甲鱼':
            boy.append(line_spoken)
        if role == '小客服':
            girl.append(line_spoken)
    
    else:
    #文件的分别保存操作
        file_name_boy = 'boy_' + str(count) + '.txt'
        file_name_girl = 'girl_' + str(count) + '.txt'

        boy_file = open(file_name_boy,'w')
        girl_file = open(file_name_girl,'w')

        boy_file.writelines(boy)
        girl_file.writelines(girl)

        boy_file.close()
        girl_file.close()
        
        boy = []
        girl = []
        count += 1


file_name_boy = 'boy_' + str(count) + '.txt'
file_name_girl = 'girl_' + str(count) + '.txt'

boy_file = open(file_name_boy,'w')
girl_file = open(file_name_girl,'w')

boy_file.writelines(boy)
girl_file.writelines(girl)

boy_file.close()
girl_file.close()

boy = []
girl = []
count += 1
f.close()
