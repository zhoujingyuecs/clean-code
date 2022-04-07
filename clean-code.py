import re

file_name = open('./name.txt')
dic_name = {}
dic_value = {}
for line in file_name:
	if '=' in line:
		split_line = line.split()
		value = 0
		if 'x' in split_line[2][:-1]:
			value = eval(split_line[2][:-1])
		else:
			value = int(split_line[2][:-1])
		dic_name[value] = split_line[0]
		dic_value[split_line[0]] = value

file_value = open('./value.txt')
lines = []
for line in file_value:
	split_line = re.split('[>=; ]', line)
	# print(split_line)
	name = split_line[1]
	value_str = split_line[4]
	# print(name, value_str)
	value = 0
	if 'x' in value_str:
		value = eval(value_str)
	else:
		value = int(value_str)
	if name in dic_value:
		string_line = '{' + hex(dic_value[name]) + ',' + hex(value) + '}, // ' + str(dic_value[name]) + ', ' + name
		lines.append([dic_value[name], string_line])

lines.sort(key = lambda x:x[0])
for line in lines:
	print(line[1])




# import re

# file_name = open('./name.txt')
# dic_name = {}
# for line in file_name:
# 	if '=' in line:
# 		split_line = line.split()
# 		value = 0
# 		if 'x' in split_line[2][:-1]:
# 			value = eval(split_line[2][:-1])
# 		else:
# 			value = int(split_line[2][:-1])
# 		dic_name[value] = split_line[0]

# file_value = open('./value.txt')
# lines = []
# for line in file_value:
# 	split_line = re.split('[{,}]', line)
# 	# value = eval(split_line[1])
# 	value = int(split_line[3])
# 	string_line = line[:-1] + ' // ' + str(value) + ', ' + dic_name[value]
# 	lines.append([value, string_line])

# lines.sort(key = lambda x:x[0])
# for line in lines:
# 	print(line[1])
