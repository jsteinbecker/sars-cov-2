def roundUpToMultiple(number, multiple):
    num = number + (multiple - 1)
    return num - (num % multiple)