
def hash_func(user_input_1, user_input_2, user_input_3, filename):
    hash_str = f'{user_input_1}{user_input_2}{user_input_3}'
    with open('hash.json', 'r') as f:
        content = json.load(f)
    if content[0].get(hash_str):
        if content[0][hash_str] != filename:
            with open(content[0][hash_str]) as f:
                data = csv.reader(f)
                with open(filename, 'w') as file:
                    writer = csv.writer(file)
                    for row in data:
                        writer.writerow(row)
            for i in content[0].keys():
                if filename == content[0][i]:
                    content[0].pop(i)
                    break
            content[0][hash_str] = filename
    else:
        for i in content[0].keys():
            if filename == content[0][i]:
                content[0].pop(i)
                break
        content[0][hash_str] = filename
        print('Запуск...')
        select_sorted(user_input_1, user_input_2, user_input_3, filename)
    with open('hash.json', 'w') as f:
        json.dump(content, f)
    print(f'Информация загружена в файл "{filename}"')
