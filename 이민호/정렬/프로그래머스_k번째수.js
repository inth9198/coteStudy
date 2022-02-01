function solution(array, commands) {
    var answer = [];
    for(let i=0; i < commands.length;i++)
    {
        let tmp=[];
        for(let j = commands[i][0] - 1; j <= commands[i][1] - 1;j++)
        {
            tmp.push(array[j]);
        }
        tmp.sort(function(a, b)  {
            return a - b;
          });
        answer.push(tmp[commands[i][2]-1])
    }
    return answer;
}
const a = solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]])
console.log(a);
