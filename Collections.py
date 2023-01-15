def func(xp, y, z):
    if xp > y:
        if xp > z:
            return xp
        else:
            return z
    else:
        if y > z:
            return y
        else:
            return z


xx = int(input("x "))
yy = int(input("y "))
zz = int(input("z "))
print(func(xx, yy, zz))
