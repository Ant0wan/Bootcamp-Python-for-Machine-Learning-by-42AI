#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#   kata00.py                                          :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#   By: abarthel <abarthel@student.42.fr>          +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#   Created: 2019/11/04 17:36:52 by abarthel          #+#    #+#              #
#   Updated: 2019/11/04 17:36:52 by abarthel         ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

t = (19, 42, 21)

if __name__ == '__main__':
    print('The {0} numbers are:\
 {1}'.format(len(t), ', '.join(str(i) for i in t)), end='\n')
