import datetime as dt

def data_array(data_loc='gpu-usage\\log1.txt'):
	data = []
	with open(data_loc, 'r') as fp:
		'''
		Stores log1.txt as an array of dictionaries. Each dictionary
		corresponds to a row, and has keys corresponding to the dataset's fields 
		'''

		first_line = fp.readline()
		first_line_list = first_line.split(',')
		first_line_list.remove('\n')
		# For each field name, removes excess whitespace and stores in a list
		fields_list = [' '.join(field.split()) for field in first_line_list] 

		for line in fp:
			row = {}
			raw_values_list = line.split(',')
			raw_values_list.remove('\n')
			# For each value, removes excess whitespace and stores in a list
			values_list = [' '.join(value.split()) for value in raw_values_list]
			for value, field in zip(values_list, fields_list):
				if field in ['Fan Speed (RPM) [RPM]', 'Memory Used [MB]', 'PerfCap Reason []']:
					row[field] = int(value)
				elif 'Date' == field:
					row[field] = dt.datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
				else:
					row[field] = float(value)
			data.append(row)

	return data


if __name__ == '__main__':
	pass