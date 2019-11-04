#!/bin/bash
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    launch.sh                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abarthel <abarthel@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/04 09:09:25 by abarthel          #+#    #+#              #
#    Updated: 2019/11/04 09:09:25 by abarthel         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

if [ -d "/goinfre/miniconda" ]
then
	env PATH="/goinfre/miniconda/bin:$PATH" bash
else
	printf "Failure: Miniconda could not be found.\n"
fi
