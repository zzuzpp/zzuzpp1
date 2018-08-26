#每日读取金山词霸的每日一句，英文和翻译，并保存到OneDayOneWord.txt文件
#number_start.txt文件记录程序运行次数，初次使用建议打开该文件，将文本修改为0。
#Autor:zpp
#Email:zhoupp@wipm.ac.cn
import requests
import time
 
def get_news():
    """获取金山词霸每日一句，英文和翻译"""
    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url)
    content = r.json()['content']
    note = r.json()['note']
    return content,note

def day_num():
    """记录时间"""
    #old_time_Y = time.strftime('%Y',time.localtime(time.time()))
    old_time_Y = 2018
    #old_time_m = time.strftime('%m',time.localtime(time.time()))
    old_time_m = 8
    #old_time_d = time.strftime('%d',time.localtime(time.time()))
    old_time_d = 22
    new_time_Y = time.strftime('%Y',time.localtime(time.time()))
    new_time_Y = int(new_time_Y)
    new_time_m = time.strftime('%m',time.localtime(time.time()))
    new_time_m = int(new_time_m)
    new_time_d = time.strftime('%d',time.localtime(time.time()))
    new_time_d = int(new_time_d)
    if new_time_Y == new_time_Y:
        if new_time_m == old_time_m:
            Rd = new_time_d - old_time_d
            R = Rd
        else:
            for i in range(new_time_m - old_time_m):
                R_time = old_time_m +i
                if R_time == 2:
                    Rm = 29 -old_time_d
                elif R_time in (1,3,5,7,8,10,11):
                    Rm = 31 - old_time_d
                else:
                    Rm = 30 - old_time_d
                R = Rm +new_time_d
    else:
        RY = (new_time_Y -old_time_Y)*365
        Rd = new_time_d - old_time_d
        for i in range(new_time_m - old_time_m):
                R_time = old_time_m +i
                if R_time == 2:
                    Rm = 29 -old_time_d
                elif R_time in (1,3,5,7,8,10,11):
                    Rm = 31 - old_time_d
                else:
                    Rm = 30 - old_time_d
                R = Rm +new_time_d
        R = RY +Rm +Rd
    return  R

def oper_num():
    """记录程序运行的次数"""
    
def record_news():
    file_news = open("D:\\python_o1_project\OneDayOneWord.txt",'a+')
    contents = get_news()
    file_news.write('\n')
    day_numer = str(day_num())
    file_news.write("第"+day_numer+"天")
    file_news.write('\n')
    file_news.write(contents[0])
    file_news.write('\n')
    file_news.write(contents[1])
    file_news.write('\n')
    file_news.write(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    file_news.close()
    
if __name__ == "__main__":
    record_news()
