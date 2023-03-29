def fahrenheit2celsius(fahrenheit): 
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius 
    
def what_to_wear(celsius):
    if celsius < -10:
        clothing = 'puffy jacket'
    elif -10 <= celsius < 0:
        clothing = 'scarf'
    elif 0 <= celsius < 10:
        clothing = 'sweater'
    elif 10 <= celsius < 20:
        clothing = 'light jacket'
    elif 20 <= celsius:
        clothing = 't-shirt'
    return clothing

celsius = fahrenheit2celsius(float(input('Enter temperature in fahrenheit: ')))
print('The temperature today is ' + '{:.1f}'.format(celsius) + ' degrees celsius, so you should wear a ' + what_to_wear(celsius))

# This function will be fruitful becuase it returns a value(the type of clothing)