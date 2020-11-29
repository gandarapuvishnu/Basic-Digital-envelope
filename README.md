# Basic-Digital-envelope

Digital Envelope Algorithm:

Receiver :
1.	Generate public and private keys to process further communication.

Sender:
1.	Create message to be shared.
2.	Create a random symmetric key
3.	Encrypt the message and random symmetric key with Symmetric Encryption. (In this case, Ceasar Cipher algorithm.)
4.	Collect Receiver’s public key
5.	Encrypt Receiver’s public key and the random symmetric key using Assymetric Encryption(In this case, RSA encryption algorithm.)
6.	Combine both Encrypted message and encrypted key.

#Envelope Created

Receiver:
1.	Decrypt the encrypted key shared within the digital envelope, using the receiver’s private key and the encrypted key by the means of assymetric decryption(In this case, RSA decryption algorithm ).
2.	By using the decrypted key obtained, receiver has to decrypt the message using that key by using the Symmetric Decryption(In this case, Ceasar Cipher algorithm).

#Envelope Opened

3.	Now, if the receiver is the expected receiver by the sender, then message will be shared correctly. Otherwise, it’ll be corrupt message.



![Screenshot (87)](https://user-images.githubusercontent.com/52231690/100534339-a4878d80-3233-11eb-9628-5ccce9835839.png)
