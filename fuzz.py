import random
import string
import myLogger

def add(v1, v2):
    if isinstance(v1, str) and not v1.isnumeric():
        return "At least one input is non-numeric"
    if isinstance(v2, str) and not v2.isnumeric():
        return "At least one input is non-numeric"

    v1 = float(v1)
    v2 = float(v2)

    return v1 + v2


def multiply(v1, v2):
    if isinstance(v1, str) and not v1.isnumeric():
        return "At least one input is non-numeric"
    if isinstance(v2, str) and not v2.isnumeric():
        return "At least one input is non-numeric"

    v1 = float(v1)
    v2 = float(v2)

    return v1 * v2


def divide(v1, v2):
#    if isinstance(v1, str) and v1.isnumeric()== False:
#       return "At least one input is non-numeric"

#    if isinstance(v2, str) and v2.isnumeric()== False:
#       return "At least one input is non-numeric"

   v1 = float(v1)
   v2 = float(v2)

   if v2!=0:
    return v1 / v2
   else:
      return "Dvision by zero"

def subtract(v1, v2):
    # if isinstance(v1, str) and not v1.isnumeric():
    #     return "At least one input is non-numeric"
    # if isinstance(v2, str) and not v2.isnumeric():
    #     return "At least one input is non-numeric"

    v1 = float(v1)
    v2 = float(v2)

    return v1 - v2

def modulus(v1, v2):
    if isinstance(v1, str) and not v1.isnumeric():
        return "At least one input is non-numeric"
    if isinstance(v2, str) and not v2.isnumeric():
        return "At least one input is non-numeric"

    v1 = float(v1)
    v2 = float(v2)

    if v2 != 0:
        return v1 % v2
    else:
        return "Modulus by zero"


def fuzzValues(val1, val2):
    # Divide
    try:
        res = divide(val1, val2)
        print("Divide: " + res)
    except Exception as e:
        print("Crash Caught in Divide: " + str(e))
    # Add
    try:
        res = add(val1, val2)
        print("Add: " + res)
    except Exception as e:
        print("Crash Caught in Add: " + str(e))
    # Multiply
    try:
        res = multiply(val1, val2)
        print("Multiply: " + res)
    except Exception as e:
        print("Crash Caught in Multiply: " + str(e))
    # Subtract
    try:
        res = subtract(val1, val2)
        print("Subtract: " + res)
    except Exception as e:
        print("Crash Caught in Subtract: " + str(e))
    # Modulus
    try:
        res = modulus(val1, val2)
        print("Modulus: " + res)
    except Exception as e:
        print("Crash Caught in Modulus: " + str(e))

def generateFuzzedValue():
   fuzz_type = random.choice(['int', 'float', 'alpha', 'alphanum'])
   if fuzz_type == 'int':
        return str(random.randint(-1000, 1000))
   elif fuzz_type == 'float':
        return str(round(random.uniform(-1000, 1000), 2))
   elif fuzz_type == 'alpha':
        return ''.join(random.choices(string.ascii_letters, k=random.randint(2, 10)))
   elif fuzz_type == 'alphanum':
        return ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(2, 10)))


def simpleFuzzer():
   try:
    a = generateFuzzedValue()
    logObj.info("Received randomly generated value for a: %r", a)
   except Exception as e:
       logObj.error("Invalid input for a expected another value")
   try:
       b = generateFuzzedValue()
       logObj.info("Received randomly generated value for a: %r", b)
   except Exception as e:
       logObj.error("Invalid input for a expected another value")
   print("A:", a)
   print("B:", b)
   try:
       fuzzresult = fuzzValues(a,b)
       logObj.info("The result of the fuzzed values are: %r", fuzzresult)
   except Exception as e:
       logObj.error("Invalid computation error %r", fuzzresult)


if __name__=='__main__':
    logObj = myLogger.giveMeLoggingObject()
    logObj.info("This is the start of the project logging")
    simpleFuzzer()
