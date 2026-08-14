class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs: string[]): string {
        const encodedChars: string[] = [];
        for (const str of strs) {
            if (str === '') {
                encodedChars.push('300');
                continue;
            }
            let chars: string[] = [];
            for (const char of str) {
                chars.push(char.charCodeAt(0).toString().padStart(3, '0'));
            }
            encodedChars.push(chars.join('|'));
        }

        return encodedChars.join(',');
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str: string): string[] {
        if (str === '') return [];

        // [123|492|002, 029|212|009]
        const encodedWords = str.split(',');
        console.log('encodedWords:', encodedWords);

        // ["jak", "kwo"]
        const decodedWords: string[] = [];
        for (const encodedWord of encodedWords) {
            if (encodedWord === '300') {
                decodedWords.push('');
                continue;
            }
            const encodedChars = encodedWord.split("|");
            let decodedWord = '';
            for (const encodedChar of encodedChars) {
                const char = String.fromCharCode(Number(encodedChar));
                decodedWord += char;
            }
            decodedWords.push(decodedWord);
        }

        
        return decodedWords;
    }
}
