class PackageState:
    name = "state"
    allowed = []

    def switch(self, state):

        if state.name in self.allowed:
            old_state_name = self.name
            self.__class__ = state
            return f'Current: {old_state_name} switching to {state.name}'
        else:
            return f'Current: {self.name} not possible to switch to {state.name}'
