#!/bin/bash

Primeira_Lista=(um dois tres quatro cinco)

for item in ${Primeira_Lista[@]};
do
	echo -n $item | wc -c;
done

