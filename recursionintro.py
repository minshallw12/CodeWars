data = []
def countdown(num):
    data.append(str(num))
    if num == 1:
        return ' '.join(data)
    return countdown(num-1)

print(countdown(10))

def countup(num):
    count = 1
    data.append(count)
    if count == num:
        return ' '.join(data)
    return countup(num+1)



print(countup(10))