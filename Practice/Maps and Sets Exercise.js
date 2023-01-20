1,2,3,4,
ref

{Array(3) => true}
{Array(3) => false}

const hasDuplicate = arr => new Set(arr).size !== arr.length

function vowel(char){
    return "aeiouy".includes(char);
}
function count(str){
    const vowelMap = new Map();
    for(let char of str){
        let lowerCaseChar = char.toLowerCase()
        if(isVowel(lowerCaseChar)){
            if(vowelMap.has(lowerCaseChar)){
                vowelMap.set(lowerCaseChar, vowelMap.get(lowerCaseChar) +1);
            } else {
                vowelMap.set(lowerCaseChar, 1);
            }
        }
    }
    return vowelMap;
}
