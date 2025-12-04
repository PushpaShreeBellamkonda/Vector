// check whether min is first or max is first

var arr=[22,2,4,9,6]
var min=arr[0]
var max=arr[0]
var minind=0
var maxind=0
for (var i in arr){
    if (arr[i]<min){
        min=arr[i]
        minind=i
    }
    if (arr[i]>max){
        max=arr[i]
        maxind=i
    }
}
if (minind<maxind){
    console.log("Minimum number is first")
}
else{
    console.log("Maximum number is first")
}