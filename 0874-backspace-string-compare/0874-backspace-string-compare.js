/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var backspaceCompare = function(s, t) {
    let s1 = [];
    let s2 = [];
    for (let c of s) { //O(n)
        if (c === '#') {
            s1.pop();
        } else {
          s1.push(c);
        }
    }

    for (let c of t) { // O(m)
        if (c === '#') {
            s2.pop();
        } else {
          s2.push(c);
        }
    }
    if (s1.length !== s2.length) { return false; }
    while (s2.length > 0 && s1.length > 0) { // O(max(n,m))
        if (s2.pop() !== s1.pop()) return false;
    }
    return true;
};