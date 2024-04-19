from television import *
import pytest

class Test():
    def setup_method(self):
        self.tv1=Television()
    def teardown_method(self):
        del self.tv1
    def test__init__(self):
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0.'

    def test_power(self):
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0.'
        self.tv1.power()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0.'
        self.tv1.power()

    def test_mute(self):
        # tv on, volume increased once, then muted
        self.tv1.power()
        self.tv1.volume_up()
        self.tv1.mute()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0.'
        #tv on and unmuted
        self.tv1.mute()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 1.'
        #tv off and muted
        self.tv1.mute()
        self.tv1.power()
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0.'
        #tv off and unmuted
        self.tv1.power()
        self.tv1.mute()
        self.tv1.power()
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 1.'
        self.tv1.power()
        self.tv1.volume_down()
        self.tv1.volume_down()
        self.tv1.power()
    def test_channel_up(self):
        #off and channel up one
        self.tv1.power()
        self.tv1.channel_up()
        self.tv1.power()
        assert self.tv1.__str__() == 'Power = False, Channel = 1, Volume = 0.'
        #on and channel up one
        self.tv1.power()
        self.tv1.channel_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 2, Volume = 0.'
        #channel up two and on
        self.tv1.channel_up()
        self.tv1.channel_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0.'
    def test_channel_down(self):
        #off nad channel decreased
        self.tv1.power()
        self.tv1.channel_up()
        self.tv1.channel_down()
        self.tv1.power()
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0.'
        #on and decreased once
        self.tv1.power()
        self.tv1.channel_down()
        assert self.tv1.__str__() == 'Power = True, Channel = 3, Volume = 0.'
    def test_volume_up(self):
        #off and volume up one
        self.tv1.power()
        self.tv1.volume_up()
        self.tv1.power()
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 1.'
        #on and volume up one
        self.tv1.power()
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 2.'
        #on muted and increased
        self.tv1.volume_up()
        self.tv1.mute()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0.'
        #on and up 1 at max
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 2.'

    def test_volume_down(self):
        #off and volume decreased
        self.tv1.power()
        self.tv1.volume_up()
        self.tv1.volume_down()
        self.tv1.power()
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0.'
        #on and decreased from max
        self.tv1.power()
        self.tv1.volume_up()
        self.tv1.volume_up()
        self.tv1.volume_down()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 1.'
        # on muted and decreased
        self.tv1.volume_down()
        self.tv1.mute()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0.'
        #on and decreased at the minimum
        self.tv1.volume_down()
        self.tv1.volume_down()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0.'
