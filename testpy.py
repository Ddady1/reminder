def arithmetic_arranger(problems):
	if len(problems) > 5:
		print('Error: Too many problems.')
	for prob in problems:
		x = prob.split()
		if x[1] != '+' and x[1] != '-':
			print("Error: Operator must be '+' or '-'.")
		elif not x[0].isdigit() or not x[2].isdigit():
			print('Error: Numbers must only contain digits.')
		elif len(x[0]) > 4 or len(x[2]) > 4:
			print('Error: Numbers cannot be more than four digits.')
	#return arranged_problems

arithmetic_arranger(["32 + 698", "3801 - 25", "45 + 43", "123 + 49"])