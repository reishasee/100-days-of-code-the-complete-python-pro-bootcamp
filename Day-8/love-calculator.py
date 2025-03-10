def calculate_love_score(name1, name2):
    true_list = ["t", "r", "u", "e"]
    true_total = 0
    love_list = ["l", "o", "v", "e"]
    love_total = 0
    
    for char in name1.lower():
        if char in true_list:
            true_total += 1
        
        if char in love_list:
            love_total += 1
            
    for char in name2.lower():
        if char in true_list:
            true_total += 1
            
        if char in love_list:
            love_total += 1 
            
    print(str(true_total) + str(love_total))
            
calculate_love_score("Kanye West", "Kim Kardashian")
