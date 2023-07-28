print('BMI  CALCULATOR')
while True:
    try:
        weight = float(input('YOUR WEIGHT (pound): '))
        break
    except ValueError:
        print('Try again')
while True:
    try:
        height = float(input('YOUR HEIGHT (inches): '))
        break
    except ValueError:
        print('Try again')
BMI = ((weight * 703) / height) / height
if BMI < 18.5:
    BMI_RANGE = "UNDERWEIGHT"
elif BMI < 25:
    BMI_RANGE = "HEALTHY"
elif BMI < 30:
    BMI_RANGE = "OVERWEIGHT"
else:
    BMI_RANGE = "OBESITY"
print('YOUR BMI:', BMI, 'YOUR RANGE:', BMI_RANGE)
