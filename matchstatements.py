
val = 255, 141, 152, 0
match val:
    case (x, y, z, 0): print('is clear')
    case (255, 255, 255, x): print('is clear')
    case (w, x, y, z): print('is opaque')