from proekt320FIO import funk320FIO

def main():
    x = list(map(int, input("Введите числа через пробел: ").split()))
    result = funk320FIO(x)
    print("Результат:", result)

if __name__ == "__main__":
    main()
