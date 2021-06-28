if __name__ == '__main__':
    f = open('text', 'r+')
    f.write('\n neue Zeile...')
    f.close()
    f = open('text', 'r+')
    print(f.read())
    f.close()





    #f = open('text', 'r')
    #for i in f:
        #print(i.replace('\n', ''))
