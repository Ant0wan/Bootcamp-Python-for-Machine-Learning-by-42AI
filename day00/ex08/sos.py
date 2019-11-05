#!/usr/local/bin/python3.7
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#   sos.py                                             :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#   By: abarthel <abarthel@student.42.fr>          +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#   Created: 2019/11/05 10:41:47 by abarthel          #+#    #+#              #
#   Updated: 2019/11/05 10:41:47 by abarthel         ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import sys


mapping = {
    'A':'.-',
    'B':'-…',
    'C':'-.-.',
    'D':'-…',
    'E':'.',
    'F':'…-.',
    'G':'–.',
    'H':'….',
    'I':'…',
    'J':'.—',
    'K':'-.-',
    'L':'.-…',
    'M':'–',
    'N':'-.',
    'O':'—',
    'P':'.–.',
    'Q':'–.-',
    'R':'.-.',
    'S':'…',
    'T':'-',
    'U':'…-',
    'V':'…-',
    'W':'.–',
    'X':'-…-',
    'Y':'-.–',
    'Z':'–…',
    '1':'.----',
    '2':'…—',
    '3':'…–',
    '4':'….-',
    '5':'……',
    '6':'-….',
    '7':'–…',
    '8':'—…',
    '9':'----.',
    '0':'-----',
    ',':'–…--',
    '.':'.-.-.-',
    '?':'…–…',
    ' ':'-…-.',
    '-':'-….-',
    '[':'-.–.',
    ']':'-.–.-',
    ' ':' / '
    }

if __name__ == '__main__':
    s = []
    for i in sys.argv[1::]:
        s.append(i.upper())
    print(s)
    for key, value in mapping.items():
        morse = morse.replace(key, value)
        print(morse)
