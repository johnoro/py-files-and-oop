from .Parallelepiped import Parallelepiped
from .Student import Student
from .BankAccount import BankAccount

def main():
    # Parallelepiped
    print("\nParallelepiped\n")
    parallelepiped = Parallelepiped(5, 10, 15)
    parallelepiped.display()
    print()

    # Student
    print("\nStudent\n")
    student = Student("John", 25, "405")
    student.display_student()
    print()

    # Bank Account
    print("\nBank Account\n")
    bank_account = BankAccount(1234, "John", 1000)
    bank_account.deposit(500)
    bank_account.withdraw(200)
    bank_account.bank_fee()
    bank_account.display()
    print()
