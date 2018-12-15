arr = [ 0x08, 0x8B, 0xDE, 0xBF, 0x9D, 0xA9, 0x04, 0x12, 0x8B, 0x12, 
  0x12, 0x9A, 0x62, 0xA9, 0x51, 0x47, 0xEA, 0xEA, 0x30, 0x8B, 
  0x26, 0x02, 0x4B, 0x77, 0x32, 0x74, 0x41, 0x7D, 0x4A, 0x7C, 
  0x4F, 0x0B, 0x4F, 0x7B, 0x05, 0x6C, 0x1B, 0x7D, 0x0B, 0x63, 
  0x14, 0x70][::-1]

left = arr[0:21]
right = arr[21:42]
left_flag = ''
right_flag = ''

left_flag += chr(arr[0] - 3)
for i in range(1, len(left), 1):
	temp = (left[i] ^ left[i - 1]) - 3
	left_flag += chr(temp)

right_flag += ''
for c in range(0x23, 0x82, 1):
	if c ^ ((16 * c) & 0xff) == right[0]:
		right_flag += chr(c - 3)

for i in range(1, len(right), 1):
	for c in range(0x20, 0x7f, 1):
		temp = c + 3
		temp ^=(right[i - 1] >> 4)
		temp ^= (16 * temp) & 0xff
		if temp == right[i]:
			right_flag += chr(c)
			break
print left_flag + right_flag