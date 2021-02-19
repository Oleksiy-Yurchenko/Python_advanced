class Player:
    instance_count = 0

    def __init__(self, name, age, height, weight):
        self.__class__.instance_count += 1
        self._name = name
        self._age = age
        self._height = height
        self._weight = weight

    @ property
    def name(self):
        return self._name

    def get_age(self):
        return '{0} age is {1}.'.format(self._name, self._age)

    def get_height(self):
        return '{0} height is {1}.'.format(self._name, self._height)

    def get_weight(self):
        return '{0} weight is {1}.'.format(self._name, self._weight)

class Team(Player):
    def __init__(self, name):
        self._name = name
        self.team = []

    def new_player(self, name, age, height, weight):
        player = Player(name, age, height, weight)
        self.team.append(player)

    def team_names(self):
        for player in self.team:
            print(player.name)


if __name__ == '__main__':

    petya = Player('Petya', 25, 175, 74)

    my_team = Team('Zvezda')
    my_team.new_player('Vasya', 30, 180, 80)
    my_team.new_player('Petya', 25, 180, 80)
    print(Player.instance_count)

    my_team.team_names()