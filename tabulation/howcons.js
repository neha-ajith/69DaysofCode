const howConstruct = (target,words) => {
    const table = Array(target.length+1)
    .fill()
    .map(() => []);

    table[0] = [[]];

    for(let i=0;i<=target.length;i++){
        for(let w of words){
            if(target.slice(i,i+w.length === w)){
                const newCombinations = table[i].map(subArray => [ ...subArray, w]);
                table[i+w.length].push(...newCombinations);
            }
        }
    }
    return table[target.length];
}

console.log(howConstruct('abcdef',['ab','abc','abcd','def','cd','ef']))
console.log(howConstruct('skateboard',['s','k','t','ate','bo','boar']))
console.log(howConstruct('eeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeeeeeeeeeef',['e','ee','eee','eeee','eeeee','eeeeee']))
// console.log()
