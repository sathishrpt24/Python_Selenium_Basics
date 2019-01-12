a = 0;
b = 1;

try:
    b/a

except StopIteration as e:
    print("New error")

except 	ArithmeticError as e:
    print("This is arithmetic Error",e)

except Exception:
    print("Error")

else:
    print("Else Loop")

finally:
    print("Finally block is executed")