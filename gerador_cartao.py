import random

def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    checksum = 0
    reverse_digits = digits[::-1]
    for i, d in enumerate(reverse_digits):
        if i % 2 == 0:
            checksum += d
        else:
            doubled = d * 2
            checksum += doubled if doubled < 10 else doubled - 9
    return checksum % 10

def generate_card(bin_code):
    number = bin_code
    while len(number) < 15:
        number += str(random.randint(0, 9))
    for i in range(10):
        check_digit = str(i)
        if luhn_checksum(number + check_digit) == 0:
            return number + check_digit

def generate_multiple_cards(bin_code, quantity):
    cards = []
    for _ in range(quantity):
        cards.append(generate_card(bin_code))
    return cards

def save_to_file(card_list, filename="cartoes_gerados.txt"):
    with open(filename, "w") as f:
        for card in card_list:
            f.write(card + "\n")
    print(f"{len(card_list)} cartões salvos em {filename}")

if __name__ == "__main__":
    bin_input = "400000"
    quantidade = 10
    cartoes = generate_multiple_cards(bin_input, quantidade)
    print("Cartões gerados:")
    for c in cartoes:
        print(c)
    save_to_file(cartoes)
