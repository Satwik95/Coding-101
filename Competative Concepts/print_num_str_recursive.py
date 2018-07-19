def print_str(n):
    if n==0:
        return
    print_str(int(n/10))
    print(num_char[int(n%10)], end=" ")
    
num_char = {0:"Zero",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",
            6:"Six",7:"Seven",8:"Eight",9:"Nine"}
print_str(12345)

