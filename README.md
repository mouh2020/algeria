
# Algeria 🇩🇿
Algeria is a Python library that allows you to calculate the (clé) and RIP (Relevé d'Identité Postal) of a given CCP (Compte de Chèque Postal) number account. It provides a simple and convenient way to obtain the clé and rip values for CCP accounts. Please note that additional features may be added to the library in the future. You can check features section for any updates.

Contributions are welcome! If you would like to contribute to the development of the Algeria library, feel free to submit pull requests or open issues on the GitHub repository.

## Features 💡

- Clé (Compte de Chèque Postal) calculation.
- RIP (Relevé d'Identité Postal) calculation.
- RIP's Clé calculation.
- Deposit fees calculation
- Checkout fees calculation


## Instalation 📌
You can install the "algeria" library using pip:

```javascript
pip install algeria
```

## Usage 📚

The CCP class provides methods to calculate the (clé) and (RIP) for a given CCP account number.

 - Initialization 

To create an instance of the CCP class, pass the CCP account number as a string to the constructor:
```javascript
from algeria.ccp import CCP

ccp_account = CCP("1234567890")
```

- Calculating the clé

To calculate the clé of the CCP account, use the get_cle method:

```javascript
cle = ccp_account.get_cle()

print("Clé CCP:", cle)
```

- Calculating the rip

To calculate the rip of the CCP account, including the first 8 digits "00799999", use the get_rip method:

```javascript
rip = ccp_account.get_rip()

print("RIP:", rip)
```

 - Calculating the cle of the rip

To calculate only the clé of the rip, use the get_rip_cle method:

```javascript
rip_cle = ccp_account.get_rip_cle()

print("RIP Clé:", rip_cle)
```

## Example

Here's an example demonstrating the usage of the "algeria" library :

```javascript
from algeria.ccp import CCP

ccp_account = CCP("1234567890")

cle = ccp_account.get_cle()
print("Clé CCP:", cle) // 45

rip = ccp_account.get_rip()
print("RIP:", rip) // 0079999912345678906

rip_cle = ccp_account.get_rip_cle()
print("RIP Clé:", rip_cle) // 06
```

The Transaction class provides methods to calculate the fees of a deposit or checkout ammount.

 - Initialization 

To create an instance of the Transaction class, pass the amount as a float to the constructor:
```javascript
from algeria.ccp import Transaction

transaction = Transaction(2000000)
```

- Calculating the fees of a deposit transaction

To calculate the fees of a deposit transaction, use the get_deposit_fees method:

```javascript
transaction_fees = transaction.get_deposit_fees()

print("Deposit fees:", transaction_fees)
```

- Calculating the fees of a checkout transaction

To calculate the fees of a checkout transaction, use the get_checkout_fees method:

```javascript
checkout_fees = transaction.get_checkout_fees()

print("Checkout fees:", checkout_fees)
```


## Example

Here's an example demonstrating the usage of the "algeria" library :

```javascript
from algeria.ccp import CCP,Transaction

ccp_account = CCP("1234567890")

cle = ccp_account.get_cle()
print("Clé CCP:", cle) // 45

rip = ccp_account.get_rip()
print("RIP:", rip) // 0079999912345678906

rip_cle = ccp_account.get_rip_cle()
print("RIP Clé:", rip_cle) // 06



transaction = Transaction(2000000)

deposit_fees = transaction.get_deposit_fees()
print("Deposit fees:", deposit_fees)   // 4818

checkout_fees = transaction.get_checkout_fees()
print("Checkout fees:", checkout_fees) // 9018

```


## Note 💡

The algorithms extracted from the web app provided [here](https://dzposte.netlify.app/) after testing them.












## 🚀 About Me
A self-taught Python programmer who enjoys developing simple scripts, bots, and automation tools.
