class Grid():
    def __init__(self, rod=1, dalkur=1, x_rod=1, x_dalkur=1):
        self.rod=rod
        self.dalkur=dalkur
        self.x_rod=x_rod
        self.x_dalkur=x_dalkur 

    def __str__(self):
        self.hnitakerfi=''
        for i in range(self.rod):
            if i==self.x_rod-1:
                for j in range(self.dalkur):
                    if j==self.x_dalkur-1:
                        self.hnitakerfi+='x'
                    else:
                        self.hnitakerfi+='o'
            else:
                for j in range(self.dalkur):
                    self.hnitakerfi+='o'
            self.hnitakerfi+='\n'
        return self.hnitakerfi


    def current_pos(self):
        return (self.x_rod, self.x_dalkur)

    def move_right(self):
        if self.x_dalkur==self.dalkur:
            self.x_dalkur=1
        else:
            self.x_dalkur+=1
        

    def move_left(self):
        if self.x_dalkur==1:
            self.x_dalkur=self.dalkur
        else:
            self.x_dalkur-=1

    def move_up(self):
        if self.x_rod==1:
            self.x_rod=self.rod
        else:
            self.x_rod-=1

    def move_down(self):
        if self.x_rod==self.rod:
            self.x_rod=1
        else:
            self.x_rod+=1