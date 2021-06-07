from PIL import Image

tilesize = 11

board = [[True]*10]*10

board[5] = [True]*5+[False]+[True]*4

im = Image.new("1", (len(board)*tilesize+1,len(board[0])*tilesize+1))

px = im.load()

for i in range(len(board)*tilesize+1):
    for j in range(len(board[0])*tilesize+1):
        px[i,j] = 1-(1*(i%tilesize == 0)*(j%tilesize == 0)+1*(i%tilesize != 0)*(i%tilesize != 0)*((i*(-1+2*((i//tilesize+j//tilesize)%2 == 1)))%tilesize == j%tilesize)*(board[(i//tilesize)%len(board)][(j//tilesize)%len(board[0])]))

im.show()

print(board)
