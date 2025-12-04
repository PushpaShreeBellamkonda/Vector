// check if array contains unique elements or not
let arr=[1,2,2,3,1,3,4]
let newarr=[]
for (var i of arr){
    if (!newarr.includes(i)){
        newarr.push(i)
    }
}
console.log(arr)
console.log(newarr)
if (newarr.length==arr.length){
    console.log("All are unique elements")
}
else{
    console.log("Duplicate elements found")
}