def is_leap(year):
    
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

    return leap
    
#year = int(input())
    
    # Write your logic here
    


year = int(input())
print(is_leap(year))
