#연습1의 해쉬 테이블 코드에 Linear Probling 기법으로 충돌해결 코드를 추가해보기
hash_table = list([0 for i in range(8)])

def get_key(data):
	return hash(data)

def hash_function(key):
	return key % 8

def save_data(data, value):
	index_key = get_key(data)
	hash_address = hash_function(index_key)
	if hash_table[hash_address] != 0:
		for index in range(hash_address, len(hash_table)):
			if hash_table[index] == 0:
				hash_table[index] = [index_key, value]
				return
			elif hash_table[index][0] == index_key:
				hash_table[index][1] = value
				return
	else:
		hash_table[hash_address] = [index_key, value]

def read_data(data):
	index_key = get_key(data)
	hash_address = hash_function(index_key)
	
	if hash_table[hash_address] != 0:	
		for index in range(hash_address, len(hash_table)):
			if hash_table[index] == 0:
				return None
			elif hash_table[index][0] == index_key:
				return hash_table[index][1]
	else:
		return None

print (hash('dk') % 8)
print (hash('da') % 8)
print (hash('dc') % 8)

save_data('dk', '01200123123')
save_data('da', '3333333333')
print(read_data('dc'))










		