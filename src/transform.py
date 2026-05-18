import pandas as pd

def crear_dim_product(df_crudo: pd.DataFrame) -> pd.DataFrame:

    dim_product: pd.DataFrame = (
        df_crudo[["ProductID", "ProductCategory"]]
        .drop_duplicates()
        .reset_index(drop=True)
        .rename(
            columns={"ProductID":"Product_id", "ProductCategory":"Product_category"}
        )
        .assign(
            Product_key = lambda x: x.index + 1
        )
        [["Product_key", "Product_id", "Product_category"]]
    )

    return dim_product

def crear_dim_store(df_crudo: pd.DataFrame)-> pd.DataFrame:

    dim_store: pd.DataFrame = (
        df_crudo[["StoreLocation"]]
        .drop_duplicates()
        .reset_index(drop=True)
        .rename(
            columns={"StoreLocation":"Store_location"}
        )
        .assign(
            Store_key = lambda x: x.index + 1
        )
        [["Store_key", "Store_location"]]   
    )

    return dim_store

def crear_dim_payment(df_crudo: pd.DataFrame)-> pd.DataFrame:

    dim_payment: pd.DataFrame = (
        df_crudo[["PaymentMethod"]]
        .drop_duplicates()
        .reset_index(drop=True)
        .rename(
            columns={"PaymentMethod":"Payment_method"}
        )
        .assign(
            Payment_key = lambda x: x.index + 1
        )
        [["Payment_key", "Payment_method"]]
    )

    return dim_payment

def crear_dim_transactionDate(df_crudo: pd.DataFrame)-> pd.DataFrame:

    dim_transactionDate: pd.DataFrame = (
        df_crudo[["TransactionDate"]]
        .assign(
            TransactionDate = lambda x: pd.to_datetime(x["TransactionDate"], format='%m/%d/%Y %H:%M'), 
            Year = lambda x: x["TransactionDate"].dt.year, 
            Month = lambda x: x["TransactionDate"].dt.month, 
            Day = lambda x: x["TransactionDate"].dt.day
        )
        .drop_duplicates(subset=["Year", "Month", "Day"])
        .reset_index(drop=True)
        .assign(
            Date_key = lambda x: x.index + 1
        )
        [["Date_key", "Year", "Month", "Day"]]
    )

    return dim_transactionDate

def crear_dim_transactionTime(df_crudo: pd.DataFrame)-> pd.DataFrame:

    dim_transactionTime: pd.DataFrame = (
        df_crudo[["TransactionDate"]]
        .assign(        
            TransactionDate = lambda x: pd.to_datetime(x["TransactionDate"], format='%m/%d/%Y %H:%M'), 
            Hour = lambda x: x["TransactionDate"].dt.hour, 
            Min = lambda x: x["TransactionDate"].dt.minute
        )
        .drop_duplicates(subset=["Hour", "Min"])
        .reset_index(drop=True)
        .assign(
            Time_key = lambda x: x.index + 1
        )
        [["Time_key","Hour","Min"]]
    )

    return dim_transactionTime

def crear_fact_transactions(df_crudo: pd.DataFrame, dim_product: pd.DataFrame, dim_store: pd.DataFrame, dim_payment: pd.DataFrame, dim_transactionDate: pd.DataFrame, dim_transactionTime: pd.DataFrame)-> pd.DataFrame:

    fact_transactions: pd.DataFrame = (
        df_crudo
        .merge(dim_product, left_on=["ProductID","ProductCategory"], right_on=["Product_id","Product_category"], validate="m:1")
        .merge(dim_store, left_on=["StoreLocation"], right_on=["Store_location"], validate="m:1")
        .merge(dim_payment, left_on=["PaymentMethod"], right_on=["Payment_method"], validate="m:1")
        .assign(
            TransactionDate = lambda x: pd.to_datetime(x["TransactionDate"], format='%m/%d/%Y %H:%M'),
            Year = lambda x: x["TransactionDate"].dt.year,
            Month = lambda x: x["TransactionDate"].dt.month,
            Day = lambda x: x["TransactionDate"].dt.day,
            Hour = lambda x: x["TransactionDate"].dt.hour,
            Min = lambda x: x["TransactionDate"].dt.minute,
            Transaction_id = range(1, len(df_crudo) + 1)
        )
        .merge(dim_transactionDate, on=["Year", "Month", "Day"], validate="m:1")
        .merge(dim_transactionTime, on=["Hour", "Min"], validate="m:1")
        .rename(
            columns={"CustomerID":"Customer_id", "DiscountApplied(%)":"Discount_applied", "TotalAmount":"Total_amount", "TransactionDate":"Transaction_date"}
        )
        [["Transaction_id", "Customer_id", "Product_key", "Price", "Quantity", "Discount_applied", "Total_amount","Store_key","Transaction_date", "Date_key", "Time_key", "Payment_key"]]
    )
    
    return fact_transactions