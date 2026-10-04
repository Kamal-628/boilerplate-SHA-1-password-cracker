import hashlib

def crack_sha1_hash(hash, use_salts=False):
    with open("top-10000-passwords.txt") as f:
        passwords = [x.strip() for x in f]

    if use_salts:
        with open("known-salts.txt") as f:
            salts = [x.strip() for x in f]
        for p in passwords:
            for s in salts:
                if hashlib.sha1((s+p).encode()).hexdigest() == hash:
                    return p
                if hashlib.sha1((p+s).encode()).hexdigest() == hash:
                    return p
    else:
        for p in passwords:
            if hashlib.sha1(p.encode()).hexdigest() == hash:
                return p

    return "PASSWORD NOT IN DATABASE"