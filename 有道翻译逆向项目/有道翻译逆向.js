var CrytoJS = require('crypto-js')

function aes_decode(content) {
  return CrytoJS.AES.decrypt(content)
}

function md5_func(content) {
  return CrytoJS.MD5(content).toString()
}

function b(e, t) {
  return md5_func(`client=${'fanyideskweb'}&mysticTime=${e}&product=${'webfanyi'}&key=${t}`)
}

function f() {
  var e = 'fsdsogkndfokasodnaso'
  const t = (new Date).getTime();
  return JSON.stringify({
      sign: b(t, e),
      client: 'fanyideskweb',
      product: 'webfanyi',
      appVersion: '1.0.0',
      vendor: 'web',
      pointParam: 'client,mysticTime,product',
      mysticTime: t,
      keyfrom: 'fanyi.web'
  })
}
// console.log(f())
