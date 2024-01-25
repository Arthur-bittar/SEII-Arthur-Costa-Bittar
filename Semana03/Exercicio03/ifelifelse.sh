#!/bin/bash

if [ ${1,,} = gabriel ]; then
	echo "Bem vindo Gabriel!"
elif [ ${1,,} = help ]; then
	echo "Digite o nome corretamente!"
else 
	echo "Você não está permitido!"
fi
	
