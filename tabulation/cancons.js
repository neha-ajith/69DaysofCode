const canConstruct = (target,words) => {
    const table = Array(target.length + 1).fill(false);
    table[0] = true;
    for (let i=0; i<=target.length;i++){
        if(table[i] === true){
            for(let w of words){
                if(target.slice(i,i+w.length) === w){
                    table[i+w.length] = true;
                }
            }
        }
    }
    return table[target.length];
}

console.log(canConstruct('abcdef',['ab','abc','abcd','def','cd']))
console.log(canConstruct('skateboard',['s','k','t','ate','bo','boar']))
console.log(canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['e','ee','eee','eeee','eeeee','eeeeee']))
