import hashlib as hl  #Hashlibrary used to create hashes
import json 

def hash_string_256(string):
    return hl.sha256(string). hexdigest() #hexdigest to geta valid string 

def hash_block(block):
    """ Hashes a block and returns a string representation of it.

    Arguments:
        :block: The block that should be hashed.
    """
    return hl.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest()
