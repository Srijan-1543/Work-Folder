def most_frequent(string, output):
    count = 1
    for i in string:
        if i in output:
            output[i] += 1
        else:
    	    output[i] = 1
    print("Printing string in decreasing order of frequency: ")
    for i in output:
        if output[i]>count:
            count = output[i]
    while count>0 :

        for i in output:
            if output[i]==count:
                print(i," = ",output[i])
        count -=1


string = input("Enter the string: ")
output = {}

most_frequent(string, output)
