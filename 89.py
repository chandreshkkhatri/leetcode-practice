def grayCode(n):
    result = [0]
    for i in range(n):
        result += [x | (1 << i) for x in reversed(result)]
    return result


if __name__ == "__main__":
    print(grayCode(10))
