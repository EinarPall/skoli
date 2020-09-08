heildarstig=0
for i in range(1,6):
    player=input('Nafn leikmanns? ')
    stats=input('Tölfræði leikmannsins á forminu pts,reb,ast,stl,blk (t.d. 20,05,08,02,03): ')
    pts=int(stats[0]+stats[1])
    reb=2*int(stats[3]+stats[4])
    ast=3*int(stats[6]+stats[7])
    stl=4*int(stats[9]+stats[10])
    blk=4*int(stats[12]+stats[13])
    stig=pts+reb+ast+stl+blk
    heildarstig=heildarstig+stig
    print(player, 'er með', stig, 'í þessari umferð')
print('Heildar stigafjöldi þinn í þessari umferð er:', heildarstig)


