day = 11

with open(f"2015/inputs/{day}.txt", "r") as f:
    lines = f.read().splitlines()

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

tests_1 = [
    ("hijklmmn", False),
    ("abbceffg", False),
    ("abbcegjk", False),
    ("abcddeeg", True),
    ("abcdffaa", True),
    ("ghjaabcc", True),
]

tests_2 = [
    ("abcdefgh", "abcdffaa"),
    ("ghijklmn", "ghjaabcc"),
]


def is_valid(password):
    if (
        any(
            ALPHABET.index(password[i - 1]) == ALPHABET.index(password[i]) - 1
            and ALPHABET.index(password[i]) == ALPHABET.index(password[i + 1]) - 1
            for i in range(1, 7)
        )
        and not any(ch in password for ch in "iol")
        and len(
            set([password[i] for i in range(1, 8) if password[i - 1] == password[i]])
        )
        > 1
    ):
        return True
    return False


# for password, test_result in tests_1:
#    print(password, is_valid(password) == test_result)


def next_password(password):
    i = 7
    next_password = list(password)
    while i >= 0:
        alphabet_index = ALPHABET.index(password[i])
        if alphabet_index + 1 == len(ALPHABET):
            next_password[i] = ALPHABET[0]
            i -= 1
        else:
            next_password[i] = ALPHABET[alphabet_index + 1]
            break
    return "".join(next_password)


def get_next_valid_password(password):
    password = next_password(password)
    while not is_valid(password):
        password = next_password(password)
    return password


# for password, test_result in tests_2:
#    print(password, get_next_valid_password(password) == test_result)

result1 = get_next_valid_password(lines[0])
print(result1)

# part 2
print(get_next_valid_password(result1))
