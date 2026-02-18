def funk320FIO(x):
    result = []

    for num in x:
        if num not in result:
            result.append(num)

    return result