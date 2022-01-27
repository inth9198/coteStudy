function solution(number, k) {
    var answer = '';
    const stack = [];
    for(let i = 0; i < number.length; i++)
    {
        const n = number[i];
        while(k > 0 && stack.length > 0 && stack[stack.length - 1] < n)
        {
            stack.pop();
            k--;
        }
        stack.push(n)
    }
    stack.splice(stack.length - k, k);
    answer = stack.join("");
    return answer;
}
const r = solution("1924",2);
console.log(r);
