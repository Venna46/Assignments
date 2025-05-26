from queue import Queue

def is_palindrome(text: str) -> bool:
    # Simplified cleaning: keep alphanumerics and lowercase everything
    cleaned = ''.join([char.lower() for char in text if char.isalnum()])

    stack = []
    queue = Queue()

    for char in cleaned:
        stack.append(char)
        queue.put(char)

    for _ in range(len(cleaned) // 2):
        if stack.pop() != queue.get():
            return False

    return True

# Example usage
if __name__ == "_main_":
    s = input("Input a word or sentence: ").strip()
    if is_palindrome(s):
        print(f"The input, '{s}', is a palindrome.")
    else:
        print(f"The input, '{s}', is not a palindrome.")
test_cases = [
    "racecar",
    "hello",
    "A man, a plan, a canal, Panama",
    "Was it a car or a cat I saw?",
    "No lemon, no melon"
]

for text in test_cases:
    print(f"'{text}': {is_palindrome(text)}")