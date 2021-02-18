import sha256 from 'crypto-js/sha256'

//加密
function encrypt(word){
    // var key = CryptoJS.enc.Utf8.parse("这里填加密的key");
    // var srcs = CryptoJS.enc.Utf8.parse(word);
    // var encrypted = CryptoJS.AES.encrypt(srcs, key, {mode:CryptoJS.mode.ECB,padding: CryptoJS.pad.Pkcs7});
    // return encrypted.toString();
    // let pwd = bcrypt.hashSync(word)
    // console.log(bcrypt.va)
    let pwd = sha256(word).toString()
    return pwd
}
// 解密
// function decrypt(word, hash){
//     let pwd = bcrypt.compareSync(word,hash)
//     return pwd
// }
export default {
    encrypt
}
