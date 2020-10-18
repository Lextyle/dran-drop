def is_collision(x_1, y_1, width_1, height_1, x_2, y_2, width_2, height_2):
	return x_1 in range(x_2 + 1 - width_1, x_2 - 1 + width_2) and y_1 in range(y_2 + 1 - height_1, y_2 - 1 + height_2)