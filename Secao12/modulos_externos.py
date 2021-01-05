"""
Módulos externos

Utilizamos o gerenciador de pacotes Python chamado Pip - Python Installer Package

colorama -> Ele é utilizado para permitir impressão de textos coloridos no terminal.

from colorama import init, Fore, Back, Style
init()

print(Fore.RED + "Geek University")
print("Geek University")
print(Fore.GREEN + "Geek University")
print(Fore.YELLOW + "Geek University")
print(Style.DIM + "Geek University")
print(Style.RESET_ALL)
print(Back.GREEN + "Geek University")

"""
import pydf

pdf = pydf.generate_pdf("<h1>Thalisson Bandeira Araujo</h1><br/><strong>Nova linha</strong>")
with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)
