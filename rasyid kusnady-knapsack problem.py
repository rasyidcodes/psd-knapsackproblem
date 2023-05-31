def max_calories(fruits, totalMoney):
    n = len(fruits)
    dp = [[0] * (totalMoney + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        currentFruit = fruits[i - 1]
        calories, price, stock = currentFruit['calories'], currentFruit['price'], currentFruit['stock']

        for j in range(1, totalMoney + 1):
            if price <= j:
                maxStock = min(stock, j // price)  # Ambil maksimal stok yang bisa dibeli dengan uang j
                for k in range(maxStock + 1):
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - k * price] + k * calories)
            dp[i][j] = max(dp[i][j], dp[i - 1][j])  # Tidak membeli buah ini

    return dp[n][totalMoney]


fruits = [
    {'name': 'apel', 'calories': 91, 'price': 2360, 'stock': 3},
    {'name': 'jeruk', 'calories': 71, 'price': 2120, 'stock': 3},
    {'name': 'pisang', 'calories': 105, 'price': 1890, 'stock': 5},
    {'name': 'kiwi', 'calories': 103, 'price': 3770, 'stock': 10},
    {'name': 'mangga', 'calories': 96, 'price': 2870, 'stock': 5}
]

totalMoney = 25000
result = max_calories(fruits, totalMoney)
print("Jumlah maksimal kalori yang bisa didapatkan oleh Pak Blangkon:", result)
# Jumlah maksimal kalori yang bisa didapatkan oleh Pak Blangkon: 1066