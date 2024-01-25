#!/bin/bash

if [ ${1,,} = gabriel ]; then
	echo "Bem vindo Gabriel!"
	return 0
elif [ ${1,,} = help ]; then
	echo "Digite o nome corretamente!"
	return 0
else 
	echo "Você não está permitido!"
	return 1
fi
	
