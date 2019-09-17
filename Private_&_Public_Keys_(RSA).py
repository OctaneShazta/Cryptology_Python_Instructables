#The following is a small script to help one understand how private and public key sharing functions.
#In this case, we use the RSA algorithm.
#A proper module for this can be imported, but here we can see a functional form of the process.
#Each person in the network has one private key and one public key associated with their encryption algorithm.
#The public key can be broadcasted to anyone, since it is only used to encrypt.
#The private key is never broadcasted to anyone.
#The RSA process requires the use of prime numbers, hence the suggested inputs under Alice.
#Messages meant for Alice are written in a flexible class which allows for user input in determining the keys.
#Messages meant for Bob are written with hard-coded variables.

strmessage = input("please enter the message you wish to send: ")
message = []
print("converting message from string to Unicode array / list")
for each in strmessage:
    message.append(ord(each))
print("plaintext message: ", message)
    
cipher = []
plain = []

class Alice:
    Cipher = []
    Plain = []
    e = int(input("Alice's e (Please select a public exponent) suggested 7: "))
    d = int(input("Alice's d (Please select a private exponenet) suggested 43: "))
    q = int(input("Alice's q (prime number) suggested 11: "))
    p = int(input("Alice's p (another prime number) suggested 31: "))
    phi = (p-1)*(q-1)
    print("Phi = (p-1)*(q-1) = ", phi)
    n = p * q
    print("A semi prime number is calculated: n = p * q = ", n)
    cipher = []
    plain = []
    print("Alice's Public key (e, n) : ", e, ", ", n)
    print("Alice's Private key (d, e, n) : ", d, ", ", e, ", ", n)

    def Encrypt():
        for i in message:
            C = (i**Alice.e)%Alice.n
            Alice.Cipher.append(C)
        print("Encrypted: ", Alice.Cipher)
    def Decrypt():
        for i in Alice.Cipher:
            M = (i**Alice.d)%Alice.n
            Alice.Plain.append(M)
        print("Decrypted: ", Alice.Plain)
        strmessage = []
        for each in Alice.Plain:
            strmessage.append(chr(each))
        print("Translated Message: ", strmessage)
            
        
class Bob:
    Cipher = []
    Plain = []
    e = 3
    d = 2011
    q =59
    p = 53
    phi = 3016
    n = 3127

    def Encrypt():
        for i in message:
            C = (i**Bob.e)%Bob.n
            Bob.Cipher.append(C)
        print("Encrypted: ", Bob.Cipher)
    def Decrypt():
        for i in Bob.Cipher:
            M = (i**Bob.d)%Bob.n
            Bob.Plain.append(M)
        print("Decrypted: ", Bob.Plain)
        strmessage = []
        for each in Bob.Plain:
            strmessage.append(chr(each))
        print("Translated Message: ", strmessage)



def Example():
    print("Original Message: ", message)
    print("Running with Alice's Keys, This would be a message sent from Bob to Alice.")
    Alice.Encrypt()
    Alice.Decrypt()
    print("Running with Bob's Keys, This would be a message sent from Alice to Bob.")
    Bob.Encrypt()
    Bob.Decrypt()


print("to continue type: \n Example(),\n Bob.Encrypt(), Bob.Decrypt(),\n Alice.Encrypt(), or Alice.Decrypt()\n")
