class Account:
    def __init__(self, name, amount):
        self.owner = name
        self.balance = amount
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("잔액 부족")
    
    def print_balance(self):
        print("잔액: ", self.balance)


owners = {}

while True:
    print("계좌개절/2 입금/2 출금/3 잔액조회/4")
    menu = int(input("메뉴 번호를 입력하세요 >>> "))

    if menu == 1:
        print("이름을 이미 입력한 고객께서는 이름 대신 _를 입력하시면 됩니다.")
        name, tmp = input().rstrip().split('/')
        print(name, tmp)
        balance = int(tmp)
        print(balance)
        if name in owners:
            print("계좌는 이미 계절되어 있습니다.")
        else:
            acc = Account(name, balance)
            owners[name] = acc

    elif menu == 2:
        print("이름을 이미 입력한 고객께서는 이름 대신 _를 입력하시면 됩니다.")
        name, tmp = input().rstrip().split('/')
        print(tmp)
        balance = int(tmp)
        
        if name not in owners:
            print("계좌를 먼저 개설하십시오.")
        else:
            acc = owners[name]
            acc.deposit(balance)
            print(owners[name])