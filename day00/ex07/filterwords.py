#!/usr/local/bin/python3.7
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#   filterwords.py                                     :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#   By: abarthel <abarthel@student.42.fr>          +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#   Created: 2019/11/05 09:57:15 by abarthel          #+#    #+#              #
#   Updated: 2019/11/05 09:57:15 by abarthel         ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import re
import sys


if __name__ == '__main__':
    try:
        s = re.sub(r'[^\w\s]', '', sys.argv[1])
        s = re.split(" +", s)
        print([word for word in s if len(word) > int(sys.argv[2])])
    except ValueError:
        print('ERROR', end='\n')
