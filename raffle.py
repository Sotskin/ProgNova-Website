#!/usr/bin/env python2

import random

# A list containing the email addresses of the top 20 contestants (excluding top 3) in the ICPC division, ordered by ranks
icpc_list = ['a@a.edu', 'b@b.edu', 'c@c.edu'];

# A list containing the email addresses of the top 10 contestants in the Open division, ordered by ranks
open_list = ['a@a.edu', 'b@b.edu', 'c@c.edu'];

random.seed(','.join(icpc_list) + ';' + ','.join(open_list))

random.shuffle(icpc_list)
random.shuffle(open_list)

# ICPC division gift card raffle winners
icpc_gift_cards = icpc_list[:5]
  
# ICPC division book raffle winners
icpc_books = icpc_list[5:10]
  
# Open division gift card raffle winners
open_gift_cards = open_list[:3]
