def main():
    coke_value = 50
    total_inserted = 0
    
    while coke_value > total_inserted:
        total_inserted += get_coin()
        if total_inserted < coke_value:
            print('Amount Due:', coke_value - total_inserted)
            

    print("Changed owned:", total_inserted - coke_value)

def get_coin():
    coin = input("Insert Coin: ").strip()
    coin = int(coin)
    accpeted_coins = [25, 10 , 5]
    if coin in accpeted_coins:
        return coin
    return 0

main()