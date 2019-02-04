class UserData:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def __repr__(self):
        return 'ID:{} Name:{}'.format(self.id, self.name)

if __name__ == '__main__':
    user1 = UserData(101, 'Jack')
    user2 = UserData(102, 'Louplus')
    print(user1)
    print(user2)
