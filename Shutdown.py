def shutdown():
    choice = input("o you want to shutdown your computer: ")
    if choice == "Yes".lower():
        print("Shutdown")
    elif choice == "No".lower():
        print("Abort Shutdown")
    else:
        print("INVALID CHOICE")

shutdown()
    
    