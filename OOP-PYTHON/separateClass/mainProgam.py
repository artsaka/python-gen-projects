from accounting import Accounting
from programmer import Programmer
from sale import Sale


if __name__ == "__main__":
    account = Accounting("Jinda", 30000, 37)
    print(f"บัญชี รายได้ต่อปี {str(account._getIncome(3000, 20000))}")

    programmer = Programmer("ArMac", 50000,5, 47)
    print(f"โปรแกรมเมอร์ รายได้ต่อปี {str(programmer._getIncome())}")

    sale = Sale("Natto", 35000, "Bangkok")
    print(f"ฝ่ายขาย รายได้ต่อปี {sale._getIncome(20000, 35000)}")