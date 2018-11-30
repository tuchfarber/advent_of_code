import hashlib


index = 0
salt = 'abc'
keys = []
all_hashes = []

def check_muliples(hash, amount):
    for i in range(len(hash) - (amount-1)):
        if (
            amount==3 and (hash[i] == hash[i+1] == hash[i+2])
        ) or (
            amount == 5 and (hash[i] == hash[i+1] == hash[i+2] == hash[i+3] == hash[i+4])
        ):
            not_at_end = i+amount < len(hash)
            if not_at_end:
                if hash[i] != hash[i+amount]:
                    return (True, hash[i])
            else:
                return (True, hash[i])
    return (False, None)

while True:
    text = salt + str(index)
    hash = hashlib.md5(text.encode('utf-8')).hexdigest()
    all_hashes.append(hash)
    (has_triples, t_char) = check_muliples(hash, 3)
    if has_triples:
        keys.append({
            't_hash': hash,
            't_index': index,
            'q_hash': None,
            'q_index': None,
            'char': t_char,
            'valid': False,
        })

    (has_quadruples, q_char) = check_muliples(hash, 5)
    if has_quadruples:
        for key in keys:
            if key['char'] == q_char and key['t_index'] >= index - 1000 and key['valid'] == False and key['t_index'] != index:
                key['q_index'] = index
                key['q_hash'] = hash
                key['valid'] = True


    index += 1
    if index % 1000 == 0:
        working_keys = [key for key in keys if key['valid'] == True]
        if len(working_keys) >= 64:
            for (index, key) in enumerate(working_keys[:64]):
                print("{t_index}: {t_hash}; {q_index}: {q_hash}; Char: {char}".format(
                    t_index=key['t_index'],
                    t_hash=key['t_hash'],
                    q_index=key['q_index'],
                    q_hash=key['q_hash'],
                    char=key['char']
                ))
            break
