
class Game(object):
    '''
        Base class for all board games 
    '''
    def __init__(self, name, players, max_players):
        self.name = name
        self.players = players
        self.max_players = max_players
        
        self.init_max_players()

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def run(self, *args, **kwargs):
        raise NotImplementedError('Implement in child class')
