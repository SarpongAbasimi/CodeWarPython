def spin_words(sentence):
    index=1
    my_array=[]
    while index < (len(sentence) + 1):
        my_array.append(sentence[(len(sentence)- index)])
        index += 1
    my_array="".join(my_array)
    return my_array



print(spin_words('sroirraw wollef yeH'))
