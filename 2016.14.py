import hashlib

def custom_hash(text, super_hash=False):
    hash = hashlib.md5(text.encode('utf-8')).hexdigest()
    if super_hash:
        for _ in range(2016):
            hash = hashlib.md5(hash.encode('utf-8')).hexdigest()
    return hash

def check_muliples(hash, amount):
    for i in range(len(hash) - (amount-1)):
        block = hash[i:i+amount]
        if block.count(block[0]) == len(block):
            if i + amount == len(hash): # Reached final block of numbers
                return (True, hash[i])
            if hash[i] != hash[i+amount]:
                return (True, hash[i])
    return (False, None)

def valid_quint(key, char, index):
    return (
        key['char'] == char
        and index > key['index'] >= index - 1000
        and key['valid'] == False
    )

def find_answer(salt, super_hash):
    index = 0
    keys = []
    valid_keys = []
    while True:
        text = salt + str(index)
        hash = custom_hash(text, super_hash=super_hash)

        # Check if hash meets initial triple character requirement
        (has_triples, t_char) = check_muliples(hash, 3)
        if has_triples:
            keys.append({
                'index': index,
                'char': t_char,
                'valid': False,
            })

        # Check if hash meets the quintuple requirement of previous hash
        (has_quintuples, q_char) = check_muliples(hash, 5)
        if has_quintuples:
            for key in keys:
                if valid_quint(key, q_char, index):
                    key['valid'] = True
                    valid_keys.append(key)

        # Check if we've reached the desired number
        if len(valid_keys) >= 64:
            return(valid_keys[63]['index'])

        index += 1

if __name__ == '__main__':
    salt = input('Enter salt: ')
    print("Part One Answer: {}".format(find_answer(salt, False)))
    print("Part One Answer: {}".format(find_answer(salt, True)))
