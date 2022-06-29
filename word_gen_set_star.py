import time
import cw_words


def main():
    find = cw_words.c5

    with open('russian.txt', 'r', encoding='windows-1251') as f:
        text = f.read()

    generated_words = set()
    for i in find:
        temp = ''.join(i)
        strs = temp.split('*')
        generated_words.update(strs)

    ru_dict = set(text.splitlines())
    print(generated_words.intersection(ru_dict)) if generated_words.intersection(ru_dict) else print('None')


if __name__ == '__main__':
    start = time.perf_counter()
    main()
    finish = time.perf_counter()
    print(f'Finished in {round(finish - start, 2)} sec')
