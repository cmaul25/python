
class Television():
    MIN_VOLUME=0
    MAX_VOLUME=2
    MIN_CHANNEL=0
    MAX_CHANNEL=3

    def __init__(self):
        self.status=False
        self.muted=False
        self.volume=Television.MIN_VOLUME
        self.channel=Television.MIN_CHANNEL

    def power(self):
        if self.status==False:
            self.status=True
        else:
            self.status=False

    def mute(self):
        if self.status == True:
            if self.muted==False:
                self.muted=True
            else:
                self.muted=False

    def channel_up(self):
        if self.status==True:
            if self.channel!=Television.MAX_CHANNEL:
                self.channel+=1
            else:
                self.channel=Television.MIN_CHANNEL

    def channel_down(self):
        if self.status == True:
            if self.channel!=Television.MIN_CHANNEL:
                self.channel-=1
            else:
                self.channel=Television.MAX_CHANNEL

    def volume_up(self):
        if self.status == True:
            self.muted==False
            if self.volume!=Television.MAX_CHANNEL:
                self.volume+=1

    def volume_down(self):
        if self.status == True:
            self.muted == False
            if self.volume!=Television.MIN_CHANNEL:
                self.volume-=1