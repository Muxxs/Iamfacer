#coding=utf-8
from flask import Flask,render_template,request
app = Flask(__name__)
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import uniout,time


def get_text():
    content=open("text.txt")
    content=str(content.read())
    content_list=content.split("=====*=====")
    text=[]
    for i in content_list:
        title=i.split("===*")[0].split("***")[-2]
        content=i.split("===*")[1].split("||")
        content_title=title,content
        text.append(content_title)
    return text
all_content=get_text()
print all_content[0]

@app.route('/restart')
def restart():
    content = open("text.txt")
    content = str(content.read())
    content_list = content.split("=====*=====")
    text = []
    for i in content_list:
        title = i.split("===*")[0].split("***")[-2]
        content = i.split("===*")[1].split("||")
        content_title = title, content
        text.append(content_title)
    return text
all_content = get_text()

@app.route('/go',methods=['GET'])
def GO():
    name=request.args.get('name')
    ip = request.remote_addr
    print name,ip
    if 1==1:
        read_config=open("config.txt","rb")
        config=open("config.txt","a+")
        if read_config.read().find(ip) == -1 :
            config.write("\n"+name+","+ip+","+time.asctime( time.localtime(time.time()) ))
            config.close()
            return render_template('404.html', text="投票成功！")
        else:
            return render_template('404.html', text="Sorry!你已经投过票了")
    else:
        return render_template('404.html', text="Sorry,It's Wrong")

@app.route('/')
def shou_all():
    all_content = get_text()
    return render_template('main.html', users=all_content)

@app.route('/all')
def show():
    all_content = get_text()
    read_config = open("config.txt", "rb").read()
    name_num=[]
    for i in all_content:
        name=i[0]
        num=read_config.count(name)
        con=name,num
        name_num.append(con)
    name_num.sort(key=lambda num:num[1],reverse=True)
    print name_num
    return render_template('all.html', content=name_num,time=time.asctime( time.localtime(time.time()) ))


@app.route('/<face>')
def show_text(face):
    global all_content
    for i in all_content:
        title=i[0]
        if title==face:
            content = i[1]
            return render_template('face.html', title=title, content=content)
    return render_template('404.html', text="Sorry,It's Wrong")

def hello_world():
    return 'Hello World!'

app.run(host='0.0.0.0',port=3002)