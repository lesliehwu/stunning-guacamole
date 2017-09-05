def compare(one,two): #one and two are the lists that are passed to the function
    same = bool
    if(len(one) == len(two)):
        for el in one:
            if el in two:
                same = True
            else:
                same = False
    else:
            same = False

    if(same == True):
        print("The lists are the same")
    if(same == False):
        print("The lists are not the same")

a_list_one = [1,2,5,6,2]
a_list_two = [1,2,5,6,2]

b_list_one = [1,2,5,6,5]
b_list_two = [1,2,5,6,5,3]

c_list_one = [1,2,5,6,5,16]
c_list_two = [1,2,5,6,5]

d_list_one = ['celery','carrots','bread','milk']
d_list_two = ['celery','carrots','bread','cream']

compare(a_list_one,a_list_two) #same
compare(b_list_one,b_list_two) #not same
compare(c_list_one,c_list_two) #not same
compare(d_list_one,d_list_two) #not same
