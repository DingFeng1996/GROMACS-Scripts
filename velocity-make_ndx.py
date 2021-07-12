import os
import linecache


#建立工作文件夹
os.system('mkdir group')

#gmx选择分组
x1=7
x2=6.8
num=1
while x2>0:
  var='gmx select -f ../10ns.pdb -s ../pull.tpr -on group/{}.ndx -select \"resname SOL and z>10 and z<12 and y>{:.2f} and y<{:.2f}\"'.format(num,x2,x1)  #生成目录group
  os.system(var)
  x1=x1-0.6
  x2=x2-0.6
  num+=1
print("End!")

#合并分组索引
 
def combine_file():
 
    # 读取指定路径下的所有文件并放入到列表group中
    root = 'group'
    file_names = os.listdir(root)
    print(file_names)
    file_ob_list = []
    for file_name in file_names:
        fileob = root + '/' + file_name
        file_ob_list.append(fileob)
    print(file_ob_list)
 
    # 对每个文件，按行读取文件内容并放入同一个列表data中
    data = []
    for file_ob in file_ob_list:
        line_num = 1
        length_file = len(open(file_ob, encoding='utf-8').readlines())
        print(length_file)
        while line_num <= length_file:
            line = linecache.getline(file_ob, line_num)
            line = line.strip()
            data.append(line)
            line_num = line_num + 1
 
    # 将data内容写入到生成的索引文件中
    f = open('./combine.ndx', 'w+', encoding='utf-8')
    for i, p in enumerate(data):
        print(i, p)
        f.write(p+'\n')
    f.close()
 
 
combine_file()
