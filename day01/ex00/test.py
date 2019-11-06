#!/usr/local/bin/python3.7
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#   test.py                                            :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#   By: abarthel <abarthel@student.42.fr>          +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#   Created: 2019/11/05 15:19:57 by abarthel          #+#    #+#              #
#   Updated: 2019/11/05 15:19:57 by abarthel         ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from recipe import Recipe
#from book import Book


if __name__ == '__main__':
#    x=Recipe()
#    print(x.name)
#    x.name = 'Cake'
#    print(x.name)
#    print()    
    y=Recipe('salad', 1, 121, [], 'Ok', 'sdfsafasf')
    print(y.name)
#    x.name = 21
#    print()    
#    e=Recipe(11)
#    print(e.name)
#    e.name = 21
#    exit()
