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

file_value = open('./mesa-read-caps.txt')
lines = []
for line in file_value:
	split_line = re.split(',', line)
	# print(split_line)
	name_v = int(split_line[0])
	value_str = split_line[1]
	# print(name, value_str)
	value = 0
	if 'x' in value_str:
		value = eval(value_str)
	else:
		value = int(value_str)
	if name_v in dic_name:
		string_line = '{' + hex(name_v) + ',' + hex(value) + '}, // ' + str(name_v) + ', ' + dic_name[name_v]
		lines.append([name_v, string_line])

lines.sort(key = lambda x:x[0])
for line in lines:
	print(line[1])
