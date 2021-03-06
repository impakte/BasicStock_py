from Tkinter import *
import tkMessageBox
import ttk
import sqlite3
import datetime
import tkFont
import ttk

W_main = Tk()
W_main.geometry("1200x800")
W_main.title("BASICSTOCK")

db = sqlite3.connect('basicstock.db')
cursor = db.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS stock(
     id integer PRIMARY KEY AUTOINCREMENT UNIQUE,
     barecode text,
     societycode text,
     description text,
     Quantity integer,
     buyprice real,
     estimateprice real,
     provider text,
     weight real,
     date text
)""")
db.commit()
            
def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def RepresentsFloat(s):
    try: 
        float(s)
        return True
    except ValueError:
        return False

def enter_product(barecode, E_societycode, E_description, E_quantity, E_buyprice, E_estimateprice, E_provider, E_weight, window):
    product = {"barecode" : barecode,
               "societycode" : E_societycode.get(),
               "description" : E_description.get(),
               "Quantity" : int(E_quantity.get()),
               "buyprice" : float(E_buyprice.get()),
               "estimateprice" : float(E_estimateprice.get()),
               "provider" : E_provider.get(),
               "weight" : float(E_weight.get()),
               "date" : str(datetime.datetime.now().date())
               }
    cursor.execute("""
    INSERT INTO stock(barecode, societycode, description, Quantity, buyprice, estimateprice, provider, weight, date) VALUES(:barecode, :societycode, :description, :Quantity, :buyprice, :estimateprice, :provider, :weight, :date)""", product)
    cursor.execute("""SELECT barecode, societycode, description, Quantity, buyprice, estimateprice, provider, weight, date FROM stock""")
    db.commit()
    for row in cursor:
        print('{0} : {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}'.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
    window.destroy()
    return
    
def check_allentries(barecode, E_societycode, E_description, E_quantity, E_buyprice, E_estimateprice, E_provider, E_weight, W_newproduct):
    if not E_societycode.get():
        L_error = Label(W_newproduct, text="Le champ Code de soci�t� n'a pas �t� rempli.")
        L_error.place(x=10, y=325)
        return
    if not E_description.get():
        L_error = Label(W_newproduct, text="Le champ description n'a pas �t� rempli.")
        L_error.place(x=10, y=325)
        return
    if not E_quantity.get():
        L_error = Label(W_newproduct, text="Le champ quantit� n'a pas �t� rempli.")
        L_error.place(x=10, y=325)
        return
    if not E_estimateprice.get():
        L_error = Label(W_newproduct, text="Le champ prix estim� n'a pas �t� rempli.")
        L_error.place(x=10, y=325)
        return
    if not E_provider.get():
        L_error = Label(W_newproduct, text="Le champ fournisseur n'a pas �t� rempli.")
        L_error.place(x=10, y=325)
        return
    if not E_weight.get():
        L_error = Label(W_newproduct, text="Le champ poid n'a pas �t� rempli.")
        L_error.place(x=10, y=325)
        return
    if not E_buyprice.get():
        L_error = Label(W_newproduct, text="Le champ Prix d'achat n'a pas �t� rempli.")
        L_error.place(x=10, y=325)
        return
    if (RepresentsInt(E_quantity.get()) == False):
        L_error = Label(W_newproduct, text="Le champ Quantit� n'est pas un nombre entier.")
        L_error.place(x=10, y=325)
        return
    elif (RepresentsFloat(E_buyprice.get()) == False):
        L_error = Label(W_newproduct, text="Le champ Prix d'achat n'est pas un nombre entier.")
        L_error.place(x=10, y=325)
        return
    elif (RepresentsFloat(E_estimateprice.get()) == False):
        L_error = Label(W_newproduct, text="Le champ Prix estim� n'est pas un nombre entier.")
        L_error.place(x=10, y=325)
        return
    elif (RepresentsFloat(E_weight.get()) == False):
        L_error = Label(W_newproduct, text="Le champ Poids n'est pas un nombre entier.")
        L_error.place(x=10, y=325)
        return
    else:
        print "Toutes les conditions sont valide"
        enter_product(barecode, E_societycode, E_description, E_quantity, E_buyprice, E_estimateprice, E_provider, E_weight, W_newproduct)
        return

def display_newproduct_window(barecode):
    W_newproduct = Tk()
    W_newproduct.geometry("600x350")
    W_newproduct.title("Nouveau Produit")
    
    L_societycode = Label(W_newproduct, text="Code soci�t�:")
    L_societycode.place(x=10, y=10)
    E_societycode = Entry(W_newproduct)
    E_societycode.place(x=85, y=10)

    L_description = Label(W_newproduct, text="Description:")
    L_description.place(x=10, y=50)
    E_description = Entry(W_newproduct, width=70)
    E_description.place(x=85, y=50)

    L_quantity = Label(W_newproduct, text="Quantit�:")
    L_quantity.place(x=10, y=90)
    E_quantity = Entry(W_newproduct)
    E_quantity.place(x=85, y=90)

    L_buyprice = Label(W_newproduct, text="Prix d'achat:")
    L_buyprice.place(x=10, y=130)
    E_buyprice = Entry(W_newproduct)
    E_buyprice.place(x=85, y=130)

    L_estimateprice = Label(W_newproduct, text="Prix de vente estim�:")
    L_estimateprice.place(x=10, y=170)
    E_estimateprice = Entry(W_newproduct)
    E_estimateprice.place(x=85, y=170)

    L_provider = Label(W_newproduct, text="Fournisseur:")
    L_provider.place(x=10, y=210)
    E_provider = Entry(W_newproduct)
    E_provider.place(x=85, y=210)

    L_weight = Label(W_newproduct, text="poid (en Kg):")
    L_weight.place(x=10, y=250)
    E_weight = Entry(W_newproduct)
    E_weight.place(x=85, y=250)
    
    B_validation = Button(W_newproduct, bg = "White", text="Valider",
        command= lambda: check_allentries(barecode, E_societycode, E_description, E_quantity, E_buyprice, E_estimateprice, E_provider, E_weight, W_newproduct))
    B_validation.place(x=275, y=290)

def update_quantity(barecode, quantity, window):
    cursor.execute("""SELECT Quantity FROM stock WHERE barecode=?""", (barecode,))
    currentQuantity = cursor.fetchone()
    newQuantity = currentQuantity[0] + int(quantity)
    cursor.execute("""UPDATE stock SET Quantity = ? WHERE barecode = ?""", (newQuantity, barecode,))
    db.commit()
    window.destroy()
    
def display_addquantity_window(barecode, window):
    W_addquantity_window = Tk()
    W_addquantity_window.geometry("400x100")
    W_addquantity_window.title("Ajouter une quantit�e")
    L_quantity = Label(W_addquantity_window, text="Quantit�:")
    L_quantity.place(x=5, y=20)
    E_quantity=Entry(W_addquantity_window)
    E_quantity.place(x=120, y=20)
    B_validation = Button(W_addquantity_window, bg = "White", text="Valider",
                          command= lambda: update_quantity(barecode, E_quantity.get(), W_addquantity_window))
    B_validation.place(x=140, y=60)
    window.destroy()
    
def recreate_product(barecode, buyprice, window):
    cursor.execute("""SELECT societycode, description, Quantity, estimateprice, provider, weight FROM stock WHERE barecode=?""", (barecode,))
    knownProduct = cursor.fetchone()
    product = {"barecode" : barecode,
               "societycode" : knownProduct[0],
               "description" : knownProduct[1],
               "Quantity" : int(knownProduct[2]),
               "buyprice" : float(buyprice),
               "estimateprice" : float(knownProduct[3]),
               "provider" : knownProduct[4],
               "weight" : float(knownProduct[5]),
               "date" : str(datetime.datetime.now().date())
               }
    cursor.execute("""
    INSERT INTO stock(barecode, societycode, description, Quantity, buyprice, estimateprice, provider, weight, date) VALUES(:barecode, :societycode, :description, :Quantity, :buyprice, :estimateprice, :provider, :weight, :date)""", product)
    db.commit()
    window.destroy()
    
def update_price(barecode, window):
    W_updateprice_window = Tk()
    W_updateprice_window.geometry("400x100")
    W_updateprice_window.title("R�enregistrer ce produit")
    L_buyprice = Label(W_updateprice_window, text="Prix d'achat:")
    L_buyprice.place(x=5, y=20)
    E_buyprice=Entry(W_updateprice_window)
    E_buyprice.place(x=120, y=20)
    B_validation = Button(W_updateprice_window, bg = "White", text="Valider",
                          command= lambda: recreate_product(barecode, E_buyprice.get(), W_updateprice_window))
    B_validation.place(x=140, y=60)
    window.destroy()
    
def display_knownproduct_window(barecode):
    W_knownproduct_window = Tk()
    W_knownproduct_window.geometry("400x100")
    W_knownproduct_window.title("Produit connu")
    B_addquantity = Button(W_knownproduct_window, bg="White", text="Ajouter une quantit�",
                           command= lambda: display_addquantity_window(barecode, W_knownproduct_window))
    B_addquantity.place(x=50, y=50)
    B_addsameproduct = Button(W_knownproduct_window, bg="White", text="R�enregistrer ce produit",
                              command = lambda: update_price(barecode, W_knownproduct_window))
    B_addsameproduct.place(x=250, y=50)
        
def check_product(barecode, window):
    print barecode
    id = 2
    cursor.execute("""SELECT barecode FROM stock WHERE barecode=?""", (barecode,))
    response = cursor.fetchone()
    print response
    window.destroy()
    if (response == None):
        display_newproduct_window(barecode)
    else:
        display_knownproduct_window(barecode)
    return

def display_addproduct_window():
    product_open = True
    W_product = Tk()
    W_product.geometry("400x100")
    W_product.title("Produit")
    L_title_addproduct = Label(W_product, text="Enregistrer un produit")
    L_title_addproduct.pack()
    L_barcode = Label(W_product, text="Entrer le code barre :")
    L_barcode.place(x=5, y=20)
    E_barecode=Entry(W_product)
    E_barecode.place(x=120, y=20)
    B_validation = Button(W_product, bg = "White", text="Valider",
                          command= lambda: check_product(E_barecode.get(), W_product))
    B_validation.place(x=140, y=60)

def display_stock_window():
    W_Stock = Tk()
    W_Stock.geometry("1400x800")
    W_Stock.title("Stock")
    label = Label(W_Stock, text="Stock")
    label.place(x=550, y=10)
    cursor.execute("""SELECT barecode, societycode, description, Quantity, buyprice, estimateprice, provider, weight, date FROM stock""")
    #db.commit()
    listbox = ttk.Treeview(W_Stock, height = 35, columns=('barecode', 'societycode', 'description', 'Quantity', 'buyprice', 'estimateprice', 'provider', 'weight', 'date'))
    listbox.column('barecode', width=100, anchor='center')
    listbox.heading('barecode', text='Code Barre')
    listbox.column('societycode', width=100, anchor='center')
    listbox.heading('societycode', text='Code Societe')
    listbox.column('description', width=200, anchor='center')
    listbox.heading('description', text='Description')
    listbox.column('Quantity', width=100, anchor='center')
    listbox.heading('Quantity', text='Quantit�e')
    listbox.column('buyprice', width=100, anchor='center')
    listbox.heading('buyprice', text='Prix achat')
    listbox.column('estimateprice', width=100, anchor='center')
    listbox.heading('estimateprice', text='Prix Minimum')
    listbox.column('provider', width=100, anchor='center')
    listbox.heading('provider', text='Fournisseur')
    listbox.column('weight', width=100, anchor='center')
    listbox.heading('weight', text='Poids')
    listbox.column('date', width=100, anchor='center')
    listbox.heading('date', text='Date')
    listbox.place(x=10, y=10)
    i = 0
    for row in cursor:
        listbox.insert('', 'end', text=i, values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
        i += 1

def display_finance_window():
    W_finance = Tk()
    W_finance.geometry("1400x800")
    W_finance.title("Finance")
    cursor.execute("""SELECT barecode, societycode, description, Quantity, buyprice, estimateprice, provider, weight, date FROM stock""")
    stockbuyvalue = 0
    for row in cursor:
        stockbuyvalue += row[4]
    L_StockBuyValue = Label(W_finance, text="Valeur d'achat du stock :" + str(stockbuyvalue) + "�")
    L_StockBuyValue.pack()
    
def display_main_window():
    label = Label(W_main, text="BasicStock")
    label.place(x=550, y=10)
    B_Product = Button(W_main, bg="White", text="Ajouter un produit", command=display_addproduct_window)
    B_Product.place(x = 100, y=300)
    B_Stock = Button(W_main, bg="White", text="Afficher le tableau des Stocks", command=display_stock_window)
    B_Stock.place(x = 100, y=600)
    B_Finance = Button(W_main, bg ="White", text="Finance", command=display_finance_window)
    B_Finance.place(x=500, y = 400)


display_main_window()

W_main.mainloop()
