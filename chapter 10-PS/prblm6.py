from random import randint

class train():

    def __init__(self, trainNo):
        self.trainNo = trainNo
    def book_a_ticket(self , fro,to):
        print(f"Ticket is booked in train no.:{self.trainNo} from {fro} to {to}")
    def get_status(self):
        print(f"The train {self.trainNo} is running on time")
    def get_info(self,fro,to):
        print(f"Ticket fare of train no.:{self.trainNo} from {fro} to {to} is {randint(1,555)}")

t = train(233)
t.book_a_ticket("Rampur","Indi")
t.get_status()
t.get_info("Rampur", "Indi")


#self ke sivaay kuch aur bhi use karr skate hai but not a good practice