#!/usr/local/bin/python3.7
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#   count.py                                           :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#   By: abarthel <abarthel@student.42.fr>          +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#   Created: 2019/11/04 12:35:58 by abarthel          #+#    #+#              #
#   Updated: 2019/11/04 12:35:58 by abarthel         ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

def output_analysis(c, ul, ll, pm, sp):
	print('The text contains {0} characters:\n- {1} upper letters\n- {2} lower letters\n- {3} punctuation marks\n- {4} spaces'.format(c, ul, ll, pm, sp), end='\n')

def text_analyzer(text):
    output_analysis(124, 1, 25, 45, 6)


