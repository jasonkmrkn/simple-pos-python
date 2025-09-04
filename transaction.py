from tabulate import tabulate
from rich import print
from enum import Enum
import string
import secrets


class Item(Enum):
    MOBIL = ("Mobil", 100_000_000)
    TEMPE = ("Tempe", 3_000)
    MIE_BURUNG_DARA = ("Mie Burung Dara", 5_000)
    SUSU_UHT_FULL_CREAM = ("Susu UHT Full Cream", 18500)
    BERAS_5KG = ("Beras 5kg", 65000)
    MINYAK_GORENG_2L = ("Minyak Goreng 2L", 35000)
    TELUR_AYAM_1KG = ("Telur Ayam 1kg", 28000)
    GULA_PASIR_1KG = ("Gula Pasir 1kg", 14000)
    MIE_INSTAN_ISI_5 = ("Mie Instan (isi 5)", 12000)
    TEH_CELUP_ISI_25 = ("Teh Celup (isi 25)", 7500)
    KOPI_BUBUK_200G = ("Kopi Bubuk 200g", 15000)
    SABUN_MANDI_BATANG = ("Sabun Mandi Batang", 4000)
    SHAMPO_BOTOL_170ML = ("Shampo Botol 170ml", 22000)
    PASTA_GIGI_120G = ("Pasta Gigi 120g", 12500)
    SAUS_TOMAT_BOTOL = ("Saus Tomat Botol", 11000)
    KECAP_MANIS_BOTOL = ("Kecap Manis Botol", 20000)
    ROTI_TAWAR = ("Roti Tawar", 16000)
    KEJU_CHEDDAR_165G = ("Keju Cheddar 165g", 25000)
    TEPUNG_TERIGU_1KG = ("Tepung Terigu 1kg", 13000)
    BISKUIT_KALENG = ("Biskuit Kaleng", 45000)
    AIR_MINERAL_1_5L = ("Air Mineral 1.5L", 6000)
    SABUN_CUCI_PIRING = ("Sabun Cuci Piring", 17000)
    DETERGEN_BUBUK_800G = ("Detergen Bubuk 800g", 24000)


class Transaction:

    def __init__(self, username):
        self.username = username
        self.transaction_id = generate_transaction_id()
        self.item_lists_with_total_price = []
        self.total_transaction_amount = 0

    
    def add_item(self, item:Item, item_qty):
        self.item_lists_with_total_price.append([item, item_qty, item.value[1] * item_qty])

    def update_item_qty(self, searched_item:Item, new_qty):
        for i, (item, qty, total_price) in enumerate(self.item_lists_with_total_price):
            if item == searched_item:
                self.item_lists_with_total_price[i][1] = new_qty
                self.item_lists_with_total_price[i][2] = new_qty * searched_item.value[1]
                break
    
    def change_item(self, item_searched:Item, new_item:Item):
        for i, (item, qty, total_price) in enumerate(self.item_lists_with_total_price):
            if item == item_searched:
                self.item_lists_with_total_price[i][0] = new_item
                self.item_lists_with_total_price[i][2] = qty * new_item.value[1]
                break

    def delete_item(self, item_searched:Item):
        for i, (item, qty, total_price) in enumerate(self.item_lists_with_total_price):
            if item == item_searched:
                self.item_lists_with_total_price.pop(i)
                break

    def reset_transaction(self):
        self.item_lists_with_total_price = []

    def check_transactions(self):
        order_list_header = ['NO', 'ITEM NAME', 'QUANTITY', 'PRICE / ITEM', 'TOTAL PRICE']
        order_list = []

        for i, (item, qty, total_price) in enumerate(self.item_lists_with_total_price):
            order_list.append([i, item.value[0], qty, item.value[1], total_price])
            self.total_transaction_amount += total_price
        
        order_list.append(['', '', '', 'TOTAL', self.total_transaction_amount])
        print(tabulate(order_list, headers=order_list_header, tablefmt='fancy_grid'))

    def check_discount(self):
        if self.total_transaction_amount > 500_000:
            self.total_transaction_amount *= (1 - 0.1)
            print("Anda mendapatkan diskon sebesar 10%")
        elif self.total_transaction_amount > 300_000:
            self.total_transaction_amount *= (1 - 0.08)
            print("Anda mendapatkan diskon sebesar 8%")
        elif self.total_transaction_amount > 200_000:
            self.total_transaction_amount *= (1 - 0.05)
            print("Anda mendapatkan diskon sebesar 5%")
        
        print(f"Total harga yang anda harus bayar adalah Rp {self.total_transaction_amount}")

    @classmethod
    def show_items_list(cls):
        item_list_header  = ['NO', 'ITEM NAME', 'ITEM PRICE']
        item_list_to_show = []
        for n, item in enumerate(Item):
            item_list_to_show.append([n, item.value[0], item.value[1]])

        print(tabulate(item_list_to_show, headers=item_list_header, tablefmt="fancy_grid"))



def generate_transaction_id(length = 10):
    """
    Generate random ID for each new transaction

    Args: 
        length (int): The desired length of the id, the default value is 10.

    Returns:
        str: random generated ID string.
    """

    chars = string.ascii_letters + string.digits
    id = ''.join(secrets.choice(chars) for i in range(length))

    return id