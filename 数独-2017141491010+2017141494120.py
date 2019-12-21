import tkinter as tk

def isValidSudoku(board):   #判断Sudoku数据是否有效
    invalid_num=0
    for y in range(9):
        for x in range(9):
            if board[y][x] >9 or board[y][x] <0:
                board[y][x]=0
                invalid_num+=1
            if board[y][x] != 0:
                if board[y].count(board[y][x]) > 1: #同一行不可出现相同数字(0即未填时除外)
                    print("同一行不可出现相同数字")
                    return False

            for col in range(9):
                if board[y][x] != 0 and col != y:    
                    if board[col][x] == board[y][x]: #同一列不可出现相同数字(0即未填时除外)
                        print("同一列不可出现相同数字")
                        return False

            for i in range(3):
                for j in range(3):
                    if board[y][x] != 0 and (i+3*(y//3), j+3*(x//3)) != (y, x):
                        if board[i+3*(y//3)][j+3*(x//3)] == board[y][x]:  #同一块3x3区域内不可出现相同数字(0即未填时除外)
                            print("同一块3x3区域内不可出现相同数字")
                            return False
    if invalid_num>0:
        print('范围之外的数字已视为空值')
        print("请检查修改您的输入\n")            
    return True

def get_sudoku():
    window = tk.Tk()
    window.title('Solve a Sudoku')
    window.geometry('600x450')

    width = 3
    height = 1
    labels = []
    entrys = []
    sudoku = [[0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0]]

    for i in range(81):
        entrys.append(tk.Entry(window, width=width))   #初始化entrys
        labels.append(tk.Label(window, width=3, height=1, bg='yellow'))   #初始化labels

    l1 = tk.Label(window, text='数独解密器', bg='white', font=('微软雅黑',15))   #设计标题
    l1.place(x='230', y='15')
    b1 = tk.Button(window, text='点击解密', bg='white', font=('微软雅黑',12), command=lambda: get_data())   #设计按钮
    b1.place(x='240', y='370')
    l2 = tk.Label(window, text='2019.7计算生物学项目实践', bg='white', font=('微软雅黑',10))   #设计右下角标语
    l2.place(x='350', y='320')
    for e in entrys:
        e.place(x=str(entrys.index(e)%9*28+entrys.index(e)//3%3*6+20),
                y=str(entrys.index(e)//9*24+entrys.index(e)//27*6+70))   #GUI中用来将数独矩阵分割成9个九宫格

    def get_data(): #获取数独矩阵的值
        print("*******************************")
        invalid_value=0
        for e in entrys:
            e_get=e.get()
            if e_get.isdigit():
                sudoku[entrys.index(e)//9][entrys.index(e)%9] = int(e_get) 
            else:
                if e_get!='':
                    invalid_value+=1
                sudoku[entrys.index(e)//9][entrys.index(e)%9] = 0

        if isValidSudoku(sudoku):   #判断输入的Sudoku是否有效
            data = sudoku   #将输入的数独代入算法中计算
            data_list = data_list_filter(data, build_data_list(data), 0)   #针对Sudoku中的每一个空格子，都算出其可能的备选数字，存入data_list中;每当空格被确认唯一值时，剩余data_list都需要再被刷新
            newdata = fill_num(data, data_list, 0)   #计算得到完整数独newdata
            if invalid_value>0:
                print('非整数值的输入已视为空值')
                print("请检查修改您的输入\n")
            print("最终解得的数独答案(可能不唯一)如下：")
            print_sudoku(newdata)   #程序输出数独newdata
            print("*******************************")
            invalid_value=0
            for l in labels:
                labels[labels.index(l)]['text']= newdata[labels.index(l)//9][labels.index(l)%9]   #将完整数独的值代入label中
                l.place(x=str(labels.index(l)%9*28+labels.index(l)//3%3*6+300),
                        y=str(labels.index(l)//9*24+labels.index(l)//27*6+70))   #用labels将数独输出到GUI界面
        else:
            pass

    window.mainloop()

def print_sudoku(data): #打印最终数独破解结果
    for i in range(9):
        for j in range(9):
            print('{:^3}'.format(data[i][j]),end='')
        print('')

def build_data_list(data): #初始化，未每个空位建立备选数字列表data_list
    data_list = []
    for y in range(9):
        for x in range(9):
            if data[y][x] == 0:
                data_list.append([(x, y), [1, 2, 3, 4, 5, 6, 7, 8, 9]])
    return data_list

def judge(data, x, y, num): #关键函数一，判断数字是否重复，是否允许填入
    if data[y].count(num) > 0: #行判断
        #print('error1')
        return False
    for col in range(9): #列判断
        if data[col][x] == num:
            #print('error2')
            return False

    for a in range(3): #九宫格判断
        for b in range(3):
            if data[a+3*(y//3)][b+3*(x//3)] == num:
                #print('error3')
                return False
    return True

def data_list_filter(data, data_list, start):    #用来再次刷新备选数字
    for blank_index in range(start, len(data_list)):
        data_list[blank_index][1] = []
        for num in range(1,10):
            if judge(data, data_list[blank_index][0][0], data_list[blank_index][0][1], num):
                data_list[blank_index][1].append(num)
    return data_list

def fill_num(data, data_list, start):  #关键函数二，对具有多个备选数字的位置依次尝试。类似深度优先遍历算法，一旦某位置的数字judge为True，则允许开始下一位置的猜测；若某位置为False，则忽略。
    if start < len(data_list):
        one = data_list[start]
        for num in one[1]:
            if judge(data, one[0][0], one[0][1], num):
                data[one[0][1]][one[0][0]] = num
                tem_data = fill_num(data, data_list, start+1)
                if tem_data != None:
                    return tem_data
        data[one[0][1]][one[0][0]] = 0  #有可能再往后猜了好几步后才发现前面错误，此时需要将过程中的所有赋值操作清零。
    else:
        return data

def main(): #主函数
    print("请在框中输入0-9之间的整数(0视为空值),输入完毕后点击解密按钮")
    try:
        get_sudoku()
    except:
        print('Error occurred! please check your data~')

main()
