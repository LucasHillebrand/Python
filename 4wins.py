import lib as lib
show=lib.fw.vargen()
Game=1
player=1
while Game == 1:
    lib.fw.show(show)
    show=lib.fw.setcoin(input(lib.fw.test(player)+"[1-7]:"), show, player)
    if show[7] != -1:
        if(lib.fw.ChWin(show, player)):
            lib.fw.show(show)
            print(lib.fw.test(player)+" has win")
            input("pls press enter:")
            Game=0
        player=lib.fw.ChPlayer(player)