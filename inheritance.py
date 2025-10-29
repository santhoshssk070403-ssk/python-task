#1
class per:
    def info(self, name, mail, mobile, address):
        print("\n--- personal information ---\n")
        print(f"name: {name}")
        print(f"email: {mail}")
        print(f"mobile: {mobile}")
        print(f"address: {address}")


class edu(per):
    def info(self, marks, total, percentage):
        print("\n--- educational information ---")
        print(f"marks: {marks}")
        print(f"total: {total}")
        print(f"percentage: {percentage}%")


edu = edu()
edu.info([85, 90, 80, 95, 88], 438, 87.6)


print("\n________*****2*****________\n")
#2

class per:
    def info(self, name, mail, mobile, address):
        print("\n--- personal information ---")
        print(f"name: {name}")
        print(f"email: {mail}")
        print(f"mobile: {mobile}")
        print(f"address: {address}")


class edu(per):
    def info(self, marks, total, percentage):
        print("\n--- educational information ---")
        print(f"marks: {marks}")
        print(f"total: {total}")
        print(f"percentage: {percentage}%")


class bank(edu):
    def info(self, acc_num, branch_name, bank_name, ifsc_code, available_balance):
        print("\n--- bank information ---")
        print(f"account number: {acc_num}")
        print(f"branch name: {branch_name}")
        print(f"bank name: {bank_name}")
        print(f"IFSC code: {ifsc_code}")
        print(f"available balance: ₹{available_balance}")

bank = bank()
bank.info("1234567890", "Main Branch", "SBI", "SBIN0000123", 15000.75)


print("\n________*****3*****________\n")
#3
class school:
    def info(self, name, mail, mobile, address):
        print("\n--- school information ---")
        print(f"name: {name}")
        print(f"email: {mail}")
        print(f"mobile: {mobile}")
        print(f"address: {address}")


class staff(school):
    def staffInfo(self, name, mail, mobile, address, dept):
        print("\n--- Staff Information ---")
        print(f"name: {name}")
        print(f"email: {mail}")
        print(f"mobile: {mobile}")
        print(f"address: {address}")
        print(f"department: {dept}")


class student(school):
    def studentInfo(self, name, mail, mobile, address, dept):
        print("\n--- student information ---")
        print(f"name: {name}")
        print(f"email: {mail}")
        print(f"mobile: {mobile}")
        print(f"address: {address}")
        print(f"department: {dept}")

choice = input("Are you a student or staff? ").strip().lower()

if choice == "student":
    s = student()
    s.studentInfo("leo", "leo@gmail.com", "9876543210", "kashmir", "cs")
elif choice == "staff":
    st = staff()
    st.staffInfo("naruto", "naruto@school.com", "9876501234", "leaf village", "hokaga")
else:
    print("Invalid choice! Please enter 'Student' or 'Staff'.")
