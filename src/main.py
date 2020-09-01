import math
from collections import Counter
from checkout_system.validators import check_bogo, check_appl, check_chmk, check_apom


f = open("input.txt", "r")

price_list = {
    "CH1": 3.11,
    "AP1":  6.00,
    "CF1": 11.23,
    "MK1":  4.75,
    "OM1": 3.69
}


for line in f:

    # Initializing the values
    total_price = 0.0
    bogo_price, chmk_price, appl_price, apom_price = 0.0, 0.0, 0.0, 0.0
    bogo, chmk, appl, apom = False, False, False, False

    line = line.strip("\n")
    items = [i.strip(" ") for i in line.split(",")]
    values = dict(Counter(items))

    # Get the all the products in list
    basket_items = values.keys()

    '''
        1 - Validate Product item is available in basket 
        2 - Based on the items available in basket, validate the Discount or Special Offers
    '''
    if "CF1" in basket_items:
        bogo = check_bogo(values["CF1"])

    if "AP1" in basket_items:
        appl = check_appl(values["AP1"])

    if "CH1" in basket_items and "MK1" in basket_items:
        chmk = check_chmk(values["CH1"], values["MK1"])

    if "OM1" in basket_items and "AP1" in basket_items:
        apom = check_apom(values["OM1"], values["AP1"])

    '''
        Based on the Offer eligiblity, get the total eligible discount amount
    '''
    if bogo:
        bogo_price = math.ceil(values["CF1"]/2)*price_list["CF1"]

    if appl:
        appl_price = 1.50 * values["AP1"]

    if chmk:
        chmk_price = 4.75

    if apom:
        if values["OM1"] > values["AP1"]:
            apom_price = (price_list["AP1"]/2) * values["AP1"]

        if values["OM1"] <= values["AP1"]:
            apom_price = (price_list["AP1"]/2) * values["OM1"]

    # Get the total pricible amount
    for i in basket_items:
        total_price = total_price + (price_list[i]*values[i])

    # Check best discountable amount from APPL and APOM Offers
    if apom_price > appl_price:
        total_price = total_price - bogo_price - chmk_price - apom_price
    else:
        total_price = total_price - bogo_price - chmk_price - appl_price

    print("`````````")
    print("Basket: ", line)
    print("Total price expected: ", total_price)
    print("`````````\n")
