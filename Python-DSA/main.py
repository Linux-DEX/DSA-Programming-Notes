count = 0

def func():
    global count
    if count == 4:
        return
    print("1")
    count += 1
    func()


if __name__ == "__main__":
    func()