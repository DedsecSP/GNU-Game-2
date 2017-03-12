from transitions import Machine

class Game(object):
    states = ['mainMenu', 'clickedPlay', 'clickedOptions', 'options', 'characterSelection', 'playGame', 'gameOver']

    def __init__(self):

        # Initialize the state machine
        self.machine = Machine(model=self, states=Game.states, initial='mainMenu')

        self.machine.add_transition('clickedPlay', 'mainMenu', 'playGame')
        self.machine.add_transition('clickedOptions', 'mainMenu', 'options')
        self.machine.add_transition('returnToMainMenu', 'playGame', 'mainMenu')
        self.machine.add_transition('returnToMainMenu', 'options', 'mainMenu')


if __name__ == "__main__":
    print("")
