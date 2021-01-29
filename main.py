import lib as lib
player=1
show=lib.ttt.loadnew()
Stop=0
while (Stop != "stop"):
    Game="true"
    while(Game == "true"):
        lib.ttt.show(show)
        I=str(input(lib.ttt.test(player)+":"))
        if (I == "stop"):
            Stop="stop"
            Game="false"
        if (I != "stop"):
            I=int(I)
            if (show[I-1] == 0):
                show[I-1]=(player)
                Win=lib.ttt.ChWin(show, player)
                player=lib.ttt.ChPlayer(player)
                if (Win[1] == 1):
                    lib.ttt.show(show)
                    print(str(Win[0]) + " has win")
                    input("pls press enter:")
                    Game = "false"
    show=lib.ttt.loadnew()