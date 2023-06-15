# Print 5+N

def main():
    while True:
        try:
            a1, a2, a3 = map(int, input().split())
            if 1 <= a1 <= 100 and 1 <= a2 <= 100 and 1 <= a3 <= 100:
                break
        except:
            pass

    total_sum = a1 + a2 + a3
    print(total_sum)

if __name__ == "__main__":
    main()