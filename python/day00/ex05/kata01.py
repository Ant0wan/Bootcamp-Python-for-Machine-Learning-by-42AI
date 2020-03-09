#!/usr/local/bin/python3.7
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#   kata01.py                                          :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#   By: abarthel <abarthel@student.42.fr>          +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#   Created: 2019/11/04 17:55:28 by abarthel          #+#    #+#              #
#   Updated: 2019/11/04 17:55:28 by abarthel         ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
    }

if __name__ == '__main__':
    for key, val in languages.items():
        print(key, 'was created by', val, sep=' ', end='\n')
