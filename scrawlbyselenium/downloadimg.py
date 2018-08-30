from urllib import request
import os


# path为要保存图片的文件夹
def downloadByHttp(url,path="./img/"):
    os.chdir(".")
    if not os.path.exists("./img"):
        os.mkdir("./img")
    # 截取文件名，避免文件名过长只截取最后20位
    fileName = url.split("/")[-1:][0][-20:]
    # 获取文件参数
    conn = request.urlopen(url)
    # 获取文件后缀名
    sub = conn.headers['Content-Type'].split("/")[-1:][0]
    print('sss:',sub)
    conn.close()
    # 如果这个超链接不包含后缀名，则加上一个后缀名
    if fileName.find(".") == -1:
        fileName = fileName+'.'+sub
    print(fileName)
    print("downloading with urlretrieve")
    request.urlretrieve(url, path+fileName)

if __name__ == "__main__":
    downloadByHttp('http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%CD%BC%C6%AC&fr=ala&ala=1&alatpl=others&pos=0')
