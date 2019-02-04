class UserData:
    def __init__(self, id, name):
        self.id = id
        self._name = name


class NewUser(UserData):
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if len(name) > 3:
            self._name = name
        else:
            print('ERROR')

    def __call__(self):
        print('{}\'s id is {}'.format(self._name, self.id))


if __name__ == '__main__':
    user = NewUser(101, 'Jack')
    user()
