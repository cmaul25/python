
class Television():
    MIN_VOLUME=0
    MAX_VOLUME=2
    MIN_CHANNEL=0
    MAX_CHANNEL=3

    def __init__(self)->None:
        '''
        Sets up status, muted, volume, and channel instance variables
        '''
        self.status=False
        self.muted=False
        self.volume=Television.MIN_VOLUME
        self.channel=Television.MIN_CHANNEL

    def power(self)->None:
        '''
        Switches power on and off
        '''
        if self.status==False:
            self.status=True
        else:
            self.status=False

    def mute(self)->None:
        '''
        Switches mute on and off
        '''
        if self.status == True:
            if self.muted==False:
                self.muted=True
            else:
                self.muted=False

    def channel_up(self)->None:
        '''
        Increments channel up by one unless at max channel then sets to channel minimum
        '''
        if self.status==True:
            if self.channel!=Television.MAX_CHANNEL:
                self.channel+=1
            else:
                self.channel=Television.MIN_CHANNEL

    def channel_down(self)->None:
        '''
        Increments channel by -1 unless at channel min then set channel to channel max
        :return:
        '''
        if self.status == True:
            if self.channel!=Television.MIN_CHANNEL:
                self.channel-=1
            else:
                self.channel=Television.MAX_CHANNEL

    def volume_up(self)->None:
        '''
        unmutes tv and increases volume by one unless at volume max
        :return:
        '''
        if self.status == True:
            self.muted=False
            if self.volume!=Television.MAX_VOLUME:
                self.volume+=1

    def volume_down(self)->None:
        '''
        unmutes tv and decreases volume by one unless at volume min
        :return:
        '''
        if self.status == True:
            self.muted = False
            if self.volume!=Television.MIN_VOLUME:
                self.volume-=1

    def __str__(self)->str:
        '''
        prints Television objects as
                    Power = {self.status}, Channel = {self.channel}, Volume = {self.volume}.
        :return:
        '''
        if self.muted==False:
            return f'Power = {self.status}, Channel = {self.channel}, Volume = {self.volume}.'
        else:
            return f'Power = {self.status}, Channel = {self.channel}, Volume = {Television.MIN_VOLUME}.'

