for i in range(2, 11):
    table = ''
    for j in range(1, 11):
        table += f'{i} X {j} = {i*j}\n'
        with open(f'table\Table_Of_{i}.txt', "w") as f:
            f.write(table)

