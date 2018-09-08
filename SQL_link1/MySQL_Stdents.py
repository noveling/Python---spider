import tkinter
# import datetime
# import threading
# import time
import tkinter.ttk
import tkinter.messagebox
import pymysql
# class App:
#
#     def __init__(self,master):
#         self.frame = tkinter.Frame(master)
#         self.frame.pack()
#         self.button = tkinter.Button(self.frame,text = 'hrllo world',command = self.frame.quit,fg = 'pink')
#         self.button.pack()
#
#         self.hiButton = tkinter.Button(self.frame,text = 'Say hi!',fg = 'yellow',command = self.say_hi)
#         self.hiButton.pack()
#
#     def say_hi(self):
#         print('hello world!')

# class Time:
#
#     def __init__(self,master):
#         self.app = tkinter.Toplevel(master)
#         self.app.overrideredirect(True)
#         self.app.attributes('-alpha', 0.9)
#         self.app.attributes('-topmost', 1)
#         self.app.geometry('130x25+0+0')
#         self.labelDateTime = tkinter.Label(self.app, width=130)
#         self.labelDateTime.pack(fill=tkinter.BOTH, expand=tkinter.YES)
#         self.labelDateTime.configure(bg='green')
#
#         self.X = tkinter.IntVar(value=0)
#         self.Y = tkinter.IntVar(value=0)
#         self.canMove = tkinter.IntVar(value=0)
#         self.still = tkinter.IntVar(value=1)
#         self.labelDateTime.bind('<ButtonRelease-1>', self.onLeftButtonDown)
#         self.labelDateTime.bind("<ButtonRelease-1>", self.onLeftButtonUp)
#         self.labelDateTime.bind('<B1-Motion>', self.onLeftButtonMove)
#         self.labelDateTime.bind('<Button-3>', self.onRightButtonDown)
#
#         self.t = threading.Thread(target=self.nowDateTime)
#         self.t.daemon = True
#         self.t.start()

    # def onLeftButtonDown(self,event):
    #     self.canMove.set(1)


    # def onLeftButtonUp(self,event):
    #     self.app.attributes("-alpha", 0.9)
    #     self.canMove.set(0)
    #
    #
    #
    # def onLeftButtonMove(self,event):
    #     if self.canMove.get() == 1:
    #         return
    #     self.app.attributes("-alpha", 0.7)
    #     newX = self.app.winfo_x() + (event.x - self.X.get())
    #     newY = self.app.winfo_y() + (event.y - self.Y.get())
    #     g = '130x25+' + str(newX) + '+' + str(newY)
    #     self.app.geometry(g)
    #
    #
    #
    # def onRightButtonDown(self,event):
    #     self.still.set(0)
    #     self.t.join(0.2)
    #     self.app.destroy()  # 关闭窗口
    #
    #
    #
    # def nowDateTime(self):
    #     while self.still.get() == 1:
    #         s = str(datetime.datetime.now())[:19]
    #         self.labelDateTime['text'] = s
    #         time.sleep(0.2)
    #

class login:
    def __init__(self,master):
        self.app_login = tkinter.Frame(master)
        self.app_login.pack()
        self.app_login["height"] = 300
        self.app_login["width"] = 190


class tk_student:
    def __init__(self,master):
        self.app_student = tkinter.Frame(master)
        self.app_student.pack()
        self.app_student['height'] = 600
        self.app_student['width'] = 500


        self.id_Selector = tkinter.StringVar(master,value = "")

        self.var_id = tkinter.StringVar(master,value="1")

        self.varName = tkinter.StringVar(master, value='路明非')
        self.entryName = tkinter.Entry(master,
                                  textvariable=self.varName)

        self.entryName.place(x=70, y=5,width = 160, height=30)

        self.labelGrade = tkinter.Label(master, text='Grade', justify=tkinter.RIGHT, width=50, bg="yellow")
        self.labelGrade.place(x=0, y=40, width=50, height=30)

        self.labelClass = tkinter.Label(master, text='Class', justify=tkinter.RIGHT, width=50, bg='yellow')
        self.labelClass.place(x=130, y=40, width=50, height=30)

        self.labelName = tkinter.Label(master, text='Name', justify=tkinter.RIGHT,
                                       width=50, bg="yellow")
        self.labelName.place(x=0, y=5, width=50, height=30)
        self.entry_Select_Name = tkinter.Entry(master, width=120,
                                               textvariable=self.id_Selector)
        self.entry_Select_Name.place(x=90, y=400, width=70, height=30)

        self.Select_id = tkinter.Label(master, text='id selector', justify=tkinter.RIGHT,
                                         width = 90,bg="yellow")
        self.Select_id.place(x=0, y=400, width=80, height=30)
        # 列表框
        self.listboxStudents = tkinter.Listbox(master, width=400)
        self.listboxStudents.place(x=10, y=170, width=480, height=220)

        # 模拟班级信息
        self.studentClasses = {'1': ['1', '2', '3'], '2': ['1', '2'], '3': ['1']}

        self.comboGrade = tkinter.ttk.Combobox(master, width=50, values=tuple(self.studentClasses.keys()))
        self.comboGrade.place(x=70, y=40, width=50, height=30)

        self.comboClass = tkinter.ttk.Combobox(master, width=50)
        self.comboClass.place(x=200, y=40, width=50, height=30)

        self.comboClass.bind('<Button-1>', self.comboChange)

        self.labelSex = tkinter.Label(root, text='Sex', justify=tkinter.RIGHT,
                                 width=50, bg='yellow')
        self.labelSex.place(x=0, y=75, width=50, height=30)
        self.buttonAdd = tkinter.Button(master, text='Add', width=10, command=self.addInformation)

        self.buttonAdd.place(x=45, y=140)

        self.buttonDelete = tkinter.Button(root, text='Delete', width=10, command=self.deleteSelection)

        self.buttonDelete.place(x=190, y=140)

        self.buttonDeletebyid = tkinter.Button(master,text="Delete info by id",width=10,command=self.deletebyid)
        self.buttonDeletebyid.place(x=360,y=400,width = 120)

        self.buttonCheck = tkinter.Button(master,text='Check',width=10,command = self.checkSelection)
        self.buttonCheck.place(x=250,y=400)

#查询结果
        self.res = tkinter.StringVar
        self.Check_res = tkinter.Text(root)
        self.Check_res.place(x=20,y=450,width = 400,height=30)

        self.Sex = [('man', 0), ('woman', 1)]

        self.v = tkinter.IntVar(root, value=0)
        self.v.set(0)
        self.monitor = tkinter.IntVar(root, value=0)
        self.id_ask = tkinter.Label(master,text="id:",justify=tkinter.RIGHT,bg="yellow")
        self.id_ask.place(x=0,y=110,width=50,height=30)
        self.id_info = tkinter.Entry(master,
                                  textvariable=self.var_id)
        self.id_info.place(x=90, y=110)


        for sex, num in self.Sex:
            radioSex = tkinter.Radiobutton(root, text=sex, variable=self.v, value=num)
            radioSex.place(x=len(sex) * 35, y=75)

    def deletebyid(self):
        try:
            db = pymysql.connect(host='localhost', user='root', db='bysj1', charset="utf8")
            cur = db.cursor()
            print("连接成功")

        except pymysql.Error as e:
            print(e)
            exit(1)

        try:
            if cur.execute("DELETE FROM students WHERE id = '%s'" % (self.id_Selector.get())):
                print("删除成功")
                self.Check_res.delete(0.0, tkinter.END)
                self.Check_res.see(tkinter.END)
                self.Check_res.update()
                tkinter.messagebox.showinfo('提示!', '成功删除!')
                db.commit()
            else:
                print("删除失败")
                tkinter.messagebox.showinfo('提示!', '删除失败!')
        except:
            print("数据库操作有误")

        if db:
            if cur:
                cur.close()
            db.close()
            print("关闭sql")

    def checkSelection(self):
        # pass
        try:
            db = pymysql.connect(host='localhost', user='root', db='bysj1',charset="utf8")
            cur = db.cursor()
            print("连接成功")

        except pymysql.Error as e:
            print(e)
            exit(1)

        try:
            if cur.execute("SELECT * FROM students WHERE id = '%s'"%(self.id_Selector.get())):
                print("查询成功")
                res=cur.fetchone()
                print(res)
                self.Check_res.delete(0.0,tkinter.END)
                self.Check_res.insert\
                    (tkinter.END,"id:"+res[0]+" 性别:"+res[1]+" 姓名:"+res[2]+" 班级信息:"+res[3])
                self.Check_res.see(tkinter.END)
                self.Check_res.update()
            else:
                self.Check_res.delete(0.0, tkinter.END)
                self.Check_res.see(tkinter.END)
                self.Check_res.update()
                tkinter.messagebox.showinfo('提示!', '查询失败!')
                print("查询失败")
        except:
            print("数据库操作有误")


        if db:
            if cur:
                cur.close()
            db.close()
            print("关闭sql")


    def deleteSelection(self):
        # 获取当前选项

        selection = self.listboxStudents.curselection()
        if not selection:
            self.Check_res.delete(0.0, tkinter.END)
            self.Check_res.see(tkinter.END)
            self.Check_res.update()
            tkinter.messagebox.showinfo('提示!', '没有获取选择')
        else:
            self.listboxStudents.delete(selection)

    # def deleteMySqldata(self,name):
    #
    #     try:
    #         db = pymysql.connect(host='localhost', user='root', db='bysj',charset="utf8")
    #         cur = db.cursor()
    #         print("连接成功")
    #
    #     except pymysql.Error as e:
    #         print(e)
    #         exit(1)
    #
    #     delete_order = "DELETE FROM students WHERE name = " + name
    #     cur.execute(delete_order)



    def comboChange(self, event):
        # 获取年级选择项
        grade = self.comboGrade.get()
        if grade:
            self.comboClass['values'] = self.studentClasses.get(grade)

        else:
            self.comboClass.set('')

    def addInformation(self):
        try:
            db = pymysql.connect(host='localhost', user='root', db='bysj1',charset="utf8")
            cur = db.cursor()
            print("连接成功")

        except pymysql.Error as e:
            print(e)
            exit(1)




        name = str(self.entryName.get())
        grade = self.comboGrade.get()
        classSelected = self.comboClass.get()
        id = str(self.var_id.get())
        if not (name.strip() and grade and classSelected and id.strip()):
            tkinter.messagebox.showerror("警告！", message="信息不完整!!!")
            return
        else:
            sex_res = 'Man' if self.v.get() == 0 else 'Woman'
            result = ' '.join(['Name:', name, 'Grade:', grade, 'Class:', classSelected])
            result = ' '.join([result, 'Sex:', sex_res, 'Id:',
                               id])
            self.listboxStudents.insert(0, result)
            self.varName.set('')
            self.var_id.set('')

        try:
            cur.execute("CREATE TABLE Students(id varchar(11) PRIMARY KEY,"
                        "sex varchar(11),name varchar(11),class varchar(22))")
            print("建表。。。")
        except:
            print("存在表")
        try:
            if cur.execute("INSERT INTO Students(id,name,sex,class) "
                           "values ('%s','%s','%s','grade:%s,class:%s')"%(id,name,sex_res,str(grade),str(classSelected))):
                tkinter.messagebox.showinfo("成功！", message="成功添加！")
                db.commit()
            else:
                tkinter.messagebox.showinfo("错误！", message="无法添加！")
                print("插入失败")
        except:
            tkinter.messagebox.showinfo("错误！", message="无法添加！")
            print("数据库操作错误")

        if db:
            if cur:
                cur.close()
            db.close()
            print("关闭sql")


if __name__ == "__main__":

    root = tkinter.Tk()
    root.config(width = 400,height = 900)
    root.title('学生信息管理系统')
    # win = App(root)
    student_tk = tk_student(root)
    root.mainloop()
