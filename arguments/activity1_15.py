#tip, the waiter
def total_calc(bill_amnt, tip_perc):
    #define function to calculate tip on bill.
    total= bill_amnt*(1+ 0.01*tip_perc)
    total= round(total, 2)
    print("Please pay $",total)
    print(f"please pay ${total}")
total_calc(150,20)