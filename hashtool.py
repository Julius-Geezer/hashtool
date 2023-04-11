import hashlib 

print('''
This script allows you to input a file, select a hash algorithm and get the hash key of the file. It uses Python's hashlib library and contrains the following hash algorithms. 

SHA1 
SHA224 
SHA256 
SHA384
SHA512   
MD5

When entering the file path, it must be formatted correctly or else an error will be thrown. The format should look like this.

/home/user/work/notes/file.txt
'''
)


file_path = input('Enter the path to the file you wish to use: ')
print(file_path) 

hash_choice = input('Enter hashing algorithm from above: ').upper() 


# Dictionary with choices of algorithms and corresponding methods 
hash_dict = {
        'SHA1': hashlib.sha1(),
        'SHA224': hashlib.sha224(), 
        'SHA256': hashlib.sha256(),
        'SHA384': hashlib.sha384(),
        'SHA512': hashlib.sha512(),
        'MD5': hashlib.md5()
        }
 
# Function that matches user input and performs hashing on the file, also handles errors 
def hashfunction(file_path, hash_choice):
    try:
        file = open(file_path, 'rb')
        read_file = file.read()
   
        hash_object = hash_dict.get(hash_choice)

        if hash_object is None:
            print('Hash algorithm not found') 
            return None
    
    except (FileNotFoundError, IsADirectoryError):
        print('File not found. Make sure input is formatted correctly') 
        return None

    hash_object.update(read_file)

    hash_value = hash_object.hexdigest() 

    print(f'The {hash_choice} hash value of {file_path}: {hash_value}')  
  

if __name__ == '__main__':
    hashfunction(file_path, hash_choice) 
