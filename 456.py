password = 'a123456'
count = 3
while count > 0:
    test = input("輸入密碼 : ")
    if(test == password):
        print("登入成功")
        break
    else:
        count -= 1
        print("密碼錯誤! 還有" , count , "次機會")
        if count == 0:
            print("bye~")
            break
    


