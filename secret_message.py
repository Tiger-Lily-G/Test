from constants import MESSAGE, KEY_CODE


def make_inverted_key_code(keycode=KEY_CODE):
    inverted_dict = {}

    for key, value in keycode.iteritems():
        inverted_dict[value] = key

    return inverted_dict

INVERTED_KEY_CODE = make_inverted_key_code()


class EncoderDecoder(object):

    def _decode_letter(self, letter):
        'Returns the letter according to the KEY_CODE'
        return KEY_CODE[letter]

    def _encode_letter(self, letter):
        'Returns the letter according to the INVERTED_KEY_CODE'
        return INVERTED_KEY_CODE[letter]

    def encode_message(self, message):
        encoded_message = ''

        for letter in message:

            if letter not in INVERTED_KEY_CODE.keys():
                encoded_message += letter
            else:
                encoded_message += self._encode_letter(letter)

        return encoded_message

    def decode_message(self, secret_message=None):
        message = ''

        if secret_message is None:
            secret_message = MESSAGE

        for letter in secret_message:

            if letter not in KEY_CODE.keys():
                message += letter
            else:
                message += self._decode_letter(letter)

        return message
