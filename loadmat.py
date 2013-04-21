import re
url = []
a = ''


def total_l(a):
    return len(a[7:])


def letters(a):
    return len(re.findall(r'[a-z]', a[7:]))


def numbers(a):
    return len(re.findall(r'[0-9]', a[7:]))


def slashes(a):
    return a[7:].count('/')


def main_letters(a):
    return len(re.findall(r'[a-z]', a.split('.')[1]))


def main_numbers(a):
    return len(re.findall(r'[0-9]', a.split('.')[1]))


def vectorize(a):
    tmp = []
    tmp.append(total_l(a))
    tmp.append(letters(a))
    tmp.append(numbers(a))
    tmp.append(slashes(a))
    tmp.append(main_letters(a))
    tmp.append(main_numbers(a))
    return tmp

if __name__ == '__main__':
    with open('./training_data1.txt') as f:
        for line in f:
            url.append(line)
    benign = url[:2000]
    malware = url[2000:]
    benign_v = []
    malware_v = []
    for i in benign:
        benign_v.append(vectorize(i))
    for i in malware:
        malware_v.append(vectorize(i))

    b = open('benignn.txt', 'w')
    b.writelines(str(benign_v))

    m = open('malwaree.txt', 'w')
    m.writelines(str(malware_v))

    benign_a = []
    malware_a = []

    for i in range(len(benign_v[0])):
        sum_b = 0
        sum_m = 0
        for v in benign_v:
            sum_b += int(v[i])
        for v in malware_v:
            sum_m += int(v[i])

        benign_a.append(float(sum_b)/len(benign_v))
        malware_a.append(float(sum_m)/len(malware_v))

    print benign_a
    print malware_a
