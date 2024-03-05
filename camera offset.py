





#offset for camera not to also go off screen but not have to be
#stuck in center either

   def offset(self):
        MARGINX = 550
        MARGINY = 350
        self.cam = self.camera 
     
        
        if (self.cam.x + CW) - self.position.x > MARGINX:
        
            self.cam.x = (self.position.x + MARGINX - CW) 

        elif self.position.x - (self.cam.x + CW) > MARGINX:
            self.cam.x = (self.position.x - MARGINX - CW) 
        if (self.cam.y + CH) - self.position.y > MARGINY:
            self.cam.y = int(self.position.y + MARGINY - CH) 
        elif self.position.y - (self.cam.y + CH) > MARGINY:
            self.cam.y = int(self.position.y - MARGINY - CH)

    def offset2(self):
        mx = 400
        my = 200
        self.cam = self.camera 
     
        
        if (self.cam.x + CW) - self.position.x > mx:
        
            self.cam.x = (self.position.x + mx - CW) 

        elif self.position.x - (self.cam.x + CW) > mx:
            self.cam.x = (self.position.x - mx - CW) 
        if (self.cam.y + CH) - self.position.y > my:
            self.cam.y = int(self.position.y + my - CH) 
        elif self.position.y - (self.cam.y + CH) > my:
            self.cam.y = int(self.position.y - my - CH)

