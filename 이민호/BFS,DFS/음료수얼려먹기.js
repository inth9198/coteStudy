function ice(n, m, sourse){
    let answer = 0;
    const G = [];
    sourse.split('\n').forEach(ice => {
        ice = ice.split('').map(i => Number(i));
        G.push(ice);
      });

    function dfs(x, y) {
        if (x <= -1 || x >= n || y <= -1 || y >= m) {
            return false;
        }
        if (G[x][y] === 0) {
            G[x][y] = 1;
            dfs(x-1, y);
            dfs(x+1, y);
            dfs(x, y-1);
            dfs(x, y+1);
            return true;
        }
        return false;
    }
    for(let i = 0; i < n ; i++) {
        for(let j = 0; j < n ; j++) {
            if(dfs(i,j) === true)
                answer++;
        }
    }

    return answer;
}
const iceN = ice(15, 14, 
    '00000111100000\n11111101111110\n11011101101110\n11011101100000\n11011111111111\n11011111111100\n11000000011111\n01111111111111\n00000000011111\n01111111111000\n00011111111000\n00000001111000\n11111111110011\n11100011111111\n11100011111111');
console.log(iceN);
