import math

chromosome_count: int = 17
chromosome_length: int = 9
how_much_repeat: int = 100
x_min: float = 0
x_max: float = 100


tournament_size = 2 if math.floor(chromosome_count * 0.2) <= 2 else math.floor(chromosome_count * 0.2)


