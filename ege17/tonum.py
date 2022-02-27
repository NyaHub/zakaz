import string
def tonum(num, base): # конвертирует число из 10 системы счисления в любую другую доступную (от 2 до 36)
    if not(2<=base<=36):
        raise Exception('Incorrect base!')
    dict=list(string.digits + string.ascii_lowercase)
    newnum = ''
    while num > 0:
        newnum = dict[num%base] + newnum
        num //= base
    return newnum
