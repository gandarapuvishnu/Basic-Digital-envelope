
class Sender:
    def symmetric_encryption(self, text, s):

        from math import remainder
        s = int(remainder(s,26))
        result = ""
        for i in range(len(text)):
            char = text[i]

            # Encrypt uppercase characters
            if (char.isupper()):
                result += chr((ord(char) + s - 65) % 26 + 65)

            # Encrypt lowercase characters
            else:
                result += chr((ord(char) + s - 97) % 26 + 97)

        return result

    def assymetric_encryption(self, common_key, recv_public_keys):
        # RSA encryption algorithm
        (e,n) = (recv_public_keys[0], recv_public_keys[1])

        Cipher = (common_key ** e) % n
        # print("\nCipher text generated is: %s" % (Cipher))
        return Cipher

    def createEnvelope(self, text, sym_key, recv_public_key):

        encr_text = self.symmetric_encryption(text, sym_key)

        encr_key = self.assymetric_encryption(sym_key, recv_public_key)

        msg = {"Text":encr_text, "Key": encr_key}

        return msg


class Receiver:
    def __init__(self):
        self.d = 0
        temp = self.key_generation()
        self.n = temp[1]
        print("\nPublic Key here is - PU(%s,%s)" % (temp[0], self.n))
        print("Private Key here is - PR(%s,%s)" % (self.d, self.n))

    def gcd(self, a, b):
        while (b):
            a, b = b, (a % b)
        return a

    def modInverse(self, a, b):
        a = a % b
        for i in range(1, b):
            if ((a * i) % b) == 1:
                return i

    def key_generation(self):
        # Sample primes
        x = 17
        y = 19

        n = x * y
        phi = (x - 1) * (y - 1)

        flag = 1
        e = 2
        while (flag):
            # e = int(input("Please select value of e: "))
            if self.gcd(phi, e) != 1:
                # print("\nGCD of phi and e should be 1 (Relatively prime).")
                # print("Please try again!")
                e += 1
                continue
            flag = 0

        if e < phi:
            self.d = self.modInverse(e, phi)
        else:
            print("Chosen invalid co-prime!")

        return (e,n)

    def symmetric_decryption(self, text, s):
        s = 26 - (s%26)
        result = ""
        for i in range(len(text)):
            char = text[i]

            # Encrypt uppercase characters
            if (char.isupper()):
                result += chr((ord(char) + s - 65) % 26 + 65)

            # Encrypt lowercase characters
            else:
                result += chr((ord(char) + s - 97) % 26 + 97)

        return result

    def assymetric_decryption(self, Cipher):
        # RSA decryption algorithm
        Decipher = (Cipher**self.d) % self.n
        return Decipher

    def openEnvelope(self, message):
        sym_key = self.assymetric_decryption(message["Key"])
        msg = self.symmetric_decryption(message["Text"], sym_key)

        return msg


if __name__ == '__main__':
    sender = Sender()
    message = input("Enter your message: ")

    receiver = Receiver()
    recv_publickeys = receiver.key_generation()
    print("Actual sent message: ", message)

    from random import randint
    random_key = randint(1, 100)
    print("Symmetric key: ", random_key)

    messageSent = sender.createEnvelope(text=message, sym_key=random_key, recv_public_key=recv_publickeys)

    print("Encrypted message: ", messageSent)

    messageReceived = receiver.openEnvelope(messageSent)

    print("Message Received: ", messageReceived)