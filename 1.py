def funcion_rec(self, n:int) -> int:
    if n <= 0:
        return 1
    else:
        return n * funcion_rec(n - 1)