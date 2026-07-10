# spam detector keywords = "buy now", "Make Money", "Subscribe this"
a = input("Enter the message:")
p1 = "buy now"
p2 = "Make Money"
p3 = "Subscribe this"
if ((p1 in a) or (p2 in a) or (p3 in a)):
    print(f"This message is Spam, since it has {p1 or p2 or p3}")

else: 
    print("This is not a spam")