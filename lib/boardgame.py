import fcntl
import os
import random
import socket

class Player(object):
    '''
        Base class for player should be istanitaited 
        for number of players in the game
    '''
    def __init__(self, name, socket=None, port=None, **kwargs):
        self.name = name
        self._socket = socket
        self._port = port
        
        if kwargs.pop('init_conn', False):
            self.init_socket()

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
    
    def init_socket(self):
        if not self.socket:
            self.socket = socket.socket(socket.AF_INET,
                                        socket.SOCK_STREAM)
            self.socket.bind(('', 0))
            self.port = self.socket.getsockname()[1]
    
    def send_message(self):
        pass 

    def recieve_message(self):
        pass
    
    @property
    def is_alive(self):
        return True

class CommandLineGame(object):
    '''
        Base class for all board games

        If command_line is specified, it means that
        we are going to be 
    '''
    def __init__(self, name, max_players, player_name=None):
        self.name = name
        self.max_players = max_players
        if not self.player_name:
            self.player_name = "%s-player%s" %(self.name,
                                               os.getpid())

        self._me = Player(self.player_name, init_conn=True)
        '''
        We need a way to uniquely identify processes,
        but keep it simple enough that other processes 
        can identify us. 
    
        Going to use:
            1) Name of game - help other processes identify
                              relevant other players/games.
            2) pid - uniquely identify all processes up
            3) port - this helps up identify which socket
                      to send to, for multiproc communication
        '''
        self._lock_f = "/tmp/%s_%s_%s" %(self.name,
                                         os.getpid(),
                                         self._port)
        self._lock_f_stream = open(self._lock_f, 'w+')

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def run(self)
        raise NotImplementedError('Implement in child class')
    
    def _get_lock(self):
        try:
            fcntl.flock(self._lock_f_stream, 
                        fcntl.LOCK_EX | fcntl.LOCK_NB)
        except IOError as e:
            raise Exception("Unable to get lock file. Ending")

    def _release_lock(self):
        try:
            fcntl.flock(self._lock_f_stream,
                        fcntl.LOCK_UN)
        except:
            raise Exception("CRITICAL: Unable to unlock file.")

    @property
    def all_players_loaded(self):
        pass
