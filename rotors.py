# rotors.py
# This code implements a Rotor class for the Enigma Emulation

class Rotor:
    '''
    This class models the Enigma Machine Rotors.
    '''

    POSITIONS = 26 #The number of possible positions.
    COMPLETE_CYCLES = 0 #Counter for completed cycles.

    def __init__(self, pos_config, wiring_config):
        #The init configuration for the rotor
        #must be pseudo random every time
        #a new Enigma session is created.
        #Use random.randint(1,27)
        self.pos_config = pos_config
        self.wiring_config = wiring_config

    def rotate(self):
        '''
        This method rotates the rotor by increasing
        the pos_config variable. If pos_config equals 26
        then it gets set to 1 as value. This restarts the
        counter and signals a full complete cycle for the
        rotor instance by incrementing the COMPLETE_CYCLES
        variable.
        '''
        if self.pos_config == self.POSITIONS:
            self.prev_pos_config = self.pos_config
            self.pos_config = 1
            self.COMPLETE_CYCLES += 1
        else:
            self.pos_config += 1

    def has_completed_cycle(self):
        '''
        This method return a boolean on whether or not
        a full rotor cycle has been completed. If a full cycle
        has been completed this signal an increase in pos_config
        for the second rotor.
        '''
        if self.prev_pos_config == self.POSITIONS:
            self.COMPLETE_CYCLES += 1
            return True
        else:
            return False
