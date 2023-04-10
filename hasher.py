import hashlib 

print('''
This scripts allows you to input a file, select a hash algorithm and get the hash, it uses Python's Hashlib library and contains the following hash algorithms 

SHA1 
SHA224 
SHA256 
SHA384
SHA512   
MD5

When entering the path for a file it must be formatted correctly, or else an error will be thrown. The format should look like this

/home/user/work/notes/file.txt
'''
)


# Input variables that store file path and choice of hash algorithm 

file_path = input('Enter the path to the file you wish to use: ')
print(file_path) 

hash_choice = input('Enter hashing algorithm from above: ').upper() 

# Function that matches user input and performs hashing on the file, also handles errors 

def hashfunction(file_path, hash_choice):
    try:
        file = open(file_path, 'rb')
        read_file = file.read()
    
        if hash_choice == 'SHA1':
            hash_object = hashlib.sha1() 
        elif hash_choice == 'SHA224':
            hash_object = hashlib.sha224()
        elif hash_choice == 'SHA256':
            hash_object = hashlib.sha256()
        elif hash_choice == 'SHA384': 
            hash_object = hashlib.sha384()
        elif hash_choice == 'SHA512':
            hash_object = hashlib.sha512()
        elif hash_choice == 'MD5':
            hash_object = hashlib.md5() 
        else:
            return None
    
    except (FileNotFoundError, IsADirectoryError):
        print('File not found. Make sure input is formatted correctly') 
        return None

    hash_object.update(read_file) 

    hash_value = hash_object.hexdigest() 

    print(f'The {hash_choice} hash value of {file_path}: {hash_value}')  
   
if __name__ == '__main__':
    hashfunction(file_path, hash_choice) 
