class Jar:
    def __init__(self, capacity=12, size =0):
        if capacity>0:
            self._capacity = capacity
            self._size = size
        else:
            raise ValueError('capacidade menor que 0')

    def __str__(self):
        lista_cookies = ''
        if self._size>self._capacity:
            return 'impossível colocar tantos cookies'
        else:
            for _ in range(self._size):
                lista_cookies += '🍪'
            return lista_cookies
    

    def deposit(self, n):
        if n+self._size<self._capacity:
            self._size += n
            return self._size
        else:
            raise ValueError('passou da capacidade de cookies')

    def withdraw(self, n):
        if n> self._size:
            raise ValueError('não temos tantos cookies no jarro')
        else:
            return self.size - n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


if __name__ == '__main__':
    x = Jar(20,11).deposit(4)
    y = Jar(20,11)
    print(y)
    print(x)
    print(y.withdraw(5))
    print(y.capacity)
    print(y.size)

