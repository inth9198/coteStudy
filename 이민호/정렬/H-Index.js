function solution(citations) {
    var answer = 0;
    citations.sort((a,b) => (b-a));
    console.log(citations);
    for(let i = 0; i < citations.length; i++)
    {
        if (answer < Math.min(citations[i],i+1))
        {
            answer = Math.min(citations[i],i+1);
        }
    }

    return answer;
}
