#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#   kata03.py                                          :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#   By: abarthel <abarthel@student.42.fr>          +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#   Created: 2019/11/04 18:22:53 by abarthel          #+#    #+#              #
#   Updated: 2019/11/04 18:22:53 by abarthel         ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

phrase = "The right format"

if __name__ == '__main__':
    print('{0:->42}'.format(phrase), end='')
