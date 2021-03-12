// Generate Coin Change
// Change is inevitable (especially when breaking a twenty).

// Make generateCoinChange(cents).
// Accept a number of American cents, compute and print how to represent that amount with smallest number of coins. Common American coins are pennies (1 cent), nickels (5 cents), dimes (10 cents), and quarters (25 cents). Return the optimal configuration of coins in an object.

// Example output, given generateCoinChange(94), return
// { quarters:3, dimes:1, nickels:1, pennies:4}

// Make a function generateCoinChange(cents) that takes in cents and prints in smaller coins
// 

function generateCoinChange(cents){
    let change={
        'quarters': 0,
        'dimes': 0,
        'nickels': 0,
        'pennies': 0
    }
    while (cents > 4){
        if (cents >= 25){
            change.quarters++
            cents -=25
        }
        else if(cents >=10){
            change.dimes++
            cents -= 10
        }
        else if(cents >=5){
            change.nickels++
            cents -=5
        }
    }
    change.pennies = cents
    return change
}
console.log(generateCoinChange (243));