let arr=[3,4,34,6,23,98]
let newarr=[]
function isprime(n){
    if (n<=1){
        return false
    }
    for (var i=2;i<n;i++){
        if (n%i==0){
            return false
        }
    }
    return true
}
for (var j of arr){
    if(isprime(j)){
        newarr.push(j)
    }
}
console.log(newarr)