
# Algeria
Algeria is a Python library that allows you to calculate the (clé) and (rip) of a given (ccp) CCP number account. It provides a simple and convenient way to obtain the clé and rip values for CCP accounts. Please note that additional features may be added to the library in the future.

Contributions are welcome! If you would like to contribute to the development of the Algeria library, feel free to submit pull requests or open issues on the GitHub repository.


## Instalation 
You can install the "algeria" library using pip:

```javascript
pip install algeria
```

## Usage

The CCP class provides methods to calculate the (clé) and (rip) for a given CCP account number.

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
print("Clé CCP:", cle)

rip = ccp_account.get_rip()
print("RIP:", rip)

rip_cle = ccp_account.get_rip_cle()
print("RIP Clé:", rip_cle)
```

The library was developed with the assistance of ChatGPT and the algorithms extracted from the web app provided [here](https://dzposte.netlify.app/).












## 🚀 About Me
A self-taught Python programmer who enjoys developing simple scripts, bots, and automation tools.