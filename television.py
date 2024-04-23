
class Television():
    MIN_VOLUME=0
    MAX_VOLUME=2
    MIN_CHANNEL=0
    MAX_CHANNEL=3

    def __init__(self)->None:
        '''
        Sets up status, muted, volume, and channel instance variables
        '''
        self.__status=False
        self.__muted=False
        self.__volume=Television.MIN_VOLUME
        self.__channel=Television.MIN_CHANNEL

    def power(self)->None:
        '''
        Switches power on and off
        '''
        if self.__status==False:
            self.__status=True
        else:
            self.__status=False

    def mute(self)->None:
        '''
        Switches mute on and off
        '''
        if self.__status == True:
            if self.__muted==False:
                self.__muted=True
            else:
                self.__muted=False

    def channel_up(self)->None:
        '''
        Increments channel up by one unless at max channel then sets to channel minimum
        '''
        if self.__status==True:
            if self.__channel!=Television.MAX_CHANNEL:
                self.__channel+=1
            else:
                self.__channel=Television.MIN_CHANNEL

    def channel_down(self)->None:
        '''
        Increments channel by -1 unless at channel min then set channel to channel max
        :return:
        '''
        if self.__status == True:
            if self.__channel!=Television.MIN_CHANNEL:
                self.__channel-=1
            else:
                self.__channel=Television.MAX_CHANNEL

    def volume_up(self)->None:
        '''
        unmutes tv and increases volume by one unless at volume max
        :return:
        '''
        if self.__status == True:
            self.__muted=False
            if self.__volume!=Television.MAX_VOLUME:
                self.__volume+=1

    def volume_down(self)->None:
        '''
        unmutes tv and decreases volume by one unless at volume min
        :return:
        '''
        if self.__status == True:
            self.__muted = False
            if self.__volume!=Television.MIN_VOLUME:
                self.__volume-=1

    def __str__(self)->str:
        '''
        prints Television objects as
                    Power = {self.status}, Channel = {self.channel}, Volume = {self.volume}.
        :return:
        '''
        if self.__muted==False:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}.'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}.'

