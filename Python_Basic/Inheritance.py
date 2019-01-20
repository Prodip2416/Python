class A:
    def Where(self):
        print('i am from class A')


class B(A):
    def Where(self):
        print('i am from class B')
        super().Where()


# class C(A, B):
#     pass


B().Where()

