class ttt:
    def show(A):
        print(str(ttt.test(A[0]))+str("|")+str(ttt.test(A[1]))+str("|")+str(ttt.test(A[2])))
        print(str(ttt.test(A[3]))+str("|")+str(ttt.test(A[4]))+str("|")+str(ttt.test(A[5])))
        print(str(ttt.test(A[6]))+str("|")+str(ttt.test(A[7]))+str("|")+str(ttt.test(A[8])))
    def loadnew():
        return [0, 0, 0, 0, 0, 0, 0, 0, 0]
    def test(I):
        if (I == 0):
            return " "
        elif (I == 1):
            return "X"
        elif (I == 2):
            return "O"
        else:
            return "!"
    def ChPlayer(P):
        if (P == 1):
            return 2
        elif (P == 2):
            return 1
    def ChWin(I, P):
        if (I[0] != 0 and I[1] != 0 and I[2] != 0 and I[3] != 0 and I[4] != 0 and I[5] != 0 and I[6] != 0 and I[7] != 0 and I[8] != 0):
            return ["nobody", 1]

        elif (I[0] == P and I[1] == P and I[2] == P):
            return [ttt.test(P), 1]
        elif (I[3] == P and I[4] == P and I[5] == P):
            return [ttt.test(P), 1]
        elif (I[6] == P and I[7] == P and I[8] == P):
            return [ttt.test(P), 1]

        elif (I[0] == P and I[3] == P and I[6] == P):
            return [ttt.test(P), 1]
        elif (I[1] == P and I[4] == P and I[7] == P):
            return [ttt.test(P), 1]
        elif (I[2] == P and I[5] == P and I[8] == P):
            return [ttt.test(P), 1]

        elif (I[0] == P and I[4] == P and I[8] == P):
            return [ttt.test(P), 1]
        elif (I[6] == P and I[4] == P and I[2] == P):
            return [ttt.test(P), 1]

        else:
            return [0, 0]
class fw:
    def vargen():
        return [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], 0]
    def test(I):
        if I == 0:
            return " "
        elif I == 1:
            return "X"
        elif I == 2:
            return "0"
        else:
            return "!"
    def show(I):
        print(fw.test(I[0][5])+"|"+fw.test(I[1][5])+"|"+fw.test(I[2][5])+"|"+fw.test(I[3][5])+"|"+fw.test(I[4][5])+"|"+fw.test(I[5][5])+"|"+fw.test(I[6][5]))
        print(fw.test(I[0][4])+"|"+fw.test(I[1][4])+"|"+fw.test(I[2][4])+"|"+fw.test(I[3][4])+"|"+fw.test(I[4][4])+"|"+fw.test(I[5][4])+"|"+fw.test(I[6][4]))
        print(fw.test(I[0][3])+"|"+fw.test(I[1][3])+"|"+fw.test(I[2][3])+"|"+fw.test(I[3][3])+"|"+fw.test(I[4][3])+"|"+fw.test(I[5][3])+"|"+fw.test(I[6][3]))
        print(fw.test(I[0][2])+"|"+fw.test(I[1][2])+"|"+fw.test(I[2][2])+"|"+fw.test(I[3][2])+"|"+fw.test(I[4][2])+"|"+fw.test(I[5][2])+"|"+fw.test(I[6][2]))
        print(fw.test(I[0][1])+"|"+fw.test(I[1][1])+"|"+fw.test(I[2][1])+"|"+fw.test(I[3][1])+"|"+fw.test(I[4][1])+"|"+fw.test(I[5][1])+"|"+fw.test(I[6][1]))
        print(fw.test(I[0][0])+"|"+fw.test(I[1][0])+"|"+fw.test(I[2][0])+"|"+fw.test(I[3][0])+"|"+fw.test(I[4][0])+"|"+fw.test(I[5][0])+"|"+fw.test(I[6][0]))
        print("1|2|3|4|5|6|7")
    def setcoin(I, show, p):
        if I != None:
            I=int(I)-1
            V=1
            tmp=0
            while V == 1:
                if show[I][tmp] == 0:
                    V=0
                    show[I][tmp] = p
                    show[7] = [tmp, I]
                    return show
                elif tmp == 5:
                    show[7] = -1
                    return show
                    V=0
                else:
                    tmp=tmp+1
            else:
                show[7] = -1
                return show
    def ChPlayer(I):
        if I == 1:
            return 2
        elif I == 2:
            return 1
        else:
            return 3
    def ChWin(show, p):
       False