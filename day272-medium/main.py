def throw_dice(nb_dice: int, faces: int, total: int):
    pass

if __name__ == '__main__':
    assert 1 == throw_dice(nb_dice=2, faces=6, total=12) # (6, 6)
    assert 2 == throw_dice(nb_dice=2, faces=6, total=11) # (5, 6) (6, 5)