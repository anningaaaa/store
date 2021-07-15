import re
def mail_log(file_path):
  global count
  log=open(file_path,'r')
  C=r'\.'.join([r'\d{1,3}']*4)
  find=re.compile(C)
  count={}
  for i in log:
    for ip in find.findall(i):
      count[ip]=count.get(ip,0)+1
if __name__ == '__main__':
  num=0
  mail_log(r'D:\pythonProject\day15\baidu_x_system.log')
  R=count.items()
  for i in R:
    if i[1]>0: #提取出现次数大于0的IP
      print(i)
      num+=1