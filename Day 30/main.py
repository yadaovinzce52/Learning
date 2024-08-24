# FileNotFound

try:
    file = open('a_file.txt')
    a_dict = {'key': 'value', 'wrong': 'right'}
except FileNotFoundError:
    file = open('a_file.txt', 'w')
    file.write('something')
except KeyError as error_message:
    print(f'The key {error_message} does not exist')
else:
    content = file.read()
    print(content)
finally:
    raise TypeError('This is an error that I made up')

height = float(input('Height: '))
weight = int(input('Weight: '))

if height > 3:
    raise ValueError('Human height should not be over 3 meters.')

bmi = weight / height ** 2

print(bmi)