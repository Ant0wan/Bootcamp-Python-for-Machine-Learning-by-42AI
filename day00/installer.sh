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

curl -o /goinfre/miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
bash /goinfre/miniconda.sh -b -p /goinfre/miniconda
