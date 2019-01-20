class Monster:
    def __init__(self, color, heads):
        self.color = color
        self.heads = heads

    def attack(self):
        print("Just attack a hero! mu.........hahahahaha")


# MS = Monster("Yellow", 5);
# MS1 = Monster("Blue", 7);
#
# print('i have ' + str(MS.heads) + ' color and ' + str(MS.heads) + ' heads.')
# print('i have ' + str(MS1.heads) + ' color and ' + str(MS1.heads) + ' heads.')
#
# MS = Monster("Black",8)
# print('i am a ' + str(MS.color ) + ' monster with ' + str(MS.heads) + ' heads.');
# MS.attack()


class A(Monster):
    def Sound(self):
        print('hurrrrrrrrrrr')


A = A("Yellow",6)
A.Sound()
A.attack()