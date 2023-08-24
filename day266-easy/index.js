const {readFileSync} = require('fs')

/**
 * @param {string} word your input word
 * @param {string[]} dictionnary list of words for the program to work on
 * @returns {string[]} the step words
 */
function get_anagram(word, dictionnary) {
    return dictionnary
        .filter(it => it.length == word.length +1 )
        .filter(it => orderedLetters(it).includes(orderedLetters(word)))
}

/**
 * @param {string} word 
 * @returns {string}
 */
function orderedLetters(word) {
    return word.split('').sort().join()
}

const words_reference = readFileSync('words_alpha.txt').toString().split("\r\n")

console.log(get_anagram("apple", words_reference))