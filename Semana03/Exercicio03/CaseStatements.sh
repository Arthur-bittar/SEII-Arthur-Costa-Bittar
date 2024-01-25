#!/bin/bash
case ${1,,} in
	Gabriel | gabriel | adm )
		            echo "Bem vindo!"
			    ;;
	help)
		echo "Escreva o nome correto"
		;;
	*)
		echo "Nome incorreto!"	
		;;						
esac
