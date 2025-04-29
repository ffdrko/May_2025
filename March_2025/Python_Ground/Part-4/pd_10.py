import random


def encode(m):
    if len(m) >= 3:
        m = m[1:] + m[0]  # Move first letter to the end
        rand_chars = ''.join(chr(random.randint(65, 90)) for _ in range(3))  # Generate 3 random uppercase letters
        return rand_chars + m + rand_chars
    else:

        return m[::-1]  # Reverse if length < 3


def decode(m):
    if len(m) >= 9:  # Ensures the length includes the 3 random characters at both ends
        core_message = m[3:-3]  # Remove the random characters
        original_message = core_message[-1] + core_message[:-1]  # Move last letter back to the front
        return original_message
    else:
        return m[::-1]  # Reverse if length < 3


# Testing the functions
message = input("Enter your message: ")
encoded_msg = encode(message)
print("Encoded:", encoded_msg)

decoded_msg = decode(encoded_msg)
print("Decoded:", decoded_msg)