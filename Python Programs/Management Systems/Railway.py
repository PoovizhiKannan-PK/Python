import collections


class Passenger():
    id = 0

    def __init__(self, name, age, pref):
        self.name = name
        self.age = age
        self.pref = pref
        self.allocated = ""
        self.given = ""
        Passenger.id += 1
        self.id = Passenger.id

    def print_details(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("ID: ", self.id)
        if self.allocated == "T":
            print("Given Berth: ", self.given)
        else:
            print("Allocated: ", self.allocated)


class TicketBooker():
    u = collections.deque([i for i in range(1, 2)])
    l = collections.deque([i for i in range(1, 2)])
    m = collections.deque([i for i in range(1, 2)])
    r = collections.deque([i for i in range(1, 2)])
    w = collections.deque([i for i in range(1, 2)])

    booked = {}
    reserved = collections.deque()
    waiting = collections.deque()

    def __init__(self, p=None):
        if p != None:
            if len(TicketBooker.w) == 0:
                print("No tickets available\n")
            else:
                print(p.allocated)
                self.book_ticket(p)

    def book_ticket(self, p):
        if len(TicketBooker.u) > 0 or len(TicketBooker.m) > 0 or len(TicketBooker.l) > 0:
            if p.pref == "U" and len(TicketBooker.u) > 0:
                print("Preference Available \nTicket booked")
                p.given = str(TicketBooker.u.popleft()) + "U"
                p.allocated = "T"
                TicketBooker.booked[p.id] = p
            elif p.pref == "L" and len(TicketBooker.l) > 0:
                print("Preference Available \nTicket booked")
                p.given = str(TicketBooker.l.popleft()) + "L"
                p.allocated = "T"
                TicketBooker.booked[p.id] = p
            elif p.pref == "M" and len(TicketBooker.m) > 0:
                print("Preference Available \nTicket booked")
                p.given = str(TicketBooker.m.popleft()) + "M"
                p.allocated = "T"
                TicketBooker.booked[p.id] = p
            else:
                print("Preference Not Available")
                if len(TicketBooker.u) > 0:
                    p.given = str(TicketBooker.u.popleft()) + "U"
                elif len(TicketBooker.m) > 0:
                    p.given = str(TicketBooker.m.popleft()) + "M"
                else:
                    p.given = str(TicketBooker.l.popleft()) + "L"
                p.allocated = "T"
                TicketBooker.booked[p.id] = p
                print("Ticket Booked")
        elif len(TicketBooker.r) > 0:
            print("Ticket in Reserve")
            p.given = str(TicketBooker.r.popleft()) + "R"
            p.allocated = "R"
            TicketBooker.reserved.append(p)
        else:
            print("Ticket in Waiting")
            p.given = str(TicketBooker.w.popleft()) + "W"
            p.allocated = "W"
            TicketBooker.waiting.append(p)

    def booked_tickets(self):
        if len(TicketBooker.booked) > 0:
            for val in TicketBooker.booked:
                print(TicketBooker.booked[val].name)
                print(TicketBooker.booked[val].id)
                print(TicketBooker.booked[val].allocated)
                print("\n")

        else:
            print("No tickets booked\n")

    def cancel_tickets(self, id):
        if id not in TicketBooker.booked:
            print("Invalid Id")
        else:
            given = TicketBooker.booked[id].given
            given = given[-1]
            print(given)
            if given == "U":
                TicketBooker.u.append(len(TicketBooker.u)+1)
            elif given == "M":
                TicketBooker.m.append(len(TicketBooker.m)+1)
            elif given == "L":
                TicketBooker.l.append(len(TicketBooker.l)+1)
            del TicketBooker.booked[id]
            if len(TicketBooker.reserved) > 0:
                p = TicketBooker.reserved.popleft()
                TicketBooker.r.append(len(TicketBooker.r)+1)
                self.book_ticket(p)
            if len(TicketBooker.waiting) > 0:
                p = TicketBooker.waiting.popleft()
                TicketBooker.w.append(len(TicketBooker.w)+1)
                self.book_ticket(p)


if __name__ == "__main__":
    while True:
        print(" 1. Book \n 2. Cancel \n 3. Available Tickets \n 4. Booked Tickets \n 5. Exit \n")
        print("Enter Option: ")
        option = int(input())

        if option == 1:
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            pref = input("Enter Pref: ")

            p = Passenger(name, age, pref)
            TicketBooker(p)

        elif option == 2:
            val = int(input("Enter Your Id: "))
            booker = TicketBooker()
            booker.cancel_tickets(val)

        elif option == 3:
            print(3)
        elif option == 4:
            booker = TicketBooker()
            booker.booked_tickets()
        elif option == 5:
            break
        else:
            print("Invalid Option")
