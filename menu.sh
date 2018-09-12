#!/bin/bash


clear
while :
do
echo " Escoja una opcion "
echo "1. calculadora"
echo "2. apagar"
echo "3. reiniciar"
echo "4. kernel"
echo "5. Salir"
echo -n "Seleccione una opcion [1 - 5]"
read opcion
case $opcion in

1) echo "calculadora:";
python calculadora.py;;
2) echo "se esta apagando:";
shutdown -h now;;
3) echo "se reiniciara";
shutdown -r now;;

4) echo "informacion del kernel";
cat /etc/*release;;

5) echo "agur";
exit 1;;



*) echo "$opc es una opcion invalida?";
echo "Presiona una tecla para continuar...";
read foo;;
esac
done
