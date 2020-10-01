import sys
import re

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        sys.exit(0)
    file_name = sys.argv[1]

    reader = open(file_name, encoding='utf8')
    text = reader.read()    
    reader.close()

    text = text.replace("\n", " ").replace(":", ".")
    B = text.count(".")
    print("B: Number of periods", B)
    A_list = text.replace('.', ' ').split()
    print("A: Number of words", len(A_list))
    A = len(A_list)
    C = len([word for word in A_list if len(word) > 6])
    print("C: Long words", C)
    lix_ = (A/B) + ((C * 100)/A)
    print("Lix: ", lix_)
