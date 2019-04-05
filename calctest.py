from tkinter import *
from tkinter import ttk
from tkinter import font


#ボタン押したときのコマンド
def keydown(names):
    def rkeydown():
        if names == "=":
            try:
                rnum.set(eval(rnum.get()))
            except SyntaxError:
                rnum.set("error")
            except NameError:
                rnum.set("error")
        elif names == "AC":
            rnum.set("")
        #文字列の一番右側の文字を削除 !要検証
        elif names == "EL":
            rnum.set(rnum.get().rstrip(rnum.get()[-1]))
        #+/-の切り替え
        elif names == "+/-":
            if rnum.get()[0] == "-":
                rnum.set(rnum.get().lstrip(rnum.get()[0]))
            else:
                rnum.set("-" + rnum.get())
        #数値を100倍して%表記．float()できなかったときはpass
        elif names == "%":
            try:
                rnum.set(float(rnum.get())*100)
            except ValueError:
                pass
        #押したキーを文字列として表示
        else:
            rnum.set(rnum.get() + names)
            
    return rkeydown

#メインウインドウの設定　サイズを250x350に，タイトルを四則演算に
root = Tk()
root.geometry("250x350")
root.title("四則演算")

#フォント設定
winfont = font.Font(family='Bahnschrift Condensed', size=18)
keyfont = font.Font(family="Bahnschrift Light",size=25)

#スタイルの設定　
style = ttk.Style()
style.configure("TLabel",font=winfont,background="black",foreground="white")


#フレームと計算窓の作成　
content = ttk.Frame(root,width=250,height=350)
winframe = ttk.Frame(content,borderwidth=1,relief="sunken")
keyframe = ttk.Frame(content,borderwidth=5,relief="sunken")

rnum = StringVar()
inum = StringVar()
sym = StringVar()

calcwindow = ttk.Entry(winframe,textvariable=rnum,font=winfont)

stlist = (N,S,E,W)

#gridの設定　
content.grid(column=0,row=0,sticky=stlist)
winframe.grid(column=0,row=0,columnspan=3,rowspan=2,padx=5,pady=5,sticky=stlist)
calcwindow.grid(column=0,row=0,columnspan=3,rowspan=2,sticky=stlist)
keyframe.grid(column=0,row=2,columnspan=3,sticky=stlist,padx=5,pady=5)

#全キーの生成,配置　
keys = []
keynames = [("AC","+/-","%","/"),
            ("9","8","7","*"),
            ("6","5","4","-"),
            ("3","2","1","+"),
            ("EL","0",".","=")]

i = 0
for y,row in enumerate(keynames,1):
    for x,names in enumerate(row):
        #ボタンのテキストにkeyname中の文字列を設定，さらにkeydown関数に引数としてnamesを与えたものをコマンドとして設定
        keys.append(ttk.Button(keyframe,text=names,command=keydown(names)))
        keys[i].grid(column=x,row=y,sticky=stlist)
        i += 1


#configure(サイズ関係)の設定
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)

content.columnconfigure(0,weight=3)
content.columnconfigure(1,weight=3)
content.rowconfigure(1,weight=1)
content.rowconfigure(2,weight=5)

winframe.columnconfigure(1,weight=1)
winframe.rowconfigure(0,weight=2)

for y in range(1,6):
    keyframe.rowconfigure(y,weight=3)

for x in range(0,3):
    keyframe.columnconfigure(x,weight=3)

root.mainloop()
