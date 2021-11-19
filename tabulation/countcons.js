const countConstruct = (target,words) => {
    table = Array(target.length + 1).fill(0);
    table[0] = 1;
    for(let i=0;i<=target.length;i++){
        if(table[i]!=0){
            for(let w of words){
                if(target.slice(i,i+w.length) === w){
                    table[i+w.length] += table[i];
                }
            }
        }
    }
    return table[target.length];
}

console.log(countConstruct('abcdef',['ab','abc','abcd','def','cd','ef']))
console.log(countConstruct('skateboard',['s','k','t','ate','bo','boar']))
console.log(countConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['ef','ee','eee','eeee','eeeee','eeeeee']))
