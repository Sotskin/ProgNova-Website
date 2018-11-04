#!/usr/bin/env python2

import random

# A list containing the email addresses of the top 10 contestants in the Open division, ordered by ranks
open_list = [
  'Huaiyu Wu',
  'Nautilus Proc',
  'David Harmeyer',
  'Forbod Yadegarian',
  'Joshua Fair',
  'Daniel Moyer',
  'Jacob Magnuson',
  'Charles Bailey',
  'Derek Goodwin',
  'Mingyang Wang'
];

seed = ','.join(open_list)
random.seed(seed)

print 'seed:', seed

random.shuffle(open_list)
  
# Open division gift card raffle winners
open_gift_cards = open_list[:3]

print 'open raffle winners:', open_gift_cards
