def multiple(start, radius, keys):
	value = 0
	for i in range(radius):
		value *= 0xA
		value += keys[start + i]
		
	return value

def validate(key):
	#if len(key) != 29:
	#	return False
		
	if ord(key[0x6]) != 0x37:
		return False
		
	if ord(key[0x0]) == 0x30:
		return False

	if ord(key[0x4]) == 0x30:
		return False

	if ord(key[0x8]) == 0x30:
		return False

	if ord(key[0xC]) == 0x30:
		return False

	if ord(key[0x10]) == 0x30:
		return False

	if ord(key[0x15]) == 0x30:
		return False		
		
	
	
	keys = []
	
	for m in key:
		if ord(m) >= 0x40 or ord(m) < 0x30:
			return False
			
		keys.append(ord(m) - 0x30)
		
	checksums = []
	
	
	checksums.append(multiple(0, 4, keys))
	checksums.append(multiple(4, 4, keys))
	checksums.append(multiple(8, 4, keys))
	checksums.append(multiple(12, 4, keys))
	checksums.append(multiple(16, 5, keys))
	checksums.append(multiple(21, 8, keys))
	
	
	
	if keys[0x7] * checksums[0x0] != checksums[0x4]:
		return False
	
	if keys[0x6] * checksums[0x0] != checksums[0x2]:
		return False
		
	if keys[0x5] * checksums[0x0] != 0:
		return False

	if keys[0x4] * checksums[0x0] != checksums[0x3]:
		return False
		
	lastCheck = (keys[0x7] * checksums[0x0]) + (keys[0x6] * checksums[0x0] * 0xA) + (keys[0x4] * checksums[0x0] * 0x3E8)
	
	print(checksums)
	print(lastCheck, checksums[0x5])
	if lastCheck != checksums[0x5]:
		return False
		
	return True

#print(multiple(0, 5, [0, 1, 0, 0, 0, 1]))
print(validate("12388079866699041114210001802"))
#print(hex(multiple(8, 4, [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 2, 3, 4, 5, 6, 8, 8])))