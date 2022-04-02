#password anonimity using Hash function
#many types of Hash, example: md5, SHA-1, SHA-256(takes a longer time)
#hash function converts input word to a nonsence code , it stores the input to memory location
#key anonimity modern technique to prevent leak of passwords
#allows receive information about us without knowing who we are
import requests, hashlib, unittest, pdb

def get_similar_hashes(hash_query, full_hash):
    # pdb.set_trace()
    url = "https://api.pwnedpasswords.com/range/" + hash_query
    res = requests.get(url)

    if res.status_code != 200:
        raise RuntimeError(f"Please check again your API. Your request failed with status {res.status_code}")
    return check_hashes(res, full_hash)
    
def convert_to_hash(password):
    hash_query = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first_chars, full_hash = hash_query[:5], hash_query[5:]
    return get_similar_hashes(first_chars, full_hash)

def check_hashes(res, full_hash):
    hashes = (hassh.split(":") for hassh in res.text.splitlines())
    for hassh, count in hashes:
        if hassh == full_hash:
            print("Unfortunately your password is not safe, leaked " + count + " times")
    

# if __name__ == "__main__":
#     sys.exit(main(sys.argv[1:]))

