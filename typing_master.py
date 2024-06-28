

import lorem
import time

def get_random_paragraph():
    return lorem.paragraph()

def typing_test():
    paragraph = get_random_paragraph()
    print("Type the following paragraph as quickly and accurately as you can:")
    print("\n" + paragraph + "\n")

    input("Press Enter when you are ready...")

    start_time = time.time()
    user_input = input("\nStart typing: ")
    end_time = time.time()

    elapsed_time = end_time - start_time
    word_count = len(paragraph.split())
    wpm = (word_count / elapsed_time) * 60

    print("\nResults:")
    print(f"Typed Paragraph: {user_input}")
    print(f"Elapsed Time: {elapsed_time:.2f} seconds")
    print(f"Words Per Minute: {wpm:.2f} WPM")

    if user_input == paragraph:
        print("Accuracy: 100%")
    else:
        print("Accuracy: Less than 100%")

if __name__ == "__main__":
    typing_test()
