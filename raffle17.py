#!/usr/bin/env python2

import random

# A list containing the full names of the top 10 contestants (excluding top 3) in the ICPC division, ordered by ranks
icpc_list = [
  'Ankeet Parikh',
  'Rohit Motwani',
  'Thomas Guo',
  'Ronald Rojas',
  'Dayou Du',
  'Aldo Chow',
  'Yiqin Qiu'
];

# A list containing the email addresses of the top 10 contestants in the Open division, ordered by ranks
open_list = [
  'Antonio Molina',
  'Huaiyu Wu',
  'Peter Steele',
  'Tiancheng Jin',
  'Zeyu Zheng',
  'Adam Barth',
  'Godmar Back',
  'Roger Ballard',
  'Jacob Magnsuon',
  'Thomas Lidbetter'
];

seed = ','.join(icpc_list) + ';' + ','.join(open_list)
random.seed(seed)

print 'seed:', seed

random.shuffle(icpc_list)
random.shuffle(open_list)

# ICPC division gift card raffle winners
icpc_gift_cards = icpc_list[:3]
  
# Open division gift card raffle winners
open_gift_cards = open_list[:3]

print 'icpc raffle winners:', icpc_gift_cards
print 'open raffle winners:', open_gift_cards
