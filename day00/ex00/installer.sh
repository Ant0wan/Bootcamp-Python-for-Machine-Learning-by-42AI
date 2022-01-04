#!/bin/bash
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    installer.sh                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abarthel <abarthel@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/04 09:09:25 by abarthel          #+#    #+#              #
#    Updated: 2019/11/04 09:09:25 by abarthel         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

function install_python()
{
	curl -o /goinfre/miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
	if [ $? -ne 0 ]
	then
		printf "Failure: could not download miniconda.\n"
		exit()
	fi
	bash /goinfre/miniconda.sh -b -p /goinfre/miniconda
	if [ $? -eq 0 ]
	then
		printf "Python has been installed.\n"
	else
		printf "Failure: Python could not be installed.\n"
		exit()
	fi
}

install_python
