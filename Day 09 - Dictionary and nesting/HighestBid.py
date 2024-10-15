
all_bids_in = False
bids = {}
while not all_bids_in:
    name = input("Type the bidder's name : ")
    bid_amount = float(input("Type the bid amount : $"))
    bids[name] = bid_amount
    continue_bidding = input("Are there more bidders? Type 'yes' or 'no'").lower()
    if continue_bidding == 'no':
        all_bids_in = True

print(bids)
winning_bid = 0
bid_winner =  ""
for name in bids:
   if bids[name] > winning_bid:
       winning_bid = bids[name]
       bid_winner = name


print(bid_winner, winning_bid)