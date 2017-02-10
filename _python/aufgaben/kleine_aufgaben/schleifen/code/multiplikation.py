for num in range(1,11):
	zeile = ''
	# Für das Gitter
	if num == 2:
		print('-' * (80))
	for base in range(1,11):
		# Für das Gitter
		if base == 2:
			zeile += '|'

		# Zahl berechnen
		val = num * base
		zeile += str(val) + "\t"
	print(zeile)
