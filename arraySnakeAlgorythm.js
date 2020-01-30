var test_array = [
    [1, 2, 3, 48, 96],
    [4, 5, 6, 101, 201],
    [7, 8, 9, 555, 952],
    [10, 11, 12, 1599, 2788],

]

var result = []


for (let i = 0; i < test_array.length; i += 2) {
    result.push(test_array[i])
    result.push(test_array[i + 1].reverse())
    result = result.join().split(",").map(Number)

}

console.log(result)