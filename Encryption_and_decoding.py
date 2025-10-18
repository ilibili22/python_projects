# در این پروژه یک نسخه ساده رمزنگاری و رمزگشایی را ساختم 

while True:
    print("Program start:")
    print("\t1)Encryption:\n\t2)Decoding:\n\t3)Exit: ")
    
    question = input("choose one of these :")

    if question == "1":
        print("Encryption:")
        Encryption = input("Enter a sentence you want to Encryption : ")
        
        Encryption_saver = ""

        for ch in Encryption:
            x = ord(ch) *  15 + 23 - 43
            Encryption_saver += chr(x)

        print(f"Encryption: {Encryption_saver}")
    elif question == "2":
        print("Decoding:")
        Decoding = input("Enter a sentence you want to Decrypt : ")
        
        Decoding_saver = ""

        for ch in Decoding :
            x = (ord(ch) -23 + 43) // 15
            Decoding_saver += chr(x)
        
        print(f"Decoding: {Decoding_saver}")
    else:
        print("Goodbye👋\nyou can come here any time you want!")
        break