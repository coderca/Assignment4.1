
print('i will always run')
print(f'{__name__}')
def main():
    print('i am main fucntion in first program')

def sub():
    print('i will only run during import')

if __name__ == '__main__':
    main()
else:
    sub()

    
# __name__ = 'firstpgm'
# __name__ = '__main__' = wile running directly