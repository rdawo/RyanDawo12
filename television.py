class Television:
    '''sets intial values for variables for use in later code'''
    MIN_VOLUME:int = 0
    MAX_VOLUME:int = 2
    MIN_CHANNEL:int = 0
    MAX_CHANNEL:int = 3

    def __init__(self)-> None:
        ''' also sets intial values for variables for use in later code'''
        self.__status:bool = False
        self.__muted:bool = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def power(self)-> None:
        '''sets power to on or off depending on current status'''
        if self.__status == False:
            self.__status = True
        elif self.__status == True:
            self.__status = False

    def mute(self)-> None:
        '''mutes or unmutes depending on current mute status'''
        if self.__muted == False:
            self.__muted = True
            self.__volume = self.MIN_VOLUME
        elif self.__muted == True:
            self.__muted = False

    def channel_up(self)-> None:
        '''changes channel to next channel or
        returns to first channel if at max channel'''
        if self.__channel == self.MAX_CHANNEL:
            self.__channel = self.MIN_CHANNEL
        elif self.__channel < self.MAX_CHANNEL:
            self.__channel += 1

    def channel_down(self)-> None:
        '''changes channel to previous channel or
        returns to last channel if at min channel'''
        if self.__channel == self.MIN_CHANNEL:
            self.__channel = self.MAX_CHANNEL
        elif self.__channel > self.MIN_CHANNEL:
            self.__channel -= 1

    def volume_up(self)-> None:
        '''sets volume to max volume or increases volume
        by 1 if less than max volume and unmutes if muted'''
        if self.__volume == self.MAX_VOLUME:
            self.__volume = self.MAX_VOLUME
        elif self.__volume < self.MAX_VOLUME:
            self.__volume += 1
            if self.__muted == True:
                self.__muted = False

    def volume_down(self) -> None:
        '''sets volume to min volume or decreases
         volume by 1 if greater than min volume'''
        if self.__volume == self.MIN_VOLUME:
            self.__volume = self.MIN_VOLUME
            self.__muted = True
        elif self.__volume > self.MIN_VOLUME:
            self.__volume -= 1

    def __str__(self) -> str:
        '''returns current status of power, channel, and volume for use in main program'''
        return f"Power: {self.__status}, Channel: {self.__channel}, Volume: {self.__volume}"
