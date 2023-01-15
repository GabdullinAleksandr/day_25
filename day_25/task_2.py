def main():
    list_ = []
    str_ = input('Строка: ')
    for i in range(len(str_)):
        for j in range(len(str_) + 1):
            var = str_[i:j + i + 1]
            list_.append(var)
    list_.append('')
    res = set(list_)
    len_ = len(res)
    print(f'result: {len_}')
    print(f'{len_} различных подстроки: {res}')


if __name__ == '__main__':
    main()
