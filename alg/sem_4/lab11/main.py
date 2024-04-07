# наличие строки ababaca в тексте

class FSM:
    def __init__(self, alphabet, states, startState, finiteStates, transitions):
        self.alphabet = alphabet
        self.states = states
        self.startState = startState
        self.finiteStates = finiteStates
        self.transitions = transitions
        self.currentState = None
        self.states = []

    def _checkIsBelongAlphabet(self, symbol):
        if symbol in self.alphabet:
            return True
        else:
            return False

    def _changeState(self, symbol):
        if self.transitions[self.currentState] and self.transitions[self.currentState][symbol]:
            self.currentState = self.transitions[self.currentState][symbol]
        else:
            raise Exception("No transition from %s by %s" % (self.currentState, symbol))

    def test(self, value):
        self.currentState = self.startState
        for symbol in value:
            if self._checkIsBelongAlphabet(symbol):
                self._changeState(symbol)
                self.states.append(self.currentState)
            else:
                self.currentState = self.startState
                self.states.append(self.currentState)
        print(self.states)
        self.states.clear()


def main():
    alphabet = "abc"
    states = ["q0", "q1", "q2", "q3", "q4", "q5", "q6", "q7"]
    startState = "q0"
    finiteStates = ["q7"]
    transitions = {
        "q0": {
            "a": "q1",
        },
        "q1": {
            "a": "q1",
            "b": "q2",
        },
        "q2": {
            "a": "q3",
        },
        "q3": {
            "a": "q1",
            "b": "q4",
        },
        "q4": {
            "a": "q5",
        },
        "q5": {
            "a": "q1",
            "b": "q4",
            "c": "q6",
        },
        "q6": {
            "a": "q7",
        },
        "q7": {
            "a": "q1",
            "b": "q2",
        },

    }
    with open("input.txt", "r") as f:
        strings = f.readlines()
        fsm = FSM(alphabet, states, startState, finiteStates, transitions)
        for string in strings:
            print(string)
            fsm.test(string)


if __name__ == "__main__":
    main()
